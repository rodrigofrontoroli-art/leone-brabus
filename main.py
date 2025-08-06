from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Leone Brabus está rodando com sucesso!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # LOG SIMPLES NO CONSOLE
    print(f"[{datetime.now()}] Webhook recebido:")
    print(data)

    # EXEMPLO DE TRATAMENTO DE MENSAGEM TEXTO
    if data.get('type') == 'message' and 'text' in data:
        mensagem = data['text']
        telefone = data.get('phone')
        print(f"Mensagem de {telefone}: {mensagem}")

        # AQUI ENTRA SUA LÓGICA DE RESPOSTA INTELIGENTE (em breve)

    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
