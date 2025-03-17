import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora")
        self.window.geometry("300x400")
        self.dark_mode = True
        
        # Configurar grid weights para hacer la interfaz adaptable
        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
        
        # Pantalla de resultados
        self.display = tk.Entry(self.window, width=25, font=('Arial', 18), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        
        # Botones
        buttons = [
            ('7', 'num'), ('8', 'num'), ('9', 'num'), ('/', 'op'),
            ('4', 'num'), ('5', 'num'), ('6', 'num'), ('*', 'op'),
            ('1', 'num'), ('2', 'num'), ('3', 'num'), ('-', 'op'),
            ('0', 'num'), ('.', 'num'), ('=', 'op'), ('+', 'op')
        ]
        
        # Crear y posicionar botones
        row = 1
        col = 0
        for (button, tipo) in buttons:
            cmd = lambda x=button: self.click(x)
            btn = tk.Button(self.window, text=button, command=cmd)
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            btn.tipo = tipo  # Guardar el tipo de botón para el tema
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Botón de limpiar
        clear_btn = tk.Button(self.window, text='C', command=self.clear)
        clear_btn.grid(row=5, column=0, padx=2, pady=2, sticky='nsew')
        clear_btn.tipo = 'op'
        
        # Botón de modo oscuro/claro
        self.theme_button = tk.Button(self.window, text='Modo Claro', command=self.toggle_theme)
        self.theme_button.grid(row=5, column=1, columnspan=2, padx=2, pady=2, sticky='nsew')
        self.theme_button.tipo = 'theme'
        
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
            num_bg = '#4a4a4a'
            op_bg = '#ff9500'
            fg_color = 'white'
            op_fg = 'black'  # Color del texto para operaciones en modo oscuro
            self.theme_button.config(text='Modo Claro')
        else:
            bg_color = '#f0f0f0'
            num_bg = '#ffffff'
            op_bg = '#ff9500'
            fg_color = 'black'
            op_fg = 'white'  # Color del texto para operaciones en modo claro
            self.theme_button.config(text='Modo Oscuro')
            
        self.window.configure(bg=bg_color)
        self.display.configure(bg=bg_color, fg=fg_color)
        
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Button):
                if hasattr(widget, 'tipo'):
                    if widget.tipo == 'num':
                        widget.configure(bg=num_bg, fg=fg_color)
                    elif widget.tipo == 'op':
                        widget.configure(bg=op_bg, fg=op_fg)  # Usar el color de texto específico para operaciones
                    else:  # theme button
                        widget.configure(bg=bg_color, fg=fg_color)

if __name__ == '__main__':
    Calculator()
