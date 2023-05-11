from tkinter import *
import csv
import os.path
class GUI:
    def __init__(self, window):
        self.window = window
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Acc. Name')
        self.entry_name = Entry(self.frame_name)
        self.button_account = Button(self.frame_name, text='Enter', command=self.clicked2)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.button_account.pack(padx=5, side='right')
        self.frame_name.pack(anchor='w', pady=10)

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_total = Frame(self.window)
        self.label_total = Label(self.frame_total)
        self.label_total.pack(pady=10)
        self.frame_total.pack()
        self.frame_total.pack_forget()

    global y
    y = 0
    global x
    x = 0
    global total
    total = 0

    def action2(self):
        global y
        if y == 0:
            self.frame_action = Frame(self.window)
            self.label_name_action = Label(self.frame_action, text='Action')
            self.radio1 = IntVar()
            self.radio1.set(3)
            self.radio_deposit = Radiobutton(self.frame_action, text='Deposit', variable=self.radio1, value=1,
                                             command=self.action)
            self.radio_withdraw = Radiobutton(self.frame_action, text='Withdraw', variable=self.radio1, value=2,
                                              command=self.action)
            self.radio_deposit.pack(side='left')
            self.radio_withdraw.pack(side='left')
            self.frame_action.pack()
            y = 1

    def action(self):
        self.label_result.config(text='')
        action = self.radio1.get()
        if action == 1:
            self.deposit()
        elif action == 2:
            self.withdraw()

    def deposit(self):
        global x
        if x == 0:
            self.frame_amount = Frame(self.window)
            self.label_amount = Label(self.frame_amount, text='Deposit')
            self.entry_amount = Entry(self.frame_amount, width=20)
            self.label_amount.pack(padx=15, side='left')
            self.entry_amount.pack(padx=15, side='left')
            self.frame_amount.pack(anchor='w', pady=10)
            self.frame_bottom = Frame(self.window)
            self.button_save = Button(self.frame_bottom, text='Save', command=self.clicked)
            self.button_save.pack()
            self.frame_bottom.pack(pady=10)
            x = 1
        else:
            self.entry_amount.delete(0, END)
            self.label_amount.config(text='Deposit')
#
    def withdraw(self):
        global x
        if x == 0:
            self.frame_amount = Frame(self.window)
            self.label_amount = Label(self.frame_amount, text='Withdraw')
            self.entry_amount = Entry(self.frame_amount, width=20)
            self.label_amount.pack(padx=15, side='left')
            self.entry_amount.pack(padx=15, side='left')
            self.frame_amount.pack(anchor='w', pady=10)
            self.frame_bottom = Frame(self.window)
            self.button_save = Button(self.frame_bottom, text='Save', command=self.clicked)
            self.button_save.pack()
            self.frame_bottom.pack(pady=10)
            x = 1
        else:
            self.entry_amount.delete(0,END)
            self.label_amount.config(text='Withdraw')
#
    #
#
    def clicked2(self):
        global total
        try:
            name = self.entry_name.get()
            name2 = f'{name}' + '.csv'
            account = 'accounts\\' + name2
            if name == '':
                raise ZeroDivisionError
            else:
                if os.path.isfile(account):
                    self.button_account.pack_forget()
                    self.label_result.config(text='')
                    with open(account, 'r') as f:
                        reader = csv.reader(f)
                        for i in reader:
                            for j in i:
                                j = float(j)
                                total += j
                    self.frame_total.pack()
                    self.label_total.config(text=f'Current Balance = ${total:.2f}')
                    self.action2()
                else:
                    raise FileNotFoundError
        except ZeroDivisionError:
            self.label_result.config(text='Account Must be Named')
        except FileNotFoundError:
            self.label_result.config(text='Account not Found')
#
#
    def clicked(self):
        global x
        global y
        global total
        try:
            name = self.entry_name.get()
            name2 = f'{name}' + '.csv'
            account = 'accounts\\' + name2
            action = self.radio1.get()
            amount = float(self.entry_amount.get())
            if action == 1:
                money = amount
            elif action == 2:
                money = amount * -1
            else:
                raise IndentationError
            if amount <= 0:
                raise TypeError
            if action == 2 and total < amount:
                raise ZeroDivisionError
            with open(account, 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([money])
            self.entry_name.delete(0,END)
            self.entry_amount.delete(0,END)
            self.radio1.set(3)
            x = 0
            y = 0
            total = 0
            self.entry_name.focus()
            self.frame_action.pack_forget()
            self.frame_amount.pack_forget()
            self.frame_bottom.pack_forget()
            self.label_result.config(text='')
            self.label_total.config(text='')
            self.button_account.pack()
        except IndentationError:
            self.label_result.config(text='No Action Selected')
        except ValueError:
            self.label_result.config(text='Enter Numeric Values')
        except TypeError:
            self.label_result.config(text='Values Must be Positive')
        except ZeroDivisionError:
            self.label_result.config(text='Not Enough Funds')
            self.entry_amount.focus()
