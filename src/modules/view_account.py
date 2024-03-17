import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, or_, select
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


class ViewAccount(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.parent = parent

        # Create widgets
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Account",
            font=(FONT_NAME, FONT_SIZE_TITLE),
        )
        self.user_info_frame = ctk.CTkFrame(
            master=self,
            border_width=1,
        )
        self.account_info_frame = ctk.CTkFrame(
            master=self,
            border_width=1,
        )

        # Set layout
        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10,
        )
        self.user_info_frame.grid(
            row=1,
            column=0,
            padx=(10, 5),
            pady=10,
        )
        self.account_info_frame.grid(
            row=1,
            column=1,
            sticky="ns",
            padx=(5, 10),
            pady=10,
        )

        # Create widgets from user_info_frame
        self.first_name_label = ctk.CTkLabel(
            master=self.user_info_frame,
            text="First Name:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.first_name_result = ctk.CTkLabel(
            master=self.user_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.last_name_label = ctk.CTkLabel(
            master=self.user_info_frame,
            text="Last Name:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.last_name_result = ctk.CTkLabel(
            master=self.user_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.cpf_label = ctk.CTkLabel(
            master=self.user_info_frame,
            text="CPF:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.cpf_result = ctk.CTkLabel(
            master=self.user_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.email_label = ctk.CTkLabel(
            master=self.user_info_frame,
            text="Email:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.email_result = ctk.CTkLabel(
            master=self.user_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.phone_label = ctk.CTkLabel(
            master=self.user_info_frame,
            text="Phone:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.phone_result = ctk.CTkLabel(
            master=self.user_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        # Set layout from user_info_frame
        self.first_name_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=(10, 0),
        )
        self.first_name_result.grid(
            row=1,
            column=1,
            padx=20,
            pady=(10, 0),
        )
        self.last_name_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=5,
        )
        self.last_name_result.grid(
            row=2,
            column=1,
            padx=20,
            pady=5,
        )
        self.cpf_label.grid(
            row=3,
            column=0,
            padx=20,
            pady=5,
        )
        self.cpf_result.grid(
            row=3,
            column=1,
            padx=20,
            pady=5,
        )
        self.email_label.grid(
            row=4,
            column=0,
            padx=20,
            pady=5,
        )
        self.email_result.grid(
            row=4,
            column=1,
            padx=20,
            pady=5,
        )
        self.phone_label.grid(
            row=5,
            column=0,
            padx=20,
            pady=5,
        )
        self.phone_result.grid(
            row=5,
            column=1,
            padx=20,
            pady=5,
        )

        # Create widgets from account_info_frame
        self.bank_label = ctk.CTkLabel(
            master=self.account_info_frame,
            text="Bank:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.bank_result = ctk.CTkLabel(
            master=self.account_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.account_type_label = ctk.CTkLabel(
            master=self.account_info_frame,
            text="Account Type:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.account_type_result = ctk.CTkLabel(
            master=self.account_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.balance_label = ctk.CTkLabel(
            master=self.account_info_frame,
            text="Initial Balance:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.balance_result = ctk.CTkLabel(
            master=self.account_info_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )

        # Set layout from account_info_frame
        self.bank_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=5,
        )
        self.bank_result.grid(
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
        self.account_type_result.grid(
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
        self.balance_result.grid(
            row=2,
            column=1,
            padx=20,
            pady=5,
        )
        self.get_account()

    def get_account(self) -> None:
        self.first_name_result.configure(text=f"{self.parent.account.user.first_name}")
        self.last_name_result.configure(text=f"{self.parent.account.user.last_name}")
        self.cpf_result.configure(text=f"{self.parent.account.user.cpf}")
        self.email_result.configure(text=f"{self.parent.account.user.email}")
        self.phone_result.configure(text=f"{self.parent.account.user.phone}")
        self.bank_result.configure(text=f"{self.parent.account.account_type.bank.name}")
        self.account_type_result.configure(
            text=f"{self.parent.account.account_type.name}"
        )
        self.balance_result.configure(text=f"${self.parent.account.balance:.2f}")
