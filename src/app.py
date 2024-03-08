import ctypes

import customtkinter as ctk

from .models.accountType import ACCOUNT_TYPES
from .models.bank import BANK_NAMES

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FONT_NAME = "Arial"
FONT_SIZE_TITLE = 30
FONT_SIZE_TEXT = 16


class App(ctk.CTk):
    def __init__(self, title: str, screen_size: tuple) -> None:
        super().__init__()
        self.title(title)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - screen_size[0]) / 2
        y = (screen_height - screen_size[1]) / 2
        self.geometry(f"{screen_size[0]}x{screen_size[1]}+{int(x)}+{int(y)}")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)

        self.menu_frame = MenuFrame(self)
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
        self.login_frame = LoginFrame(self)
        self.login_frame.grid(
            row=0,
            column=1,
        )

    def display_sign_up(self) -> None:
        if hasattr(self, "login_frame"):
            self.login_frame.destroy()
        self.sign_up_frame = SignUpFrame(self)
        self.sign_up_frame.grid(
            row=0,
            column=1,
        )


class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.grid_rowconfigure(4, weight=1)

        self.login_button = ctk.CTkButton(
            master=self,
            text="Login",
            command=lambda: parent.display_login(),
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
        self.apperance_mode_openmenu.set("Dark")
        self.login_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=30,
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
            pady=10,
        )

    def change_appearance_mode(self, new_appearance_mode: str) -> None:
        ctk.set_appearance_mode(new_appearance_mode)


class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)

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
        self.password_label = ctk.CTkLabel(
            master=self,
            text="Password:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.password_entry = ctk.CTkEntry(
            master=self,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.sign_in_button = ctk.CTkButton(
            master=self,
            text="Sign In",
        )
        self.sign_up_button = ctk.CTkButton(
            master=self,
            text="Sign Up",
            command=lambda: parent.display_sign_up(),
        )

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
            pady=10,
        )
        self.username_entry.grid(
            row=1,
            column=1,
            padx=20,
            pady=10,
        )
        self.password_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
        )
        self.password_entry.grid(
            row=2,
            column=1,
            padx=20,
            pady=10,
        )
        self.sign_in_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=20,
            sticky="we",
        )
        self.sign_up_button.grid(
            row=3,
            column=1,
            padx=20,
            pady=20,
            sticky="we",
        )


class SignUpFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)

        self.user_credential_frame = ctk.CTkFrame(
            master=self,
            border_width=1,
        )
        self.account_credential_frame = ctk.CTkFrame(
            master=self,
            border_width=1,
        )
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Sign Up",
            font=(FONT_NAME, FONT_SIZE_TITLE),
        )
        self.user_credential_frame.grid(
            row=1,
            column=0,
            padx=(10, 5),
            pady=10,
        )
        self.account_credential_frame.grid(
            row=1,
            column=1,
            sticky="ns",
            padx=(5, 10),
            pady=10,
        )
        self.sign_up_button = ctk.CTkButton(
            master=self,
            text="Sign In",
        )
        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10,
        )
        self.sign_up_button.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10,
            # sticky="we"
        )
        # Create widgets from user_credential_frame
        self.first_name_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="First Name:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.first_name_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.last_name_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="Last Name:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.last_name_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.cpf_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="CPF:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.cpf_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.email_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="Email:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.email_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.phone_label = ctk.CTkLabel(
            master=self.user_credential_frame,
            text="Phone:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.phone_entry = ctk.CTkEntry(
            master=self.user_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )

        # Set layout from user_account_frame

        self.first_name_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
        )
        self.first_name_entry.grid(
            row=1,
            column=1,
            padx=20,
            pady=10,
        )
        self.last_name_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
        )
        self.last_name_entry.grid(
            row=2,
            column=1,
            padx=20,
            pady=10,
        )
        self.cpf_label.grid(
            row=3,
            column=0,
            padx=20,
            pady=10,
        )
        self.cpf_entry.grid(
            row=3,
            column=1,
            padx=20,
            pady=10,
        )
        self.email_label.grid(
            row=4,
            column=0,
            padx=20,
            pady=10,
        )
        self.email_entry.grid(
            row=4,
            column=1,
            padx=20,
            pady=10,
        )
        self.phone_label.grid(
            row=5,
            column=0,
            padx=20,
            pady=10,
        )
        self.phone_entry.grid(
            row=5,
            column=1,
            padx=20,
            pady=10,
        )

        # Create widgets from account_credential_frame
        self.bank_label = ctk.CTkLabel(
            master=self.account_credential_frame,
            text="Bank:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.bank_optionmenu = ctk.CTkOptionMenu(
            master=self.account_credential_frame,
            values=[bank for bank in BANK_NAMES.values()],
        )
        self.account_type_label = ctk.CTkLabel(
            master=self.account_credential_frame,
            text="Account Type:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.account_type_optionmenu = ctk.CTkOptionMenu(
            master=self.account_credential_frame,
            values=[account_type for account_type in ACCOUNT_TYPES.values()],
        )
        self.balance_label = ctk.CTkLabel(
            master=self.account_credential_frame,
            text="Initial Balance:",
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )
        self.balance_entry = ctk.CTkEntry(
            master=self.account_credential_frame,
            font=(FONT_NAME, FONT_SIZE_TEXT),
        )

        # Set layout from account_credential_frame
        self.bank_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
        )
        self.bank_optionmenu.grid(
            row=0,
            column=1,
            padx=20,
            pady=10,
        )
        self.account_type_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
        )
        self.account_type_optionmenu.grid(
            row=1,
            column=1,
            padx=20,
            pady=10,
            sticky="we",
        )
        self.balance_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
        )
        self.balance_entry.grid(
            row=2,
            column=1,
            padx=20,
            pady=10,
        )
