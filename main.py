import requests
import validators
from tkinter import *

curr_mode = 0
curr_number = 0
curr_time = 0
curr_link = ''
counter = 0

def OLXreq():
    global curr_mode, counter, curr_number, curr_time, curr_link
    if curr_mode == 1 and counter < curr_number:
        counter += 1
        le.config(text=("      Added: " + str(counter)))
        requests.get(curr_link)
        print("+1")
        root.after(curr_time, OLXreq)
    elif counter == curr_number:
        setMode()
        le.config(text="           End!")
    return

def setMode():
    global curr_mode, counter, curr_number, curr_time, curr_link
    if curr_mode == 0:
        print("Break time (sec):", time.get(), "Number of views:", number.get())

        #Empty field
        if number.get() == '' or time.get() == '' or link.get() == '':
            le.config(text="Please complete\nall fields!")
            return

        #Bad data format
        try:
            curr_number = int(number.get())
            curr_time = int(time.get() + '000')
        except:
            le.config(text="Error!\nBad data format!")
            return

        #Time less than 0
        if int(time.get()) < 0:
            le.config(text="Error!\nTime cannot be\nless than 0!")
            return

        # Time less than 0
        if int(number.get()) < 1:
            le.config(text="Error!\nNumber cannot\nbe less than 1!")
            return

        curr_link = link.get()

        #Link format
        if not validators.url(curr_link):
            le.config(text="      Error!\n      Bad link!")
            return

        curr_mode = 1
        bt1['text'] = 'Stop'
        print('Start')
    else:
        curr_mode = 0
        counter = 0
        bt1['text'] = 'Start'
        print('Stop')
    OLXreq()

root = Tk()
root.geometry("315x190")
root.title("Visits adder")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

number = StringVar()
Label(root, text="Number of views:").place(x = 10, y = 10)
Entry(root, width=15, textvariable=number).place(x = 115, y = 12)

time = StringVar()
Label(root, text="Break time (sec):").place(x = 10, y = 40)
Entry(root, width=15, textvariable=time).place(x = 115, y = 42)

link = StringVar()
Label(root, text="Link:").place(x = 10, y = 70)
Entry(root, width=40, textvariable=link).place(x = 55, y = 72)

le = Label(root, text="")
le.place(x = 110, y = 105)

bt1 = Button(root, text="Start", command=setMode)
bt1.place(x = 240, y = 23)

Label(root, text="https://github.com/ShocK1999").place(x = 142, y = 167)

root.mainloop()