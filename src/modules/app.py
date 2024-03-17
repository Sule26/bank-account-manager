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
