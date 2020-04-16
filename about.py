from tkinter import *


class About:
    def __init__(self,root):
        self.root = root

        frame=Frame(root,bg='#ffa500',width=550,height=550)
        frame.pack(fill=BOTH)
        text=Label(frame,text='This is our about us page you find more'
                              '\ninformation about us here'
                              '\nthis application was created for educational purposes'
                              '\nand we have learned a lot :)',
                   font='ariall 14 bold',bg='#ffa500',fg='white')

        text.place(x=50,y=50)

def main():
    root = Tk()
    app = About(root)
    root.title("About us")
    root.geometry("550x550+550+200")
    root.resizable(False,False)
    root.mainloop()
if __name__ == '__main__':
    main()