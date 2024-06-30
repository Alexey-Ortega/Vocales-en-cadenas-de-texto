import tkinter as tk
from tkinter import messagebox

# Inicio de variable
def contar_vocales():
    texto = entrada.get()
    vocales = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vocales:
            contador += 1
    messagebox.showinfo("Resultado", f"El número de vocales en el texto es: {contador}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contador de Vocales")

# Crear y colocar los widgets
etiqueta = tk.Label(ventana, text="Introduce una cadena de texto:")
etiqueta.pack(padx=10, pady=10)

entrada = tk.Entry(ventana, width=50)
entrada.pack(padx=10, pady=10)

boton = tk.Button(ventana, text="Contar Vocales", command=contar_vocales)
boton.pack(padx=10, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
