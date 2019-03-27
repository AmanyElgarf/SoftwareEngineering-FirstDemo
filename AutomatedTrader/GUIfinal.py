# WebsiteTest.py - prototyping a website with multiple windows/frames in Tkinter GUI
from tkinter import *
import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import ATController as at

AT = at.AutomatedTrader(0.0, {})


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # The container is where we'll stack a bunch of frames on top of each other.
        # The frame we want visible will be raised above the others
        container = tk.Frame(self)
        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Put all of the pages in the same location; the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    # Show a frame for the given page name
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.grid()
        button1 = tk.Button(self, text="Go to Account Info",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="GO AUTOTRADER Mode",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.grid()
        button2.grid()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        def show_balance():
            messagebox.showinfo("Balance", AT.print_balance())

        def withdraw():
            bal = entry_1.get()
            if float(bal) > AT.balance:
                messagebox.showinfo("Warning", "Attempted to withdraw more than available Balance, please try again")
            else:
                AT.balance -= float(bal)
                messagebox.showinfo("Success", "withdrew from AutoTrade Balance")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.iconPath = r"kash.PNG"
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_size = Label(self)
        self.icon_size.image = self.icon
        self.icon_size.configure(image=self.icon)
        self.icon_size.grid()

        label = tk.Label(self, text="Account Info", font=controller.title_font)
        label.grid()
        photo = tk.PhotoImage(file=r"kash.PNG")
        photo_label = tk.Label(self, image=photo)
        photo_label.grid(sticky="nsew")
        bal_label = Label(self, text="Withdraw Balance:")
        bal_label.grid()
        entry_1 = Entry(self)
        entry_1.grid()
        withdraw_button = tk.Button(self, text="Withdraw",
                                    command=lambda: withdraw())

        balance_button = tk.Button(self, text="Show Balance",
                                   command=lambda: show_balance())

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        withdraw_button.grid()
        balance_button.grid()
        button.grid()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        def run():
            print("AutoTrader has begun.")

        def stop():
            print("AutoTrader stopped.")
            print(AT.stock_portfolio.items())

        def get_Info():
            balance = entry_1.get()
            string_to_display = "Balance added is $" + balance
            AT.balance += float(balance)
            balance_label = Label(self)
            balance_label["text"] = string_to_display
            balance_label.grid()
            stock = entry_2.get()

            string_to_display = "AutoTrading for... " + stock
            time.sleep(1)
            string_to_display1 = "\nCollecting Sentiment..."
            time.sleep(1)
            string_to_display2 = "\nFetching Predictions..."

            stock_label = Label(self)
            stock_label["text"] = string_to_display1 + string_to_display2
            stock_label.grid()
            AT.search_stock_symbol(stock)
            stockprice = AT.get_stock_price(stock)
            AT.AutoTrade(520, stockprice, 362.2, stock)
            string_to_display3 = "Autotrader has run\n"

            string_to_display5 = stock + "'s price is $" + str(stockprice) + "\n"
            string_to_display4 = "New Balance is $" + str(AT.balance)
            run_label = Label(self)
            run_label["text"] = string_to_display3 + string_to_display5 + string_to_display4
            run_label.grid()
        def get_stock():
            stock = entry_2.get()
            string_to_display = "AutoTrading for... " + stock
            stock_label = Label(self)
            stock_label["text"] = string_to_display
            stock_label.grid()

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.iconPath = r"kash.PNG"
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_size = Label(self)
        self.icon_size.image = self.icon
        self.icon_size.configure(image=self.icon)
        self.icon_size.grid()

        AT_label = Label(self, text="Welcome! Please enter an initial deposit for your AutoTrader account balance.\n")
        AT_label.grid()
        Balance_label = Label(self, text="Add Balance:")
        Stock_label = Label(self, text="Initial Stock Ticker:")

        # formatting
        Balance_label.grid()
        entry_1 = Entry(self)
        entry_1.grid()

        Stock_label.grid()
        entry_2 = Entry(self)
        entry_2.grid()

        button1 = tk.Button(self, text="RUN",
                            command=lambda: get_Info())
        button2 = tk.Button(self, text="STOP",
                            command=lambda: stop())
        button3 = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))

        button1.grid()
        button2.grid()
        button3.grid()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
