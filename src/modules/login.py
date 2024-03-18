import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from ..models.account import Account
from ..models.uris import MYSQL_URI, POSTGRES_URI
from ..models.user import User

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


class Login(ctk.CTkFrame):
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
                parent,
                self.username_entry.get(),
                self.password_entry.get(),
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
        if all(
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
            parent.display_menu(menu_type="logged_in")
            parent.display_view_account()

    def check_entry(
        self,
        entry: ctk.CTkEntry,
        entry_name: str,
        warning_label: ctk.CTkLabel,
    ) -> bool:
        warning_row = {
            "username": 2,
            "password": 4,
        }
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
