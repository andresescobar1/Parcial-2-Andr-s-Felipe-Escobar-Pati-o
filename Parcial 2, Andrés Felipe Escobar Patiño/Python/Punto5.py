import tkinter as tk
from tkinter import messagebox

def verificar_division(num2):
    if num2 == 0:
        raise ZeroDivisionError("División por cero no permitida.")

def realizar_operacion(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = ""

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            verificar_division(num2)
            resultado = num1 / num2
        elif operacion == "potencia":
            resultado = num1 ** num2
            
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "División por cero no permitida.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Entradas para los números
entry_num1 = tk.Entry(root)
entry_num1.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Botones para las operaciones
btn_suma = tk.Button(root, text="Sumar", command=lambda: realizar_operacion("suma"))
btn_suma.pack()

btn_resta = tk.Button(root, text="Restar", command=lambda: realizar_operacion("resta"))
btn_resta.pack()

btn_multiplicacion = tk.Button(root, text="Multiplicar", command=lambda: realizar_operacion("multiplicacion"))
btn_multiplicacion.pack()

btn_division = tk.Button(root, text="Dividir", command=lambda: realizar_operacion("division"))
btn_division.pack()

btn_potencia = tk.Button(root, text="Potencia", command=lambda: realizar_operacion("potencia"))
btn_potencia.pack()

# Label para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()
