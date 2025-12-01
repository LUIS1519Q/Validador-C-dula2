import tkinter as tk
from tkinter import messagebox

def validar_cedula(cedula):
    # Lógica de validación (la misma que tenías)
    if not cedula.isdigit() or len(cedula) != 10:
        return "La cédula debe tener 10 dígitos numéricos."
    dig = [int(d) for d in cedula]
    provincia = int(cedula[:2])
    if provincia < 1 or provincia > 24:
        return "Código de provincia inválido."
    if dig[2] >= 6:
        return "Tercer dígito inválido para persona natural."
    coef = [2,1,2,1,2,1,2,1,2]
    
    # Cálculo con coeficientes y reducción
    suma = 0
    for d, c in zip(dig[:9], coef):
        mult = d * c
        if mult >= 10:
            mult = mult - 9 # O mult % 10 + 1 (excepto si es 9, que se vuelve 9)
        suma += mult
        
    resto = suma % 10
    verificador = 0 if resto == 0 else 10 - resto
    
    return "Cédula válida." if verificador == dig[9] else f"Cédula inválida. El dígito verificador debe ser {verificador}."


def validar_y_mostrar():
    cedula = entrada_texto.get()
    resultado = validar_cedula(cedula)
    
    # Mostrar el resultado usando una caja de mensaje
    if "válida" in resultado:
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showerror("Resultado", resultado)

# --- Configuración de la Interfaz Tkinter ---
raiz = tk.Tk()
raiz.title("Validador de Cédula Ecuador")
raiz.geometry("300x150") # Ajusta el tamaño de la ventana

# Etiqueta de instrucción
etiqueta = tk.Label(raiz, text="Ingrese la Cédula:")
etiqueta.pack(pady=10)

# Campo de entrada de texto
entrada_texto = tk.Entry(raiz, width=20)
entrada_texto.pack(pady=5)

# Botón de validación
boton_validar = tk.Button(raiz, text="Validar", command=validar_y_mostrar)
boton_validar.pack(pady=10)

# Iniciar el loop principal de la GUI
raiz.mainloop()