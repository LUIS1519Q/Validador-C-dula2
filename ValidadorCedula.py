from flask import Flask, render_template, request

app = Flask(__name__)

def validar_cedula(cedula):
    if not cedula.isdigit() or len(cedula) != 10:
        return "La cédula debe tener 10 dígitos numéricos."
    
    dig = [int(d) for d in cedula]
    provincia = int(cedula[:2])
    
    if provincia < 1 or provincia > 24:
        return "Código de provincia inválido."
    
    if dig[2] >= 6:
        return "Tercer dígito inválido para persona natural."
    
    coef = [2,1,2,1,2,1,2,1,2]
    suma = 0
    
    for d, c in zip(dig[:9], coef):
        mult = d * c
        if mult >= 10:
            mult -= 9
        suma += mult
    
    resto = suma % 10
    verificador = 0 if resto == 0 else 10 - resto
    
    if verificador == dig[9]:
        return "Cédula válida."
    else:
        return f"Cédula inválida. El dígito verificador debe ser {verificador}."

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    if request.method == "POST":
        cedula = request.form["cedula"]
        resultado = validar_cedula(cedula)
        
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
