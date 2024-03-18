import re

import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from ..models.accountRule import AccountRule
from ..models.accountType import ACCOUNT_TYPES, AccountType
from ..models.bank import BANK_NAMES, Bank
from ..models.uris import MYSQL_URI, POSTGRES_URI

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FONT_NAME = "Arial"
FONT_SIZE_TITLE = 30
FONT_SIZE_TEXT = 16
FONT_SIZE_WARNING = 7
WARNING_TEXT_COLOR = "red"

engine = create_engine(url=POSTGRES_URI)
# TODO: Solve the issues related to MySQL Syntax
# engine = create_engine(url=MYSQL_URI)
Session = sessionmaker(bind=engine)
session = Session()


class SignUp(ctk.CTkFrame):
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
        if all(
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

            if float(entry.get()) < minimum_initial_balance:

                warning_label.configure(
                    text=f"* Minimum balance is ${minimum_initial_balance:.2f}"
                )
                return False

        warning_label.grid_forget()
        return True
