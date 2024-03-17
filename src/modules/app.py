import customtkinter as ctk
from CTkTable import *
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from ..models.account import Account
from ..models.uris import MYSQL_URI, POSTGRES_URI
from .check_account import CheckAccount
from .login import Login
from .menu import Menu
from .sign_up import SignUp
from .view_account import ViewAccount

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

        self.menu_frame = Menu(self)
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
        if hasattr(self, "check_account_frame"):
            self.check_account_frame.destroy()
        if hasattr(self, "view_account_frame"):
            self.view_account_frame.destroy()
        self.login_frame = Login(self)
        self.login_frame.grid(
            row=0,
            column=1,
        )

    def display_sign_up(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        if hasattr(self, "check_account_frame"):
            self.check_account_frame.destroy()
        if hasattr(self, "view_account_frame"):
            self.view_account_frame.destroy()
        self.sign_up_frame = SignUp(self)
        self.sign_up_frame.grid(
            row=0,
            column=1,
        )

    def display_check_account(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        if hasattr(self, "sign_up_frame"):
            self.sign_up_frame.destroy()
        if hasattr(self, "check_account_frame"):
            self.check_account_frame.destroy()
        if hasattr(self, "view_account_frame"):
            self.view_account_frame.destroy()
        self.check_account_frame = CheckAccount(self)
        self.check_account_frame.grid(
            row=0,
            column=1,
        )

    def display_logged_menu_frame(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        if hasattr(self, "sign_up_frame"):
            self.sign_up_frame.destroy()
        if hasattr(self, "check_account_frame"):
            self.check_account_frame.destroy()
        if hasattr(self, "view_account"):
            self.view_account_frame.destroy()
        self.menu_frame.display_logged_menu_()

    def display_view_account(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        if hasattr(self, "sign_up_frame"):
            self.sign_up_frame.destroy()
        if hasattr(self, "check_account_frame"):
            self.check_account_frame.destroy()
        self.view_account_frame = ViewAccount(self)
        self.view_account_frame.grid(
            row=0,
            column=1,
        )
