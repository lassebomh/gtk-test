import tkinter as tk
from tkinter import ttk

def tkn(root, widget, *args, **kwargs):
	class limbo():
		def grid(self, column, row, *args, **kwargs):
			self.obj.grid(column=column, row=row, *args, **kwargs)
			return self.obj
		def pack(self, *args, **kwargs):
			self.obj.pack(*args, **kwargs)
			return self.obj

	lim = limbo()
	lim.obj = widget(root, *args, **kwargs)

	return lim

root = tk.Tk()

toolbar = tkn(root, ttk.Notebook).grid(0, 0)

tool0 = tkn(toolbar, ttk.Frame).grid(0, 0)
tool1 = tkn(toolbar, ttk.Frame).grid(0, 0)

toolbar.add(tool0, text='Objects')
toolbar.add(tool1, text='Map')

tk.mainloop()

# git testt