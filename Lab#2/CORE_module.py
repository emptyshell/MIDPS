#!/usr/bin/python

from Tkinter import *
from math import *

master = Tk()
display =  Entry(master, width=20, justify='right', bd=3, bg='lightgrey')

class Calculator:

	def __init__(self):
		self.var1 = ""
		self.var2 = ""
		self.result = 0
		self.current = 0
		self.operator = 0

	def numb_butt(self, index):
		if self.current is 0:
			self.var1= str(self.var1) + str(index)
			display.delete(0, END)
			display.insert(0, string=self.var1)
		else:
			self.var2 = str(self.var2) + str(index)
			display.delete(0, END)
			display.insert(0, string=self.var2)

	def equate(self):
		if self.operator is 0:
			self.var1 = float(self.var1) + float(self.var2)
			self.var2 = str("")
		elif self.operator is 1:
			self.var1 = float(self.var1) - float(self.var2)
			self.var2 = str("")
		elif self.operator is 2:
			self.var1 = float(self.var1) * float(self.var2)
			self.var2 = str("")
		elif self.operator is 3:
			self.var1 = float(self.var1) / float(self.var2)
			self.var2 = str("")
		elif self.operator is 4:
			try:
				self.var1 = pow(float(self.var1),float(self.var2))
			except OverflowError:
				self.var1 = str("inf")
			self.var2 = str("")
		elif self.operator is 5:
			try:
				self.var1 = pow(float(self.var1),0.5)
			except ValueError:
				self.var1 = str("error")
			self.var2 = str("")
		elif self.operator is 6:
			if float(self.var1)>0:
				tmp = "-" + str(self.var1)
				self.var1 = float(tmp)
			else:
				self.var1 = fabs(float(self.var1))
		if self.var1 is FloatType:	
			format(self.var1, '.15f')
		if self.var1 is FloatType:
			display.delete(0, END)
			display.insert(0, string=self.var1)
		else:
			display.delete(0, END)
			display.insert(0, string=self.var1)
			self.__init__()
		print(type(self.var1))

	def set_op(self, op):
		self.operator = op
		display.delete(0, END)
		if self.current is 0:
			self.current = 1
		else:
			self.equate()
			self.var2 = ""

	def clear(self):
		self.__init__()
		display.delete(0, END)
