from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class text_editor:

    current_open_file = "no_file"

    def new_file(self,event=""):
        self.text_area.delete(1.0,END)
        self.current_open_file="no_file"

    def open_file(self,event=""):
        open_return=filedialog.askopenfile(initialdir="/d",title="select file to open",filetypes=(("text files","*.txt"),("Python file","*.py"),("All files","*.*")))
        if(open_return != None):
            self.text_area.delete(1.0,END)
            for line in open_return:
                self.text_area.insert(END,line)
        self.current_open_file=open_return.name
        open_return.close()


    def save(self,event=""):
        if self.current_open_file=="no_file":
            self.save_as()
        else:
            f=open(self.current_open_file,mode="w+")
            f.write(self.text_area.get(1.0,END))
            f.close()


    def save_as(self,event=""):
        f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        text2save=self.text_area.get(1.0,END)
        self.current_open_file=f.name
        f.write(text2save)
        f.close()

    def copy_text(self,event=""):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_text(self,event=""):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")


    def paste_text(self, event=""):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())


    def about(self):
        messagebox.showinfo("About","Text Editor Version 10.1702.312.0 © 2019 Owner Corporation. All rights reserved.\n\nBy Watson Biard")

    def __init__(self,master):
        self.master=master
        master.title("Text editor")
        self.text_area=Text(self.master,undo=True)
        self.text_area.bind('<Control-c>', self.copy_text)
        self.text_area.bind('<Control-v>', self.paste_text)
        self.text_area.bind('<Control-x>', self.cut_text)
        self.text_area.bind('<Control-z>', self.text_area.edit_undo)
        self.text_area.bind('<Control-y>', self.text_area.edit_redo)
        self.text_area.bind('<Control-n>', self.new_file)
        self.text_area.bind('<Control-o>', self.open_file)
        self.text_area.bind('<Control-s>', self.save)
       



        self.text_area.pack(fill=BOTH,expand=1)
        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)



        #creating file menu
        self.file_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)

        self.file_menu.add_command(label="New file      Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="Open      Ctrl+O",command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save      Ctrl+S", command=self.save)
        self.file_menu.add_command(label="Save As       Ctrl+N", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.master.quit)


        #created edit menu
        self.edit_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu)

        self.edit_menu.add_command(label="Copy      Ctrl+c",command=self.copy_text)
        self.edit_menu.add_command(label="Cut       Ctrl+x", command=self.cut_text)
        self.edit_menu.add_command(label="Paste     Ctrl+v", command=self.paste_text)
        self.edit_menu.add_command(label="Undo      Ctrl+z", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo      Ctrl+y", command=self.text_area.edit_redo)


        # created help menu
        self.help_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)

        self.help_menu.add_command(label="About", command=self.about)

# createing root window
root=Tk()


te=text_editor(root)





# create main loop for looping through
root.mainloop()



