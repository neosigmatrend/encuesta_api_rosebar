from flask import Flask, request
from dotenv import load_dotenv
import os
import yagmail

load_dotenv()
app = Flask(__name__)

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_DEST = os.getenv("EMAIL_DEST")

@app.route("/api/responder", methods=["POST"])
def responder():
    data = request.json
    nombre = data.get("nombre", "Sin nombre")
    area = data.get("area", "Sin área")
    ip = data.get("ip", "IP no disponible")

    cuerpo = f"""
📥 Nueva respuesta Rose Bar:

👤 Nombre: {nombre}
🏢 Área: {area}
🌐 IP real: {ip}
"""
    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)
        yag.send(to=EMAIL_DEST, subject="📨 Encuesta recibida", contents=cuerpo)
        return "OK"
    except Exception as e:
        print("❌ Error al enviar correo:", e)
        return "Error", 500

# 👇 AGREGA ESTO AL FINAL
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

