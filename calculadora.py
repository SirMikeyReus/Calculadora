    import tkinter as tk

    class CalculatorApp:
        def __init__(self, master):
            self.master = master
            master.title("Calculadora")

            self.display = tk.Entry(master, font=('Arial', 20), justify='right')
            self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")
            
            buttons = [
                ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
                ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
                ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
                ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
                ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3)
            ]

            for (text, row, col) in buttons:
                button = tk.Button(master, text=text, font=('Arial', 15), command=lambda t=text: self.on_button_click(t))
                button.grid(row=row, column=col, sticky="nsew")

            master.grid_rowconfigure(5, weight=1)
            master.grid_columnconfigure(4, weight=1)

            # Configurar eventos de teclado
            master.bind('<Key>', self.on_key_press)
            master.bind('<Return>', lambda event: self.on_button_click('='))
            master.bind('<BackSpace>', lambda event: self.on_button_click('C'))

        def on_button_click(self, value):
            if value == '=':
                try:
                    result = eval(self.display.get())
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                except:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Error")
            elif value == 'C':
                self.display.delete(0, tk.END)
            else:
                self.display.insert(tk.END, value)

        def on_key_press(self, event):
            key = event.char
            if key.isdigit() or key in ['+', '-', '*', '/', '(', ')', '.', '^']:
                self.on_button_click(key)
            elif key == '\r':
                self.on_button_click('=')
            elif key == '\x08':
                self.on_button_click('C')

    def main():
        root = tk.Tk()
        app = CalculatorApp(root)
        root.mainloop()

    if __name__ == "__main__":
        main()