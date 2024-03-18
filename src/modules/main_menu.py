import customtkinter as ctk
from CTkTable import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainMenu(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.grid_rowconfigure(2, weight=1)


        # Create widgets
        self.login_button = ctk.CTkButton(
            master=self,
            text="Login",
            command=lambda: self.parent.display_login(),
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
        self.faq_button.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )
        self.apperance_mode_label.grid(
            row=3,
            column=0,
            padx=10,
        )
        self.apperance_mode_openmenu.grid(
            row=4,
            column=0,
            padx=10,
            pady=(10, 30),
        )

    def change_appearance_mode(self, new_appearance_mode: str) -> None:
        ctk.set_appearance_mode(new_appearance_mode)
