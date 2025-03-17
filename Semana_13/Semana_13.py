import tkinter as tk
from tkinter import messagebox

def agregar_producto():
    producto = entrada.get()
    if producto:
        lista.insert(tk.END, producto)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_lista():
    lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Productos")
ventana.geometry("500x350")
ventana.config(bg="#f0f0f0")

# Marco principal
frame = tk.Frame(ventana, bg="#ffffff", padx=10, pady=10, relief=tk.RIDGE, bd=2)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Etiqueta
etiqueta = tk.Label(frame, text="Ingrese el nombre del producto:", bg="#ffffff", font=("Arial", 12))
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(frame, width=40, font=("Arial", 12))
entrada.pack(pady=5)

# Botones
botones_frame = tk.Frame(frame, bg="#ffffff")
botones_frame.pack(pady=5)

boton_agregar = tk.Button(botones_frame, text="Agregar Producto", command=agregar_producto, font=("Arial", 10))
boton_agregar.grid(row=0, column=0, padx=5)

boton_limpiar = tk.Button(botones_frame, text="Limpiar Lista", command=limpiar_lista, font=("Arial", 10))
boton_limpiar.grid(row=0, column=1, padx=5)

# Lista para mostrar productos
lista = tk.Listbox(frame, width=50, height=10, font=("Arial", 10))
lista.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
