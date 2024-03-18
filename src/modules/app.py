import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from ..models.account import Account
from ..models.uris import MYSQL_URI, POSTGRES_URI
from .check_account import CheckAccount
from .deposit import Deposit
from .logged_in_menu import LoggedInMenu
from .login import Login
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
        self.display_login()

        self.mainloop()

    def create_menu(self, menu_type: str):
        if menu_type == "main":
            return MainMenu(self)

        if menu_type == "logged_in":
            return LoggedInMenu(self)

    def display_menu(self, menu_type) -> None:
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

    def display_login(self) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = Login(self)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def display_sign_up(self) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = SignUp(self)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def display_check_account(self) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = CheckAccount(self)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def display_logged_menu_frame(self) -> None:
        self.menu_frame.display_logged_menu_()

    def display_view_account(self) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = ViewAccount(self)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def display_deposit(self) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = Deposit(self)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def display_withdraw(self) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = Withdraw(self)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def display_transferance(self) -> None:
        try:
            self.displayed_frame.destroy()
        except:
            pass
        self.displayed_frame = Transference(self)
        self.displayed_frame.grid(
            row=0,
            column=1,
        )

    def update_object_account(self):
        stmt = select(Account).where(Account.id == self.account.id)
        self.account = session.execute(stmt).scalars().first()
