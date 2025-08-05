from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)
    return jsonify({"status": "recebido"}), 200

@app.route('/', methods=['GET'])
def home():
    return "Leone Brabus está rodando com sucesso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)