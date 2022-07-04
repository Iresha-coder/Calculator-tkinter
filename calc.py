from tkinter import *
from tkinter import messagebox


class MainWindow:

    def __init__(self, theme):
        root = Tk()
        root.title("Calculator")

        self.theme = theme

        global var
        global f_num
        global s_num

        if theme == "default":
            pass

        self.frame_1 = LabelFrame(root, bd=0, bg="white")
        self.frame_2 = LabelFrame(root, bd=0, bg="white")
        self.frame_3 = LabelFrame(root, bd=0, bg="white")
        self.button_frame = LabelFrame(root, bd=0)

        self.inp = Entry(root, bd=0, bg="white", font=("Segoe UI Bold", 18))

        theme_light = Button(self.frame_2, text="Light",
                             command=self.light_theme, font=("Segoe UI Bold", 12))
        theme_light.grid(row=0, column=0)
        theme_dark = Button(self.frame_2, text="Dark",
                            command=self.dark_theme, font=("Segoe UI Bold", 12))
        theme_dark.grid(row=0, column=1)

        self.button_1 = Button(self.frame_2, text="1", padx=40, pady=20, command=lambda: self.button_click(
            1), bg="white", bd=1, font=("Segoe UI Bold", 16))
        self.button_2 = Button(self.frame_2, text="2", padx=40, pady=20, command=lambda: self.button_click(
            2), bg="white", bd=1, font=("Segoe UI Bold", 16))
        self.button_3 = Button(self.frame_2, text="3", padx=40, pady=20, command=lambda: self.button_click(
            3), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_4 = Button(self.frame_2, text="4", padx=40, pady=20, command=lambda: self.button_click(
            4), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_5 = Button(self.frame_2, text="5", padx=40, pady=20, command=lambda: self.button_click(
            5), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_6 = Button(self.frame_2, text="6", padx=40, pady=20, command=lambda: self.button_click(
            6), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_7 = Button(self.frame_2, text="7", padx=40, pady=20, command=lambda: self.button_click(
            7), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_8 = Button(self.frame_2, text="8", padx=40, pady=20, command=lambda: self.button_click(
            8), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_9 = Button(self.frame_2, text="9", padx=40, pady=20, command=lambda: self.button_click(
            9), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_0 = Button(self.frame_2, text="0", padx=40, pady=20, command=lambda: self.button_click(
            0), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_cl = Button(self.frame_2, text="Clear", padx=79, pady=20,
                                command=self.button_clear, bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_a = Button(self.frame_2, text="+", padx=40, pady=20,
                               command=self.button_add, bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_s = Button(self.frame_2, text="-", padx=40, pady=20,
                               command=self.button_sub, bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_m = Button(self.frame_2, text="*", padx=40, pady=20,
                               command=self.button_mul, bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_d = Button(self.frame_2, text="/", padx=40, pady=20,
                               command=self.button_div, bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_e = Button(self.frame_2, text="=", padx=91, pady=20,
                               command=lambda: self.button_equal(int(self.inp.get())), bg="white", bd=1, font=("Segoe UI Bold", 12))
        self.button_dot = Button(self.frame_2, text=".", padx=40, pady=20, command=lambda: self.button_click(
            "."), bg="white", bd=1, font=("Segoe UI Bold", 12))

        self.inp.pack(ipadx=5, ipady=5)

        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_0.grid(row=4, column=0)
        self.button_cl.grid(row=4, column=1, columnspan=2)
        self.button_a.grid(row=5, column=0)
        self.button_e.grid(row=5, column=1, columnspan=2)
        self.button_s.grid(row=6, column=0)
        self.button_m.grid(row=6, column=1)
        self.button_d.grid(row=6, column=2)
        self.button_dot.grid(row=7, column=1)

        self.frame_2.pack()
        self.frame_1.pack()
        self.frame_3.pack()
        self.button_frame.pack()

        root.mainloop()

    def button_click(self, number):
        current = self.inp.get()
        self.inp.delete(0, END)
        self.inp.insert(0, str(current) + str(number))

    # def button_add(self):
    #     self.var = 1
    #     first_number = self.inp.get()
    #     try:
    #         self.f_num = int(first_number)
    #     except ValueError:
    #         if self.f_num == "":
    #             messagebox.showerror("Error", "Cannot Add Empty Input")
    #         self.f_num = float(first_number)
    #     self.label_1 = Label(
    #         self.frame_1, text="{0} +".format(first_number), anchor=E, bg="white")
    #     self.label_1.grid(row=0, column=0, sticky=W+E)
    #     self.inp.delete(0, END)

    # def button_sub(self, number):
    #     self.var = 2
    #     self.first_number = self.inp.get()
    #     try:
    #         self.f_num = int(self.first_number)
    #     except ValueError:
    #         if self.f_num == "":
    #             messagebox.showerror("Error", "Cannot Add Empty Input")
    #         self.f_num = float(self.first_number)
    #     self.label_1 = Label(
    #         self.frame_1, text="{0} -".format(self.first_number), anchor=E, bg="white")
    #     self.label_1.grid(row=0, column=0, sticky=W+E)
    #     self.inp.delete(0, END)

    # def button_mul(self, number):
    #     var = 3
    #     first_number = self.inp.get()
    #     try:
    #         self.f_num = int(first_number)
    #     except ValueError:
    #         if self.f_num == "":
    #             messagebox.showerror("Error", "Cannot Add Empty Input")
    #         self.f_num = float(first_number)
    #     self.label_1 = Label(
    #         self.frame_1, text="{0} *".format(first_number), anchor=E, bg="white")
    #     self.label_1.grid(row=0, column=0, sticky=W+E)
    #     self.inp.delete(0, END)

    # def button_div(self, number):
    #     var = 4
    #     first_number = self.inp.get()
    #     try:
    #         self.f_num = int(first_number)
    #     except ValueError:
    #         if self.f_num == "":
    #             messagebox.showerror("Error", "Cannot Add Empty Input")
    #         f_num = float(first_number)
    #     self.label_1 = Label(
    #         self.frame_1, text="{0} /".format(first_number), anchor=E, bg="white")
    #     self.label_1.grid(row=0, column=0, sticky=W+E)
    #     self.inp.delete(0, END)

    def button_equal(self, number):
        global s_num
        self.second_number = self.inp.get()
        try:
            s_num = int(self.second_number)
        except ValueError:
            if self.second_number == "":
                messagebox.showerror(
                    "Error", "Cannot solve sum, due to no second number")
            elif self.second_number == " ":
                messagebox.showerror("Error", "Cannot add space")
            self.inp.delete(0, END)
            self.label_1 = Label(self.frame_1, text="", anchor=E, bg="white")
            self.label_1.grid(row=0, column=0, sticky=W+E)
        self.s_num = float(self.second_number)
        self.inp.delete(0, END)
        if self.var == 1:
            self.inp.insert(0, self.f_num + s_num)
            self.label_1 = Label(
                self.frame_1, text="{0} + {1}".format(str(self.f_num), str(s_num)), anchor=E, bg="white")
            self.label_1.grid(row=0, column=0, sticky=W+E)
        elif self.var == 2:
            self.inp.insert(0, self.f_num - s_num)
            self.label_1 = Label(
                self.frame_1, text="{0} - {1}".format(str(self.f_num), str(s_num)), anchor=E, bg="white")
            self.label_1.grid(row=0, column=0, sticky=W+E)
        elif self.var == 3:
            self.inp.insert(0, self.f_num * s_num)
            self.label_1 = Label(
                self.frame_1, text="{0} * {1}".format(str(self.f_num), str(s_num)), anchor=E, bg="white")
            self.label_1.grid(row=0, column=0, sticky=W+E)
        elif self.var == 4:
            try:
                self.inp.insert(0, self.f_num / s_num)
            except ZeroDivisionError:
                messagebox.showinfo("Division By Zero",
                                    "Cannot divide by zero")
                self.inp.delete(0, END)
                self.label_1 = Label(
                    self.frame_1, text="     ", anchor=E, bg="white")
                self.label_1.grid(row=0, column=0, sticky=W+E)
                
        self.label_1 = Label(
            self.frame_1, text="{0} / {1}".format(str(self.f_num), str(s_num)), anchor=E, bg="white")
        self.label_1.grid(row=0, column=0, sticky=W+E)

    def button_clear(self):
        self.inp.delete(0, END)
        self.label_1 = Label(self.frame_1, text="", anchor=E, bg="white")
        self.label_1.grid(row=0, column=0, sticky=W+E)

    def button_pos_neg(self, number):
        pass

    def light_theme(self):
        pass

    def dark_theme(self):
        pass


file = open("D:\\Python\\Projects\\Calculator\\Files\\theme.txt", "r+")

if file.read() == "white":
    app = MainWindow(theme="light")
elif file.read() == "dark":
    app = MainWindow(theme="dark")
else:
    app = MainWindow("default")
