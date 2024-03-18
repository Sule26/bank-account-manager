import customtkinter as ctk
from CTkTable import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainMenu(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.grid_rowconfigure(3, weight=1)

        # Create widgets
        self.sign_in_button = ctk.CTkButton(
            master=self,
            text="Sign In",
            command=lambda: self.parent.display_frame(menu_type="sign_in"),
        )
        self.sign_up_button = ctk.CTkButton(
            master=self,
            text="Sign Up",
            command=lambda: parent.display_frame(menu_type="sign_up"),
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
            values=["Light", "Dark"],
            command=self.change_appearance_mode,
        )

        # Set default
        self.apperance_mode_openmenu.set(ctk.get_appearance_mode())

        # Set layout
        self.sign_in_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=(30, 10),
        )
        self.sign_up_button.grid(
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
            row=4,
            column=0,
            padx=10,
        )
        self.apperance_mode_openmenu.grid(
            row=5,
            column=0,
            padx=10,
            pady=(10, 30),
        )

    def change_appearance_mode(self, new_appearance_mode: str) -> None:
        ctk.set_appearance_mode(new_appearance_mode)
