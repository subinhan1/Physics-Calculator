import tkinter as tk
from scipy import constants

class mainwindow(tk.Tk):
    """Main window with tkinter"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Setting title of window
        self.title(" Physics Constant Calculator")
        self.geometry("600x600")

        # Creating a frame called container
        container = tk.Frame(self, height=600, width=600)

        # Making sure container fits self perfectly
        container.pack(side="top", fill="both", expand=True)

        # Assigning location of container using grid
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # Making dictionary of frames
        self.frames = {}


        for F in (StartPage, Calculator):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using the method show_frame(defined below) to show the StartPage
        self.show_frame(StartPage)


    def show_frame(self, frame_name):
        frame = self.frames[frame_name]

        # This raises the current frame to the top
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, 
            text="Physics Constant Calculator",
            font=("default", 24))
        label.pack(side="top", expand=True)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Start",
            font=("default", 24),
            command=lambda: controller.show_frame(Calculator),
        )
        switch_window_button.pack(side="bottom", expand=True)
        switch_window_button.focus_set()

        # Switches frames when space is entered
        switch_window_button.bind('<space>', lambda: controller.show_frame(Calculator))


class Calculator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Setting up grid to have weight so that it expands along with the frame
        for x in range(5):
            self.rowconfigure(x, weight=1)
        for y in range(8):
            self.columnconfigure(y, weight=1)

        # Initialize variables
        self.expression = ""
        self.memory = tk.StringVar()
        self.equation = tk.StringVar()

        # self.equation is being shown on the entry
        expression_field = tk.Entry(self, textvariable = self.equation)
        expression_field.grid(columnspan=4, sticky="nesw")

        # Updates self.equation on screen when numbers are pressed
        def press(num):
            self.expression += str(num)
            self.equation.set(self.expression)

        # Evaluates the expression and updates screen with results
        def equal_press():
            try:
                total=str(eval(self.expression))
                self.equation.set(total)

                self.expression = ""

            except:
                self.equation.set(" error ")
                self.expression = ""

        # Stores current values on screen to memory
        def memory_store():
            self.memory.set(self.equation.get())

        # Prints current stored value to screen
        def memory_callback():
            self.expression += str(self.memory.get())
            self.equation.set(self.expression)

        def scientific_not():
            self.equation.set("{:e}".format(float(str(self.equation.get()))))

        # Resets memory 
        def memory_clear():
            self.memory.set("")

        # Resets entire screen
        def clear():
            self.expression = ""
            self.equation.set("")

        #Buttons(0~9, / * - + . enter clear ms mc mcl)
        button1 = tk.Button(self, text=" 1 ", command=lambda:press(1), height=1, width=7)
        button1.grid(row=3, column=0, sticky="nesw")

        button2 = tk.Button(self, text=" 2 ", command=lambda:press(2), height=1, width=7)
        button2.grid(row=3, column=1, sticky="nesw")

        button3 = tk.Button(self, text=" 3 ", command=lambda:press(3), height=1, width=7)
        button3.grid(row=3, column=2, sticky="nesw")

        button4 = tk.Button(self, text=" 4 ", command=lambda:press(4), height=1, width=7)
        button4.grid(row=2, column=0, sticky="nesw")

        button5 = tk.Button(self, text=" 5 ", command=lambda:press(5), height=1, width=7)
        button5.grid(row=2, column=1, sticky="nesw")

        button6 = tk.Button(self, text=" 6 ", command=lambda:press(6), height=1, width=7)
        button6.grid(row=2, column=2, sticky="nesw")

        button7 = tk.Button(self, text=" 7 ", command=lambda:press(7), height=1, width=7)
        button7.grid(row=1, column=0, sticky="nesw")

        button8 = tk.Button(self, text=" 8 ", command=lambda:press(8), height=1, width=7)
        button8.grid(row=1, column=1, sticky="nesw")

        button9 = tk.Button(self, text=" 9 ", command=lambda:press(9), height=1, width=7)
        button9.grid(row=1, column=2, sticky="nesw")

        button0 = tk.Button(self, text=" 0 ", command=lambda:press(0), height=1, width=7)
        button0.grid(row=4, column=0, sticky="nesw")

        plus = tk.Button(self, text=" + ", command=lambda:press("+"), height=1, width=4)
        plus.grid(row=5, column=3, sticky="nesw")

        minus = tk.Button(self, text=" - ", command=lambda:press("-"), height=1, width=4)
        minus.grid(row=4, column=3, sticky="nesw")

        multiply = tk.Button(self, text=" * ", command=lambda:press("*"), height=1, width=4)
        multiply.grid(row=3, column=3, sticky="nesw")

        divide = tk.Button(self, text=" / ", command=lambda:press("/"), height=1, width=4)
        divide.grid(row=2, column=3, sticky="nesw")

        enter = tk.Button(self, text=" Enter ", command=lambda:equal_press(), height=1, width=4)
        enter.grid(row=1, column=3, sticky="nesw")

        Clear = tk.Button(self, text=" Clear ", command=lambda:clear(), height=1, width=4)
        Clear.grid(row=6, column=3, sticky="nesw")

        decimal = tk.Button(self, text=" . ", command=lambda:press("."), height=1, width=7)
        decimal.grid(row=4, column=1, sticky="nesw")

        mem_store = tk.Button(self, text=" MS ", command=lambda:memory_store(), height=1, width=4)
        mem_store.grid(row=5, column=0, sticky="nesw")

        mem_callback = tk.Button(self, text= " MC ", command=lambda:memory_callback(), height=1, width=4)
        mem_callback.grid(row=5, column=1, sticky="nesw")

        mem_clear = tk.Button(self, text = " MCL ", command=lambda:memory_clear(), height=1, width=4)
        mem_clear.grid(row=5, column=2, sticky="nesw")

        to_Sci_Not = tk.Button(self, text = " SciNot ", command=lambda:scientific_not(), height=1, width=4)
        to_Sci_Not.grid(row=6, column=2, sticky="nesw")

        planck_const = tk.Button(self, text = " h ", command=lambda:press(constants.h), height=1, width=4)
        planck_const.grid(row=6, column=0, sticky="nesw")

        light_vel = tk.Button(self, text = " c ", command=lambda:press(constants.c), height=1, width=4)
        light_vel.grid(row=6, column=1, sticky="nesw")

        reduced_planck_const = tk.Button(self, text = "ℏ", command=lambda:press(constants.hbar), height=1, width=4)
        reduced_planck_const.grid(row=7, column=2, sticky="nesw")

        ten_micro = tk.Button(self, text = "10^-6", command=lambda:press(1e-6), height=1, width=4)
        ten_micro.grid(row=7, column=0, sticky="nesw")

        ten_nano = tk.Button(self, text = "10^-9", command=lambda:press(1e-9), height=1, width=4)
        ten_nano.grid(row=7, column=1, sticky="nesw")


# optional : need to make a frame switch from numbers to physics constants
# Fixing : 

# Need : Entry to display constants as symbols rather than numeric value





if __name__ == "__main__":
    calculator = mainwindow()
    calculator.mainloop()








