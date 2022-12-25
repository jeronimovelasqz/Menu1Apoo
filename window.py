from tkinter import *

class Menu1Apoo:

    def __init__(self):
        self.window = Tk()

        self.window.geometry("1136x951")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 951,
            width = 1136,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"background.png")
        self.background = self.canvas.create_image(
            743.5, 515.5,
            image=self.background_img)

        self.img0 = PhotoImage(file = f"img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b0.place(
            x = 632, y = 500,
            width = 370,
            height = 51)

        self.img1 = PhotoImage(file = f"img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b1.place(
            x = 648, y = 579,
            width = 397,
            height = 48)

        self.img2 = PhotoImage(file = f"img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b2.place(
            x = 657, y = 649,
            width = 322,
            height = 48)

        self.window.resizable(False, False)
        self.window.mainloop()
    def btn_clicked(self):
        print("Button Clicked")


eso = Menu1Apoo()
