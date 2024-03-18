from typing import Union

import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from ..models.account import Account
from ..models.uris import MYSQL_URI, POSTGRES_URI
from .check_account import CheckAccount
from .deposit import Deposit
from .logged_in_menu import LoggedInMenu
from .sign_in import SignIn
from .main_menu import MainMenu
from .sign_up import SignUp
from .transference import Transference
from .view_account import ViewAccount
from .withdraw import Withdraw

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

engine = create_engine(url=POSTGRES_URI)
# TODO: Solve the issues related to MySQL Syntax
# engine = create_engine(url=MYSQL_URI)
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

        self.display_menu(menu_type="main")
        self.display_frame(menu_type="sign_in")

        self.mainloop()

    def create_menu(
        self,
        menu_type: str,
    ) -> Union[
        "MainMenu",
        "LoggedInMenu",
    ]:
        if menu_type == "main":
            return MainMenu(self)

        if menu_type == "logged_in":
            return LoggedInMenu(self)

    def display_menu(
        self,
        menu_type,
    ) -> None:
        try:
            self.displayed_menu.destroy()
        except:
            pass
        self.displayed_menu = self.create_menu(menu_type=menu_type)
        self.displayed_menu.grid(
            row=0,
            column=0,
            sticky="nsw",
        )

    def create_frame(
        self,
        frame_type: str,
    ) -> Union[
        "SignIn",
        "SignUp",
        "CheckAccount",
        "ViewAccount",
        "Deposit",
        "Withdraw",
        "Transference",
    ]:
        if frame_type == "sign_in":
            return SignIn(self)

        if frame_type == "sign_up":
            return SignUp(self)

        if frame_type == "check_account":
            return CheckAccount(self)

        if frame_type == "view_account":
            return ViewAccount(self)

        if frame_type == "deposit":
            return Deposit(self)

        if frame_type == "withdraw":
            return Withdraw(self)

        if frame_type == "transference":
            return Transference(self)

    def display_frame(
        self,
        menu_type,
    ) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = self.create_frame(menu_type)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def update_object_account(self):
        stmt = select(Account).where(Account.id == self.account.id)
        self.account = session.execute(stmt).scalars().first()
