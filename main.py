import tkinter as tk
from string import ascii_letters
from sqlite3 import connect


def swap(c):
    try:
        del(app)
        print("Olá")
    except:
        pass
    finally:
        if c.lower() == "login":
            app = Login()
        elif c.lower() == "signin":
            app = SignIn()
        elif c.lower() == "final":
            app = FinalPage()

class FinalPage:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("FinalPage")
        self.x = (self.janela.winfo_screenwidth() / 2) - (700 / 2)
        self.y = (self.janela.winfo_screenheight() / 2) - (600 / 2)
        self.janela.geometry(f"700x600+{int(self.x)}+{int(self.y)}")
        self.frame = tk.Frame(self.janela, width=700, height=600, background="#3A4570")
        self.frame.place(x=0, y=0)
        self.label = tk.Label(master=self.frame,
                              font="Inter 30",
                              bg="#3A4570",
                              fg="#F0B305",
                              text="Você fez login com sucesso!")
        self.label.place(x=20, y=20)

        self.janela.mainloop()

class Login:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Login")
        self.x = (self.janela.winfo_screenwidth() / 2) - (700 / 2)
        self.y = (self.janela.winfo_screenheight() / 2) - (600 / 2)
        self.janela.geometry(f"700x600+{int(self.x)}+{int(self.y)}")
        # Images
        self.backImage = tk.PhotoImage(file="Assets/FundoLoginDesktop.png")
        self.EntryImg1 = tk.PhotoImage(file="Assets/EntryUser.png")
        self.EntryImg2 = tk.PhotoImage(file="Assets/EntryPass.png")
        self.FButton = tk.PhotoImage(file="Assets/LoginFButton.png")
        self.FButton_Pressed = tk.PhotoImage(file="Assets/LoginFButton_Pressed.png")
        self.SButton = tk.PhotoImage(file="Assets/LoginSButton.png")
        self.SButton_Pressed = tk.PhotoImage(file="Assets/LoginSButton_Pressed.png")
        self.TitleImg = tk.PhotoImage(file="Assets/LoginTitle.png")
        self.AsideTitleImg = tk.PhotoImage(file="Assets/LoginAside_Title.png")

        # Imagem de fundo
        self.Bg = tk.Canvas(master=self.janela, width=700, height=600, borderwidth=0,
                            highlightthickness=0)
        self.Bg.pack()
        self.Bg.create_image(350, 300, anchor=tk.CENTER, image=self.backImage)

        # LeftSide
        self.Title = self.Bg.create_image(60, 127, anchor=tk.NW, image=self.AsideTitleImg)
        self.SignInButton = self.Bg.create_image(100, 189,
                                                 anchor=tk.NW,
                                                 image=self.SButton)
        self.Bg.tag_bind(self.SignInButton,
                         "<ButtonPress-1>",
                         lambda _: self.SignInButton_press())
        self.Bg.tag_bind(self.SignInButton,
                         "<ButtonRelease-1>",
                         lambda _: self.SignInButton_release())

        # RightSide
        self.SideFrame = tk.Frame(master=self.Bg, width=400, height=600, bg="#3A4570")
        self.SideFrame.place(x=300, y=0)
        self.SideTitle = tk.Label(master=self.SideFrame,
                                  image=self.TitleImg,
                                  borderwidth=0)
        self.SideTitle.place(x=128, y=22)

        # Inputs
        self.EntryUserBack = tk.Label(master=self.SideFrame,
                                      image=self.EntryImg1,
                                      borderwidth=0)
        self.EntryUserBack.place(x=25, y=128)
        self.EntryUser = tk.Entry(master=self.SideFrame,
                                  width=40,
                                  borderwidth=0,
                                  fg="grey",
                                  font="Inter 10")
        self.EntryUser.place(x=75, y=140)
        self.EntryUser.placeholder = "Nome de usuário ou email"
        self.EntryUser.insert(0, "Nome de usuário ou email")
        self.EntryUser.bind("<FocusIn>",
                            lambda event, entry=self.EntryUser:
                            self.on_focus_in(entry))
        self.EntryUser.bind("<FocusOut>",
                            lambda event, entry=self.EntryUser:
                            self.on_focus_out(entry))
        self.EntryUser.Label = tk.Label(master=self.SideFrame,
                                        text="",
                                        foreground="#ff0000",
                                        bg="#3A4570",
                                        font="Inter 8")
        self.EntryUser.Label.place(x=50, y=174)

        self.EntryPassBack = tk.Label(master=self.SideFrame,
                                      image=self.EntryImg2,
                                      borderwidth=0)
        self.EntryPassBack.place(x=25, y=203)
        self.EntryPass = tk.Entry(master=self.SideFrame,
                                  width=40,
                                  borderwidth=0,
                                  fg="grey",
                                  font="Inter 10")
        self.EntryPass.place(x=75, y=215)
        self.EntryPass.placeholder = "Senha"
        self.EntryPass.insert(0, "Senha")
        self.EntryPass.bind("<FocusIn>",
                            lambda event, entry=self.EntryPass:
                            self.on_focus_in(entry))
        self.EntryPass.bind("<FocusOut>",
                            lambda event, entry=self.EntryPass:
                            self.on_focus_out(entry))
        self.EntryPass.Label = tk.Label(master=self.SideFrame,
                                        text="",
                                        foreground="#ff0000",
                                        bg="#3A4570",
                                        font="Inter 8")
        self.EntryPass.Label.place(x=50, y=249)

        self.LoginButton = tk.Button(self.SideFrame,
                                     image=self.FButton,
                                     borderwidth=0,
                                     highlightthickness=0)
        self.LoginButton.place(x=160, y=309)
        self.LoginButton.bind("<Button-1>", self.white_entry)
        self.LoginButton.bind("<ButtonPress-1>", lambda event, button=self.LoginButton:
        self._on_pressed(button), add=True)
        self.LoginButton.bind("<ButtonRelease-1>", lambda event, button=self.LoginButton:
        self._on_release(button), add=True)

        self.janela.mainloop()

    def on_focus_in(self, entry):
        if entry.get() == entry.placeholder:
            entry["show"] = "*" if "senha" in entry.placeholder.lower() else ""
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(self, entry):
        if entry.get() == "":
            entry["show"] = "" if "senha" in entry.placeholder.lower() else ""
            entry.insert(0, entry.placeholder)
            entry.config(fg="grey")

    def _on_pressed(self, button):
        button.config(image=self.FButton_Pressed)
        return "break"

    def _on_release(self, button):
        button.config(image=self.FButton)
        return "break"

    def SignInButton_press(self):
        self.Bg.itemconfig(self.SignInButton, image=self.SButton_Pressed)

    def SignInButton_release(self):
        self.Bg.itemconfig(self.SignInButton, image=self.SButton)
        self.janela.destroy()
        swap("SignIn")

    def white_entry(self, event):
        args = {"UserEmail": self.EntryUser,
                "Pass": self.EntryPass}
        for entry in args.values():
            if entry.get() == "" or entry.get() == " ":
                entry.Label['text'] = "*Não pode estar vazio"
                break
            elif entry.get() == entry.placeholder:
                entry.Label['text'] = "*Não pode estar vazio"
                break
        else:
            state = 0
            email_or_user = 0
            user_email = args['UserEmail'].get()
            password = args['Pass'].get()
            state += 1 if self.check_database(args['Pass'].get(), what_check="password") else 0
            if args['UserEmail'].get().endswith("@gmail.com"):
                state += 1 if self.check_database(args['UserEmail'].get()) else 0
                email_or_user = 0
            else:
                state += 1 if self.check_database(args['UserEmail'].get(), what_check="name") else 0
                email_or_user = 1
            if state == 2:
                self.janela.destroy()
                swap("final")
                return "break"


    def check_database(self, for_check, what_check='email'):
        for_check = for_check.lower() if what_check == "email" else for_check
        con = connect("data.db")
        exe = con.cursor()
        select = exe.execute("select * from users where ¨ = ?".replace("¨", what_check), (for_check, ))
        if select.fetchall():
            con.close()
            return True
        con.close()
        return False


class SignIn:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Login")
        self.x = (self.janela.winfo_screenwidth() / 2) - (700 / 2)
        self.y = (self.janela.winfo_screenheight() / 2) - (600 / 2)
        self.janela.geometry(f"700x600+{int(self.x)}+{int(self.y)}")
        textVariable = tk.StringVar()
        # Images
        self.backImage = tk.PhotoImage(file="Assets/FundoLoginDesktop.png")
        self.EntryImg1 = tk.PhotoImage(file="Assets/EntryUser.png")
        self.EntryImg2 = tk.PhotoImage(file="Assets/EntryPass.png")
        self.EntryImg3 = tk.PhotoImage(file="Assets/EntryEmail.png")
        self.FButton = tk.PhotoImage(file="Assets/SignInFButton.png")
        self.FButton_Pressed = tk.PhotoImage(file="Assets/SignInFButton_Pressed.png")
        self.SButton = tk.PhotoImage(file="Assets/SignInSButton.png")
        self.SButton_Pressed = tk.PhotoImage(file="Assets/SignInSButton_Pressed.png")
        self.TitleImg = tk.PhotoImage(file="Assets/SignInTitle.png")
        self.AsideTitleImg = tk.PhotoImage(file="Assets/SignInAside_Title.png")

        # Imagem de fundo
        self.Bg = tk.Canvas(master=self.janela, width=700, height=600, borderwidth=0,
                            highlightthickness=0)
        self.Bg.pack()
        self.Bg.create_image(350, 300, anchor=tk.CENTER, image=self.backImage)

        # LeftSide
        self.Title = self.Bg.create_image(60, 127, anchor=tk.NW, image=self.AsideTitleImg)
        self.LoginButton = self.Bg.create_image(100, 189,
                                                anchor=tk.NW,
                                                image=self.SButton)
        self.Bg.tag_bind(self.LoginButton,
                         "<ButtonPress-1>",
                         lambda _: self.LoginButton_press())
        self.Bg.tag_bind(self.LoginButton,
                         "<ButtonRelease-1>",
                         lambda _: self.LoginButton_release())

        # RightSide
        self.SideFrame = tk.Frame(master=self.Bg, width=400, height=600, bg="#3A4570")
        self.SideFrame.place(x=300, y=0)
        self.SideTitle = tk.Label(master=self.SideFrame,
                                  image=self.TitleImg,
                                  borderwidth=0)
        self.SideTitle.place(x=75, y=22)

        # Inputs
        self.EntryUserBack = tk.Label(master=self.SideFrame,
                                      image=self.EntryImg1,
                                      borderwidth=0)
        self.EntryUserBack.place(x=25, y=128)
        self.EntryUser = tk.Entry(master=self.SideFrame,
                                  width=40,
                                  borderwidth=0,
                                  fg="grey",
                                  font="Inter 10")
        self.EntryUser.place(x=75, y=140)
        self.EntryUser.placeholder = "Nome de usuário"
        self.EntryUser.insert(0, "Nome de usuário")
        self.EntryUser.bind("<FocusIn>",
                            lambda event, entry=self.EntryUser:
                            self.on_focus_in(entry))
        self.EntryUser.bind("<FocusOut>",
                            lambda event, entry=self.EntryUser:
                            self.on_focus_out(entry))
        self.EntryUser.Label = tk.Label(master=self.SideFrame,
                                        text="",
                                        foreground="#ff0000",
                                        bg="#3A4570",
                                        font="Inter 8")
        self.EntryUser.Label.place(x=50, y=174)

        self.EntryEmailBack = tk.Label(master=self.SideFrame,
                                       image=self.EntryImg3,
                                       borderwidth=0)
        self.EntryEmailBack.place(x=25, y=203)
        self.EntryEmail = tk.Entry(master=self.SideFrame,
                                   width=40,
                                   borderwidth=0,
                                   fg="grey",
                                   font="Inter 10")
        self.EntryEmail.place(x=75, y=215)
        self.EntryEmail.placeholder = "Email"
        self.EntryEmail.insert(0, "Email")
        self.EntryEmail.bind("<FocusIn>",
                             lambda event, entry=self.EntryEmail:
                             self.on_focus_in(entry))
        self.EntryEmail.bind("<FocusOut>",
                             lambda event, entry=self.EntryEmail:
                             self.on_focus_out(entry))
        self.EntryEmail.Label = tk.Label(master=self.SideFrame,
                                         text="",
                                         foreground="#ff0000",
                                         bg="#3A4570",
                                         font="Inter 8")
        self.EntryEmail.Label.place(x=50, y=249)
        self.EntryPassBack = tk.Label(master=self.SideFrame,
                                      image=self.EntryImg2,
                                      borderwidth=0)
        self.EntryPassBack.place(x=25, y=278)
        self.EntryPass = tk.Entry(master=self.SideFrame,
                                  width=40,
                                  borderwidth=0,
                                  fg="grey",
                                  font="Inter 10")
        self.EntryPass.place(x=75, y=289)
        self.EntryPass.placeholder = "Senha"
        self.EntryPass.insert(0, "Senha")
        self.EntryPass.bind("<FocusIn>",
                            lambda event, entry=self.EntryPass:
                            self.on_focus_in(entry))
        self.EntryPass.bind("<FocusOut>",
                            lambda event, entry=self.EntryPass:
                            self.on_focus_out(entry))
        self.EntryPass.Label = tk.Label(master=self.SideFrame,
                                        text="",
                                        foreground="#ff0000",
                                        bg="#3A4570",
                                        font="Inter 8")
        self.EntryPass.Label.place(x=50, y=323)
        self.EntryPassRBack = tk.Label(master=self.SideFrame,
                                       image=self.EntryImg2,
                                       borderwidth=0)
        self.EntryPassRBack.place(x=25, y=353)
        self.EntryPassR = tk.Entry(master=self.SideFrame,
                                   width=40,
                                   borderwidth=0,
                                   fg="grey",
                                   font="Inter 10")
        self.EntryPassR.place(x=75, y=364)
        self.EntryPassR.placeholder = "Repita a senha"
        self.EntryPassR.insert(0, "Repita a senha")
        self.EntryPassR.bind("<FocusIn>",
                             lambda event, entry=self.EntryPassR:
                             self.on_focus_in(entry))
        self.EntryPassR.bind("<FocusOut>",
                             lambda event, entry=self.EntryPassR:
                             self.on_focus_out(entry))
        self.EntryPassR.Label = tk.Label(master=self.SideFrame,
                                         text="",
                                         foreground="#ff0000",
                                         bg="#3A4570",
                                         font="Inter 8")
        self.EntryPassR.Label.place(x=50, y=398)

        self.SignInButton = tk.Button(self.SideFrame,
                                      image=self.FButton,
                                      borderwidth=0,
                                      highlightthickness=0)
        self.SignInButton.place(x=150, y=459)
        self.SignInButton.bind("<Button-1>", self.white_entry)
        self.SignInButton.bind("<ButtonPress-1>", lambda event, button=self.SignInButton:
        self._on_pressed(button), add=True)
        self.SignInButton.bind("<ButtonRelease-1>", lambda event, button=self.SignInButton:
        self._on_release(button), add=True)

        self.janela.mainloop()

    def on_focus_in(self, entry):
        if entry.get() == entry.placeholder:
            entry["show"] = "*" if "senha" in entry.placeholder.lower() else ""
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(self, entry):
        if entry.get() == "":
            entry["show"] = "" if "senha" in entry.placeholder.lower() else ""
            entry.insert(0, entry.placeholder)
            entry.config(fg="grey")

    def _on_pressed(self, button):
        button.config(image=self.FButton_Pressed)
        return "break"

    def _on_release(self, button):
        button.config(image=self.FButton)
        return "break"

    def LoginButton_press(self):
        self.Bg.itemconfig(self.LoginButton, image=self.SButton_Pressed)

    def LoginButton_release(self):
        self.Bg.itemconfig(self.LoginButton, image=self.SButton)
        self.janela.destroy()
        swap("Login")

    def white_entry(self, event):
        args = {"User": self.EntryUser,
                "Email": self.EntryEmail,
                "Pass": self.EntryPass,
                "PassR": self.EntryPassR}
        for index, entry in args.items():
            if index == "User":
                pass
            elif entry.get() == "" or entry.get() == " ":
                entry.Label['text'] = "*Não pode estar vazio"
                break
            elif entry.get() == entry.placeholder:
                entry.Label['text'] = "*Não pode estar vazio"
                break
        else:
            self.check_entry(args)
            return "break"

    def check_entry(self, args):
        for index, entry in args.items():
            entry.Label['text'] = ""
            if index == "UserEmail":
                # Lógica Ou Ou em python
                if ((self.check_name(entry) or not self.check_email(entry)) and
                        (not self.check_name(entry) or self.check_email(entry))):
                    break
            elif index == "User":
                if not self.check_name(entry):
                    break
            elif index == "Email":
                if not self.check_email(entry):
                    break
            elif index == "Pass":
                if not self.check_pass(entry):
                    break
            elif index == "RPass":
                if args['RPass'].get() != args['Pass'].get():
                    entry.Label['text'] = "*Senhas não coincidem"
                    break
        else:
            self.print_to_database(args['User'].get(), args['Email'].get(), args['Pass'].get())
            self.janela.destroy()
            swap("login")

    def check_name(self, entry):
        name = entry.get().strip()
        if " " in name:
            entry.Label['text'] = "*Nome não pode conter espaços em branco"
            return False
        elif name == "":
            return True
        elif len(name) > 150:
            entry.Label['text'] = "*Nome de usuário muito grande, MAX: 150"
            return False
        else:
            for i in name:
                if i in ascii_letters or i.isdigit() or i == "_":
                    pass
                else:
                    entry.Label['text'] = "*Nome de usuário inválido"
                    return False
        return True

    def check_email(self, entry):
        email = entry.get().strip()
        adress = email.lower().find("@gmail.com")
        if adress == -1:
            entry.Label['text'] = "*Email deve conter @gmail.com"
            return False
        elif len(email) > 150:
            entry.Label['text'] = "*Email muito grande, MAX: 150"
            return False
        elif self.check_database(email):
            entry.Label['text'] = "*Email já cadastrado"
            return False
        else:
            for i in email[:adress]:
                if i.isalpha() or i.isdigit or i == ".":
                    pass
                else:
                    entry.Label['text'] = "*Email inválido"
                    return False
        return True

    def check_pass(self, entry):
        password = entry.get().strip()
        digits = False
        alpha = False
        symbols = False
        if " " in password:
            entry.Label['text'] = "*Senha não pode conter espaços"
            return False
        elif len(password) < 8:
            entry.Label['text'] = "*Senha deve conter 8 caracteres, simbólos, letras e números"
            return False
        elif len(password) > 150:
            entry.Label['text'] = "*Senha muito grande, MAX: 150"
            return False
        for i in password:
            if i.isdigit():
                digits = True
            elif i.isalpha():
                alpha = True
            elif i in "!@#$%¨&*_-+*/.,;:|\\":
                symbols = True
            else:
                entry.Label['text'] = "*Caractere não reconhecido"
                return False
        if not (digits and alpha and symbols):
            entry.Label['text'] = "*Senha deve conter 8 caracteres, simbólos, letras e números"
            return False
        return True

    def check_database(self, for_check, what_check='email'):
        for_check = for_check.lower() if what_check == "email" else for_check
        con = connect("data.db")
        exe = con.cursor()
        select = exe.execute("select * from users where ¨ = ?".replace("¨", what_check), (for_check,))
        if select.fetchall():
            return True
        return False

    def print_to_database(self, name, email, password):
        con = connect("data.db")
        exe = con.cursor()
        exe.execute("insert into users (name, email, password) values (?, ?, ?)",
                    (name, email.lower(), password))
        con.commit()
        con.close()


if __name__ == "__main__":
    app = Login()
