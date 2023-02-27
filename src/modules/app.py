from src.modules.cpf.cpf import Cpf
from PIL import ImageTk, Image
import tkinter as tk


class App:
    WIDTH = 600
    HEIGHT = 600

    def __init__(self):
        self.main_window()

    def main_window(self):
        self.root = tk.Tk()
        self.root.title("Bank System")
        self.root.iconbitmap("src/images/icon.ico")
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.root.config(bg='#207050')
        self.root.resizable(False, False)

        self.cpf_object = Cpf()
        self.ACCOUNT_TYPES = ["Current Account", "Saving Account"]
        self.type_choosen = tk.StringVar()
        self.type_choosen.set(self.ACCOUNT_TYPES[0])

        # TITLE LABEL
        self.title_label = tk.Label(self.root, text="Bank System", font=('Arial', 50), bg='#207050')
        self.title_label.place(x=110, y=10)
        # Logo
        self.logo = ImageTk.PhotoImage(Image.open("src/images/logo.png"))
        self.logo_label = tk.Label(image=self.logo, bg='#207050')
        self.logo_label.place(x=270, y=150)

        # LoginFrame
        self.loginFrame = tk.LabelFrame(self.root, relief=tk.SUNKEN)
        self.loginFrame.place(x=200, y=250)

        self.title_loginFrame_label = tk.Label(self.loginFrame, text='Sign In', font=('Arial', 18))
        self.title_loginFrame_label.grid(row=0, column=0, columnspan=3, sticky=tk.W + tk.E)

        self.username_label = tk.Label(self.loginFrame, text="Username")
        self.username_label.grid(row=1, column=0, sticky=tk.W)

        self.password_label = tk.Label(self.loginFrame, text="Password")
        self.password_label.grid(row=2, column=0, sticky=tk.W)

        self.username = tk.Entry(self.loginFrame, width=20)
        self.username.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky=tk.W)

        self.password = tk.Entry(self.loginFrame, width=20, show="*")
        self.password.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky=tk.W)

        self.login_btn = tk.Button(self.loginFrame, text="Login", width=20)
        self.login_btn.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W + tk.E)

        self.sing_up = tk.Button(self.loginFrame, text='Sing Up', width=20, command=self.register_window)
        self.sing_up.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W + tk.E)

        self.root.mainloop()

    def register_window(self):
        self.register_window = tk.Toplevel()
        self.register_window.title("Creating a new account")
        self.register_window.iconbitmap("src/images/icon.ico")
        self.register_window.resizable(False, False)
        # RegisterFrame
        self.registerFrame = tk.LabelFrame(self.register_window, text="Create an Account", bg='#707070', font=('Arial', 18))
        self.registerFrame.pack()

        #   RegisterFrameUser
        self.registerFrameUser = tk.LabelFrame(self.registerFrame, text="User's Infos")
        self.registerFrameUser.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        #   RegisterFrameUser Label
        self.f_name_label = tk.Label(self.registerFrameUser, text="First Name")
        self.f_name_label.grid(row=0, column=0, sticky=tk.W)

        self.l_name_label = tk.Label(self.registerFrameUser, text="Last Name")
        self.l_name_label.grid(row=1, column=0, sticky=tk.W)

        self.age_label = tk.Label(self.registerFrameUser, text="Age")
        self.age_label.grid(row=2, column=0, sticky=tk.W)

        self.cpf_label = tk.Label(self.registerFrameUser, text="CPF")
        self.cpf_label.grid(row=3, column=0, sticky=tk.W)

        #   registerFrameUser Entry
        self.f_name = tk.Entry(self.registerFrameUser, width=30)
        self.f_name.grid(row=0, column=1, columnspan=2, pady=7, padx=(2, 10), sticky=tk.W)

        self.l_name = tk.Entry(self.registerFrameUser, width=30)
        self.l_name.grid(row=1, column=1, columnspan=2, pady=7, padx=(2, 10), sticky=tk.W)

        self.age = tk.Entry(self.registerFrameUser, width=30)
        self.age.grid(row=2, column=1, columnspan=2, pady=7, padx=(2, 10), sticky=tk.W)

        self.cpf = tk.Entry(self.registerFrameUser, width=30)
        self.cpf.grid(row=3, column=1, columnspan=2, pady=7, padx=(2, 10), sticky=tk.W)

        self.btn_verify_cpf = tk.Button(self.registerFrameUser, text="Verify CPF", width=11, command=self.verify_cpf)
        self.btn_verify_cpf.grid(row=4, column=1, pady=7, sticky=tk.W)

        self.btn_generate_cpf = tk.Button(self.registerFrameUser, text="Generate CPF", width=11, command=self.generate_cpf,)
        self.btn_generate_cpf.grid(row=4, column=2, pady=7, sticky=tk.W)

        #   registerFrameAccount
        self.registerFrameAccount = tk.LabelFrame(self.registerFrame, text="Account's infos")
        self.registerFrameAccount.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        #   registerFrameAccount Label
        self.account_type_label = tk.Label(self.registerFrameAccount, text="Choose Type of Account", wraplength=75)
        self.account_type_label.grid(row=0, column=0, sticky=tk.W)

        self.inicial_deposit_label = tk.Label(self.registerFrameAccount, text="Inicial Deposit (US$)", wraplength=75)
        self.inicial_deposit_label.grid(row=1, column=0, sticky=tk.W)

        #   registerFrameAccount Entry
        self.account_type = tk.OptionMenu(self.registerFrameAccount, self.type_choosen, *self.ACCOUNT_TYPES)
        self.account_type.config(width=21)
        self.account_type.grid(row=0, column=1, columnspan=2, pady=7, padx=(0, 10), sticky=tk.W)

        self.inicial_deposit = tk.Entry(self.registerFrameAccount, width=28)
        self.inicial_deposit.grid(row=1, column=1, columnspan=2, pady=7, padx=(0, 10), sticky=tk.W)

        #   registerFrameLogin
        self.registerFrameLogin = tk.LabelFrame(self.registerFrame, text="Login's infos")
        self.registerFrameLogin.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        #   registerFrameLogin Label
        self.register_username_label = tk.Label(self.registerFrameLogin, text="Username")
        self.register_username_label.grid(row=0, column=0, sticky=tk.W)

        self.register_password_label = tk.Label(self.registerFrameLogin, text="Password")
        self.register_password_label.grid(row=1, column=0, sticky=tk.W)

        self.register_repeat_password_label = tk.Label(self.registerFrameLogin, text="Repeat Password", wraplength=75)
        self.register_repeat_password_label.grid(row=2, column=0, sticky=tk.W)

        # registerFrameLogin Entry
        register_username = tk.Entry(self.registerFrameLogin, width=30)
        register_username.grid(row=0, column=1, columnspan=2, pady=7, padx=(2, 10), sticky=tk.W)

        register_password = tk.Entry(self.registerFrameLogin, width=30)
        register_password.grid(row=1, column=1, columnspan=2, pady=7, padx=(2, 10), sticky=tk.W)

        register_repeat_password = tk.Entry(self.registerFrameLogin, width=30)
        register_repeat_password.grid(row=2, column=1, columnspan=2, pady=7, padx=(0, 10), sticky=tk.W)

        # Register button

        submit_btn = tk.Button(self.registerFrame, text="Register", width=30)
        submit_btn.grid(row=3, column=0, columnspan=3, pady=10, padx=10, sticky=tk.W + tk.E)

    def generate_cpf(self) -> None:
        self.cpf.delete(0, tk.END)
        self.cpf.config(fg="black")
        self.cpf.insert(0, self.cpf_object.generateCpf())

    def verify_cpf(self) -> None:
        if self.cpf_object.verifyCpf(self.cpf.get()):
            self.cpf.config(fg="green")
        else:
            self.cpf.config(fg="red")
