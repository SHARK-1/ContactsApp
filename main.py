from App import *

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.pack(expand=tk.YES, fill=tk.BOTH)
    root.title('ConatctsApp')
    root.geometry('780x420+500+200')
    root.resizable(False, False)
    # root.iconbitmap('Images/Icon.ico')
    root.mainloop()
    print('123')
