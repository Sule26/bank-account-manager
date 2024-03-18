import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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


class Deposit(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.parent = parent

        # Create widgets
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Deposit",
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
        self.value_to_deposit_label = ctk.CTkLabel(
            master=self,
            text="Value to Deposit:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.value_to_deposit_entry = ctk.CTkEntry(
            master=self,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.value_to_deposit_warning = ctk.CTkLabel(
            master=self,
            font=(FONT_NAME, FONT_SIZE_WARNING),
            text_color=WARNING_TEXT_COLOR,
        )
        self.deposit_button = ctk.CTkButton(
            master=self,
            text="Deposit",
            command=lambda: self.deposit(),
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
            padx=20,
            pady=5,
        )
        self.current_balance_result.grid(
            row=1,
            column=1,
            padx=20,
            pady=5,
        )
        self.value_to_deposit_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=5,
        )
        self.value_to_deposit_entry.grid(
            row=2,
            column=1,
            padx=20,
            pady=5,
        )
        self.deposit_button.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
        )

    def deposit(self) -> None:
        if self.check_entry(
            entry=self.value_to_deposit_entry,
            warning_label=self.value_to_deposit_warning,
        ):
            self.parent.account.deposit(value=float(self.value_to_deposit_entry.get()))
            self.parent.update_object_account()
            self.current_balance_result.configure(
                text=f"${self.parent.account.balance:.2f}"
            )
            self.value_to_deposit_entry.delete(0, "end")

    def check_entry(
        self,
        entry: ctk.CTkEntry,
        warning_label: ctk.CTkLabel,
    ) -> bool:
        warning_label.grid(
            row=3,
            column=1,
        )
        if entry.get() == "":
            warning_label.configure(text="* Entry can't be blank")
            return False

        if " " in entry.get():
            warning_label.configure(text="* Entry can't have spaces")
            return False

        if not entry.get().isnumeric():
            warning_label.configure(text="* Entry must have only digits")
            return False

        warning_label.grid_forget()
        return True
