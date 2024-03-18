import customtkinter as ctk
from CTkTable import *
from loguru import logger
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from ..models.account import Account
from ..models.uris import MYSQL_URI, POSTGRES_URI

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


class Transference(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.parent = parent

        # Create widgets
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Transference",
            font=(FONT_NAME, FONT_SIZE_TITLE),
        )
        self.current_balance_label = ctk.CTkLabel(
            master=self,
            text="Current Balance:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.current_balance_result = ctk.CTkLabel(
            master=self,
            text=f"${self.parent.account.balance:.2f}",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.secondary_account_number_label = ctk.CTkLabel(
            master=self,
            text="Secondary Account Number:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.secondary_account_number_entry = ctk.CTkEntry(
            master=self,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.secondary_account_number_warning = ctk.CTkLabel(
            master=self,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.value_to_transfer_label = ctk.CTkLabel(
            master=self,
            text="Value to Transfer:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.value_to_transfer_entry = ctk.CTkEntry(
            master=self,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.value_to_transfer_warning = ctk.CTkLabel(
            master=self,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.transfer_button = ctk.CTkButton(
            master=self,
            text="Transfer",
            command=lambda: self.transfer(),
        )

        # Set layout
        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
        )
        self.current_balance_label.grid(
            row=1,
            column=0,
            padx=10,
        )
        self.current_balance_result.grid(
            row=1,
            column=1,
            padx=10,
        )
        self.secondary_account_number_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=5,
        )
        self.secondary_account_number_entry.grid(
            row=2,
            column=1,
            padx=20,
            pady=5,
        )
        self.value_to_transfer_label.grid(
            row=4,
            column=0,
            padx=10,
        )
        self.value_to_transfer_entry.grid(
            row=4,
            column=1,
            padx=10,
        )
        self.transfer_button.grid(
            row=6,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
        )

    def transfer(self) -> None:
        if all(
            [
                self.check_entry(
                    entry=self.secondary_account_number_entry,
                    entry_name="secondary_account_number",
                    warning_label=self.secondary_account_number_warning,
                ),
                self.check_entry(
                    entry=self.value_to_transfer_entry,
                    entry_name="value_to_transfer",
                    warning_label=self.value_to_transfer_warning,
                ),
            ]
        ):
            stmt = select(Account).where(
                Account.number == self.secondary_account_number_entry.get()
            )
            secondary_account = session.execute(stmt).scalars().first()
            self.parent.account.transference(
                value=float(self.value_to_transfer_entry.get()),
                receiver_account=secondary_account,
            )
            self.parent.update_object_account()
            self.current_balance_result.configure(
                text=f"${self.parent.account.balance:.2f}"
            )
            self.value_to_transfer_entry.delete(0, "end")
            self.secondary_account_number_entry.delete(0, "end")

    def check_entry(
        self,
        entry: ctk.CTkEntry,
        entry_name: str,
        warning_label: ctk.CTkLabel,
    ) -> bool:
        warning_row = {
            "secondary_account_number": 3,
            "value_to_transfer": 5,
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

        if entry_name == "secondary_account_number":
            if len(entry.get()) != 11:
                warning_label.configure(text="* Entry must have exactly 11 characters")
                return False

            stmt = select(Account).where(
                Account.number == self.secondary_account_number_entry.get().upper()
            )
            secondary_account = session.execute(stmt).scalars().first()

            if not secondary_account:
                warning_label.configure(text="* Account number not found")
                return False

            if self.parent.account.id == secondary_account.id:
                warning_label.configure(text="* You can't transfer to yourself")
                return False

        if entry_name == "value_to_transfer":
            if not entry.get().isnumeric():
                warning_label.configure(text="* Entry just accept digits")
                return False

        warning_label.grid_forget()
        return True
