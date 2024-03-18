import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from ..models.account import Account
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


class CheckAccount(ctk.CTkFrame):
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

        self.account_table.add_row([account_row.number, f"${account_row.balance:.2f}"])

        self.account_table.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
        )
