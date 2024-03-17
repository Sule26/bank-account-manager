import ctypes
import re

import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, or_, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from .models.account import Account
from .models.accountRule import AccountRule
from .models.accountType import ACCOUNT_TYPES, AccountType
from .models.bank import BANK_NAMES, Bank
from .models.base import Base
from .models.uris import MYSQL_URI, POSTGRES_URI
from .models.user import User

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FONT_NAME = "Arial"
FONT_SIZE_TITLE = 30
FONT_SIZE_TEXT = 16
FONT_SIZE_WARNING = 7
WARNING_TEXT_COLOR = "red"

engine = create_engine(url=POSTGRES_URI)
Session = sessionmaker(bind=engine)
session = Session()


class App(ctk.CTk):
    def __init__(self, title: str, screen_size: tuple) -> None:
        super().__init__()
        self.title(title)
        self.account: "Account"
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - screen_size[0]) / 2
        y = (screen_height - screen_size[1]) / 2
        self.geometry(f"{screen_size[0]}x{screen_size[1]}+{int(x)}+{int(y)}")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)

        self.menu_frame = MenuFrame(self)
        self.menu_frame.grid_rowconfigure(4, weight=1)
        self.menu_frame.grid(
            row=0,
            column=0,
            sticky="nsw",
        )

        self.display_login()

        self.mainloop()

    def display_login(self) -> None:
        if hasattr(self, "sign_up_frame"):
            self.sign_up_frame.destroy()
        if hasattr(self, "account_table_frame"):
            self.check_account_frame.destroy()
        self.login_frame = LoginFrame(self)
        self.login_frame.grid(
            row=0,
            column=1,
        )

    def display_sign_up(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        if hasattr(self, "account_table_frame"):
            self.check_account_frame.destroy()
        self.sign_up_frame = SignUpFrame(self)
        self.sign_up_frame.grid(
            row=0,
            column=1,
        )

    def display_account_table(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        if hasattr(self, "sign_up_frame"):
            self.sign_up_frame.destroy()
        self.check_account_frame = CheckAccountFrame(self)
        self.check_account_frame.grid(
            row=0,
            column=1,
        )

    def display_logged_menu_frame(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        if hasattr(self, "sign_up_frame"):
            self.sign_up_frame.destroy()
        self.menu_frame.display_logged_menu_()

            row=0,
            column=0,
            sticky="nsw",
        )


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.display_main_menu()

    def display_main_menu(self) -> None:
        # Create widgets
        self.login_button = ctk.CTkButton(
            master=self,
            text="Login",
            command=lambda: self.parent.display_login(),
        )
        self.watch_account_button = ctk.CTkButton(
            master=self,
            text="Check Account",
            command=lambda: self.parent.display_account_table(),
        )
        self.faq_button = ctk.CTkButton(
            master=self,
            text="FAQ",
        )
        self.apperance_mode_label = ctk.CTkLabel(
            master=self,
            text="Apperance Mode:",
        )
        self.apperance_mode_openmenu = ctk.CTkOptionMenu(
            master=self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode,
        )

        # Set default
        self.apperance_mode_openmenu.set("Dark")

        # Set layout
        self.login_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=(30, 10),
        )
        self.watch_account_button.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )
        self.faq_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
        )
        self.apperance_mode_label.grid(
            row=5,
            column=0,
            padx=10,
        )
        self.apperance_mode_openmenu.grid(
            row=6,
            column=0,
            padx=10,
            pady=(10, 30),
        )

    def display_logged_menu_(self) -> None:
        self.grid_forget_main_menu()

        # Create widgets
        self.view_account_button = ctk.CTkButton(
            master=self,
            text="View Account",
            command=lambda: self.parent.display_view_account(),
        )
        self.deposit_button = ctk.CTkButton(
            master=self,
            text="Deposit",
        )
        self.withdraw_button = ctk.CTkButton(
            master=self,
            text="Withdraw",
        )
        self.transference_button = ctk.CTkButton(
            master=self,
            text="Transference",
        )
        self.apperance_mode_label = ctk.CTkLabel(
            master=self,
            text="Apperance Mode:",
        )
        self.apperance_mode_openmenu = ctk.CTkOptionMenu(
            master=self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode,
        )

        # Set layout
        self.view_account_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=(30, 10),
        )
        self.deposit_button.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )
        self.withdraw_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
        )
        self.transference_button.grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
        )

    def grid_forget_logged_menu(self) -> None:
        self.view_account_button.grid_forget()
        self.deposit_button.grid_forget()
        self.withdraw_button.grid_forget()
        self.transference_button.grid_forget()

    def grid_forget_main_menu(self) -> None:
        self.login_button.grid_forget()
        self.watch_account_button.grid_forget()
        self.faq_button.grid_forget()

    def change_appearance_mode(self, new_appearance_mode: str) -> None:
        ctk.set_appearance_mode(new_appearance_mode)


class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)

        # Create widgets
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Login",
            font=(FONT_NAME, FONT_SIZE_TITLE),
        )
        self.username_label = ctk.CTkLabel(
            master=self,
            text="Username:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.username_entry = ctk.CTkEntry(
            master=self,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.username_warning = ctk.CTkLabel(
            master=self,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.password_label = ctk.CTkLabel(
            master=self,
            text="Password:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.password_entry = ctk.CTkEntry(
            master=self,
            font=(FONT_NAME, FONT_SIZE_TEXT),
            show="*",
        )
        self.password_warning = ctk.CTkLabel(
            master=self,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.login_warning = ctk.CTkLabel(
            master=self,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.sign_in_button = ctk.CTkButton(
            master=self,
            text="Sign In",
            command=lambda: self.login(
                parent, self.username_entry.get(), self.password_entry.get()
            ),
        )
        self.sign_up_button = ctk.CTkButton(
            master=self,
            text="Sign Up",
            command=lambda: parent.display_sign_up(),
        )

        # Set layout
        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10,
        )
        self.username_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=5,
        )
        self.username_entry.grid(
            row=1,
            column=1,
            padx=20,
            pady=5,
        )
        self.password_label.grid(
            row=3,
            column=0,
            padx=20,
            pady=5,
        )
        self.password_entry.grid(
            row=3,
            column=1,
            padx=20,
            pady=5,
        )
        self.sign_in_button.grid(
            row=5,
            column=0,
            padx=20,
            pady=20,
            sticky="we",
        )
        self.sign_up_button.grid(
            row=5,
            column=1,
            padx=20,
            pady=20,
            sticky="we",
        )

    def login(self, parent: ctk.CTk, username: str, password: str) -> None:
        if any(
            [
                self.check_entry(
                    self.username_entry,
                    "username",
                    self.username_warning,
                ),
                self.check_entry(
                    self.password_entry,
                    "password",
                    self.password_warning,
                ),
            ]
        ):
            self.login_warning.grid(
                row=4,
                column=0,
                columnspan=2,
            )
            stmt = (
                select(Account)
                .join(User)
                .where(User.username == username, User.password == password)
            )
            parent.account = session.execute(stmt).scalars().first()

            if not parent.account:
                self.login_warning.configure(
                    text="* Username or Password does not exist"
                )
                return

            self.login_warning.grid_forget()
            parent.display_logged_menu_frame()

    def check_entry(
        self, entry: ctk.CTkEntry, entry_name: str, warning_label: ctk.CTkLabel
    ) -> bool:
        warning_row = {"username": 2, "password": 4}
        warning_label.grid(
            row=warning_row[entry_name],
            column=1,
        )

        if entry.get() == "":
            warning_label.configure(text="* Entry can't be blank")
            return False

        if " " in entry.get():
            warning_label.configure(text="* Entry can't have spaces")
            return False

        if len(entry.get()) < 6:
            warning_label.configure(text="* Entry must have at least 6 characters")
            return False

        warning_label.grid_forget()
        return True


class SignUpFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)

        # Create widgets
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Sign Up",
            font=(FONT_NAME, FONT_SIZE_TITLE),
        )
        self.user_credential_frame = ctk.CTkFrame(
            master=self,
            border_width=1,
        )
        self.account_credential_frame = ctk.CTkFrame(
            master=self,
            border_width=1,
        )
        self.sign_up_button = ctk.CTkButton(
            master=self,
            text="Sign Up",
            command=lambda: self.sign_up(),
        )

        # Set layout
        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10,
        )
        self.user_credential_frame.grid(
            row=1,
            column=0,
            padx=(10, 5),
            pady=10,
        )
        self.account_credential_frame.grid(
            row=1,
            column=1,
            sticky="ns",
            padx=(5, 10),
            pady=10,
        )
        self.sign_up_button.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10,
            # sticky="we"
        )
        # Create widgets from user_credential_frame
        self.first_name_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="First Name:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.first_name_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.first_name_warning = ctk.CTkLabel(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.last_name_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="Last Name:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.last_name_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.last_name_warning = ctk.CTkLabel(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.cpf_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="CPF:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.cpf_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.cpf_warning = ctk.CTkLabel(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.email_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="Email:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.email_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.email_warning = ctk.CTkLabel(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.phone_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="Phone:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.phone_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.phone_warning = ctk.CTkLabel(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )

        # Set layout from user_account_frame
        self.first_name_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=(10, 0),
        )
        self.first_name_entry.grid(
            row=1,
            column=1,
            padx=20,
            pady=5,
        )
        self.last_name_label.grid(
            row=3,
            column=0,
            padx=20,
            pady=5,
        )
        self.last_name_entry.grid(
            row=3,
            column=1,
            padx=20,
            pady=5,
        )
        self.cpf_label.grid(
            row=5,
            column=0,
            padx=20,
            pady=5,
        )
        self.cpf_entry.grid(
            row=5,
            column=1,
            padx=20,
            pady=5,
        )
        self.email_label.grid(
            row=7,
            column=0,
            padx=20,
            pady=5,
        )
        self.email_entry.grid(
            row=7,
            column=1,
            padx=20,
            pady=5,
        )
        self.phone_label.grid(
            row=9,
            column=0,
            padx=20,
            pady=5,
        )
        self.phone_entry.grid(
            row=9,
            column=1,
            padx=20,
            pady=5,
        )

        # Create widgets from account_credential_frame
        self.bank_label = ctk.CTkLabel(
            master=self.account_credential_frame,
            text="Bank:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.bank_optionmenu = ctk.CTkOptionMenu(
            master=self.account_credential_frame,
            values=[bank for bank in BANK_NAMES.values()],
        )
        self.account_type_label = ctk.CTkLabel(
            master=self.account_credential_frame,
            text="Account Type:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.account_type_optionmenu = ctk.CTkOptionMenu(
            master=self.account_credential_frame,
            values=[account_type for account_type in ACCOUNT_TYPES.values()],
        )
        self.balance_label = ctk.CTkLabel(
            master=self.account_credential_frame,
            text="Initial Balance:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.balance_entry = ctk.CTkEntry(
            master=self.account_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.balance_warning = ctk.CTkLabel(
            master=self.account_credential_frame,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )

        # Set layout from account_credential_frame
        self.bank_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=5,
        )
        self.bank_optionmenu.grid(
            row=0,
            column=1,
            padx=20,
            pady=5,
        )
        self.account_type_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=5,
        )
        self.account_type_optionmenu.grid(
            row=1,
            column=1,
            padx=20,
            pady=5,
            sticky="we",
        )
        self.balance_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=5,
        )
        self.balance_entry.grid(
            row=2,
            column=1,
            padx=20,
            pady=5,
        )

    def sign_up(self) -> None:
        if any(
            [
                self.check_entry(
                    entry=self.first_name_entry,
                    entry_name="first_name",
                    warning_label=self.first_name_warning,
                ),
                self.check_entry(
                    entry=self.last_name_entry,
                    entry_name="last_name",
                    warning_label=self.last_name_warning,
                ),
                self.check_entry(
                    entry=self.cpf_entry,
                    entry_name="cpf",
                    warning_label=self.cpf_warning,
                ),
                self.check_entry(
                    entry=self.email_entry,
                    entry_name="email",
                    warning_label=self.email_warning,
                ),
                self.check_entry(
                    entry=self.phone_entry,
                    entry_name="phone",
                    warning_label=self.phone_warning,
                ),
                self.check_entry(
                    entry=self.balance_entry,
                    entry_name="balance",
                    warning_label=self.balance_warning,
                ),
            ]
        ):
            pass

    def check_entry(
        self, entry: ctk.CTkEntry, entry_name: str, warning_label: ctk.CTkLabel
    ) -> bool:
        warning_row = {
            "first_name": 2,
            "balance": 3,
            "last_name": 4,
            "cpf": 6,
            "email": 8,
            "phone": 10,
        }
        warning_label.grid(
            row=warning_row[entry_name],
            column=1,
        )
        if entry.get() == "":
            warning_label.configure(text="* Entry can't be blank")
            return False

        if " " in entry.get():
            warning_label.configuer(text="* Entry can't have spaces")
            return False

        if entry_name in ["first_name", "last_name"]:
            if not entry.get().isalpha():
                warning_label.configure(text="* Entry can't have numbers")
                return False

        if entry_name == "cpf":
            if not entry.get().isnumeric():
                warning_label.configure(text="* Entry just accept digits")
                return False
            if len(entry.get()) != 11:
                warning_label.configure(text="* Entry must have exactly 11 digits")
                return False
            # if not validate_cpf(entry.get()):
            #     warning_label.configure(text="* CPF is not valid")
            #     return False

        if entry_name == "email":
            if not re.search(
                "/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$/", entry.get()
            ):
                warning_label.configure(text="* Not a valid email")
                return False

        if entry_name == "phone":
            if not entry.get().isnumeric():
                warning_label.configure(text="* Entry must have only digits")
                return False

            if len(entry.get()) != 9:
                warning_label.configure(text="* Entry must have exactly 9 digits")
                return False

        if entry_name == "balance":
            if not entry.get().isnumeric():
                warning_label.configure(text="* Entry must have only digits")
                return False

            stmt = (
                select(AccountRule.minimum_initial_balance)
                .join(AccountType)
                .join(Bank)
                .where(
                    AccountType.name == self.account_type_optionmenu.get(),
                    Bank.name == self.bank_optionmenu.get(),
                )
            )
            minimum_initial_balance = session.execute(stmt).scalars().first()

            if int(entry.get()) < minimum_initial_balance:

                warning_label.configure(
                    text=f"* Minimum balance is ${minimum_initial_balance:.2f}"
                )
                return False

        warning_label.grid_forget()
        return True


class CheckAccountFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk):
        super().__init__(master=parent)
        self.values = [["Number", "Balance"]]

        # Create widgets
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Check Account",
            font=(FONT_NAME, FONT_SIZE_TITLE),
        )
        self.number_account_label = ctk.CTkLabel(
            master=self,
            text="Account Number:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.number_account_entry = ctk.CTkEntry(
            master=self,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.account_table = CTkTable(
            master=self,
            values=self.values,
        )
        self.check_random_button = ctk.CTkButton(
            master=self,
            text="Check Random Account",
            command=lambda: self.update_table(),
        )
        self.check_button = ctk.CTkButton(
            master=self,
            text="Check Account",
            command=lambda: self.update_table(self.number_account_entry.get()),
        )

        # Set layout
        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
        )
        self.number_account_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )
        self.number_account_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
        )
        self.check_random_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
        )
        self.check_button.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
        )

    def update_table(self, account_number: str = None):
        self.account_table.delete_row(index=2)

        if account_number:
            stmt = select(Account).where(Account.number == account_number)
        else:
            stmt = select(Account).order_by(func.random())

        account_row = session.execute(stmt).scalars().first()

        self.account_table.add_row([account_row.number, account_row.balance])

        self.account_table.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
        )
