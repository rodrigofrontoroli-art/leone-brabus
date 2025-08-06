from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Leone Brabus está rodando com sucesso!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("Mensagem recebida:", data)

        # Extrai o telefone e a mensagem recebida
        phone = data.get("phone", "")
        msg = data.get("text", "").lower()

        # Resposta básica
        if "studio" in msg:
            reply = "Perfeito! Você está buscando um studio para investir ou para morar?"
        elif "oi" in msg or "olá" in msg:
            reply = "Olá! Sou o Leone, corretor da Brabus. Me diz uma coisa: qual tipo de imóvel você procura?"
        else:
            reply = "Legal! Me conta um pouco mais do que você está buscando."

        # Monta resposta para Z-API
        return jsonify({
            "messages": [
                {
                    "text": reply,
                    "phone": phone
                }
            ]
        }), 200

    except Exception as e:
        print("Erro:", e)
        return jsonify({"error": str(e)}), 500
