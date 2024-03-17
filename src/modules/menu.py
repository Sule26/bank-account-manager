import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from ..models.uris import MYSQL_URI, POSTGRES_URI

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Menu(ctk.CTkFrame):
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
            command=lambda: self.parent.display_check_account(),
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
