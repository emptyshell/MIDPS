#!/usr/bin/python

from CORE_module import *

master.title("calculator")

calc = Calculator()

b0 = Button(master, text="0", command=lambda: calc.numb_butt(0))
b1 = Button(master, text="1", command=lambda: calc.numb_butt(1))
b2 = Button(master, text="2", command=lambda: calc.numb_butt(2))
b3 = Button(master, text="3", command=lambda: calc.numb_butt(3))
b4 = Button(master, text="4", command=lambda: calc.numb_butt(4))
b5 = Button(master, text="5", command=lambda: calc.numb_butt(5))
b6 = Button(master, text="6", command=lambda: calc.numb_butt(6))
b7 = Button(master, text="7", command=lambda: calc.numb_butt(7))
b8 = Button(master, text="8", command=lambda: calc.numb_butt(8))
b9 = Button(master, text="9", command=lambda: calc.numb_butt(9))
b_dot = Button(master, text=".", command=lambda: calc.numb_butt("."))

plus = Button(master, text="+", command=lambda: calc.set_op(0))
minus = Button(master, text="-", command=lambda: calc.set_op(1))
times = Button(master, text="*", command=lambda: calc.set_op(2))
dives = Button(master, text="/", command=lambda: calc.set_op(3))
power = Button(master, text="^", command=lambda: calc.set_op(4))
root = Button(master, text=u"\u221A", command=lambda: calc.set_op(5))
plusminus = Button(master, text=u"\u00B1", command=lambda: calc.set_op(6))

equals = Button(master, text="=", command=calc.equate)
clear = Button(master, text="C", command=calc.clear)

#display.place(x=0 , y=2)
display.grid(row=0, column=0, columnspan=4)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b0.grid(row=4, column=1)
b_dot.grid(row=5, column=1)
clear.grid(row=5, column=2)
equals.grid(row=5, column=3)
plus.grid(row=1, column=3)
minus.grid(row=2, column=3)
times.grid(row=3, column=3)
dives.grid(row=4, column=3)
root.grid(row=4, column=0)
power.grid(row=5, column=0)
plusminus.grid(row=4, column=2)





master.mainloop()