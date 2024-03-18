import customtkinter as ctk
from CTkTable import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class LoggedInMenu(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.grid_rowconfigure(6, weight=1)

        # Create widgets
        self.view_account_button = ctk.CTkButton(
            master=self,
            text="View Account",
            command=lambda: self.parent.display_view_account(),
        )
        self.deposit_button = ctk.CTkButton(
            master=self,
            text="Deposit",
            command=lambda: self.parent.display_deposit(),
        )
        self.withdraw_button = ctk.CTkButton(
            master=self,
            text="Withdraw",
            command=lambda: self.parent.display_withdraw(),
        )
        self.transference_button = ctk.CTkButton(
            master=self,
            text="Transference",
            command=lambda: self.parent.display_transferance(),
        )
        self.watch_account_button = ctk.CTkButton(
            master=self,
            text="Check Account",
            command=lambda: self.parent.display_check_account(),
        )
        self.log_out_button = ctk.CTkButton(
            master=self,
            text="Logout",
            command=lambda: [
                self.parent.display_login(),
                self.disconnect(),
                self.parent.display_menu(menu_type="main"),
            ],
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
        self.watch_account_button.grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
        )
        self.log_out_button.grid(
            row=5,
            column=0,
            padx=10,
            pady=10,
        )
        self.apperance_mode_label.grid(
            row=7,
            column=0,
            padx=10,
        )
        self.apperance_mode_openmenu.grid(
            row=8,
            column=0,
            padx=10,
            pady=(10, 30),
        )

    def disconnect(self) -> None:
        delattr(self.parent, "account")

    def change_appearance_mode(self, new_appearance_mode: str) -> None:
        ctk.set_appearance_mode(new_appearance_mode)
