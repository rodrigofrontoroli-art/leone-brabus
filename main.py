
from flask import Flask, request
import requests
import os

app = Flask(__name__)

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

def send_message(phone, message):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    payload = {
        "phone": phone,
        "message": message
    }
    requests.post(url, json=payload)

@app.route("/")
def home():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    try:
        if data.get("event") == "message":
            phone = data["message"]["phone"]
            message_text = data["message"]["text"].strip().lower()

            # Aqui é onde o Leone começa a agir como corretor consultivo
            resposta_inicial = (
                "👋 Oi! Aqui é o *Leone*, da Brabus. Me diga seu nome e o que está buscando — "
                "imóvel para morar ou investir? Quero entender seu perfil e te ajudar como um consultor faria. Vamos juntos."
            )
            send_message(phone, resposta_inicial)
    except Exception as e:
        print(f"Erro no webhook: {e}")
    return "OK"

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
