import tkinter as tk


def swap(c):
    try:
        app.janela.destroy()
        del (app)
    except:
        pass
    finally:
        if c.lower() == "login":
            app = Login()
        elif c.lower() == "signin":
            app = SignIn()


class Login:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Login")
        self.janela.geometry("700x600")
        self.fonte = tk.font.Font(family="Inter", size=18)
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
        self.SideFrame.place(x=298, y=-2)
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
        self.EntryUser.insert(0, "Nome de usuário ou email")
        self.EntryUser.bind("<FocusIn>",
                            lambda event, entry=self.EntryUser, ph="Nome de usuário ou email":
                            self.on_focus_in(entry, ph))
        self.EntryUser.bind("<FocusOut>",
                            lambda event, entry=self.EntryUser, ph="Nome de usuário ou email":
                            self.on_focus_out(entry, ph))

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
        self.EntryPass.insert(0, "Senha")
        self.EntryPass.bind("<FocusIn>",
                            lambda event, entry=self.EntryPass, ph="Senha":
                            self.on_focus_in(entry, ph))
        self.EntryPass.bind("<FocusOut>",
                            lambda event, entry=self.EntryPass, ph="Senha":
                            self.on_focus_in(entry, ph))

        self.LoginButton = tk.Button(self.SideFrame,
                                     image=self.FButton,
                                     borderwidth=0,
                                     highlightthickness=0)
        self.LoginButton.place(x=160, y=309)
        self.LoginButton.bind("<ButtonPress-1>", lambda event, button=self.LoginButton:
        self._on_pressed(button), add=True)
        self.LoginButton.bind("<ButtonRelease-1>", lambda event, button=self.LoginButton:
        self._on_release(button), add=True)

        self.janela.mainloop()

    def on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
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

class SignIn:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Login")
        self.janela.geometry("700x600")
        self.backImage = tk.PhotoImage(file="Assets/FundoLoginDesktop.png")

        # Imagem de fundo
        self.Label = tk.Label(master=self.janela, width=700, height=600, image=self.backImage)
        self.Label.pack()

        self.SideFrame = tk.Frame(master=self.Label, width=400, height=600, bg="#3A4570")
        self.SideFrame.place(x=298, y=-2)

        self.janela.mainloop()


if __name__ == "__main__":
    swap("Login")
