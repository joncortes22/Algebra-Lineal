from tkinter import *
def main():
    root = Tk()
    root.geometry("450x300")
    root.title("Smart Home")
    root.resizable(0,0)


    root.columnconfigure(0, weight=2)
    root.rowconfigure(0, weight=1)

    root.columnconfigure(4, weight=2)
    root.rowconfigure(5, weight=1)

    lbtitle = Label(root, text="MENÚ PRINCIPAL")
    lbtitle.grid(column=2, row=0, padx=4, pady=5)

    btnencrypt = Button(root, text ="ENCRIPTAR", height=1, width=12)
    btnencrypt.grid(column=1, row=1, padx=4, pady=5)

    btndeencrypt = Button(root, text ="DESENCRIPTAR", height=1, width=12)
    btndeencrypt.grid(column=3, row=1, padx=4, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()