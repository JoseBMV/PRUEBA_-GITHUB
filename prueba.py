import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora")
        self.window.geometry("300x400")
        self.dark_mode = True
        
        # Pantalla de resultados
        self.display = tk.Entry(self.window, width=25, font=('Arial', 18), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Botones
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Crear y posicionar botones
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=5, height=2, command=cmd).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Botón de limpiar
        tk.Button(self.window, text='C', width=5, height=2, command=self.clear).grid(row=5, column=0)
        
        # Botón de modo oscuro/claro
        self.theme_button = tk.Button(self.window, text='Modo Claro', width=12, height=2, command=self.toggle_theme)
        self.theme_button.grid(row=5, column=1, columnspan=2)
        
        self.set_theme()
        self.window.mainloop()
    
    def click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, value)
    
    def clear(self):
        self.display.delete(0, tk.END)
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
    
    def set_theme(self):
        if self.dark_mode:
            bg_color = '#333333'
            fg_color = 'white'
            self.theme_button.config(text='Modo Claro')
        else:
            bg_color = 'white'
            fg_color = 'black'
            self.theme_button.config(text='Modo Oscuro')
            
        self.window.configure(bg=bg_color)
        self.display.configure(bg=bg_color, fg=fg_color)
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=bg_color, fg=fg_color)

if __name__ == '__main__':
    Calculator()
