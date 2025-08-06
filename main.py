from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Leone Brabus está rodando com sucesso!'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print('Mensagem recebida:', data)

        # Exemplo de resposta automática
        response_text = "Olá! Sou o Leone, da Brabus Negócios Imobiliários. Já vou te ajudar."
        
        return jsonify({"reply": response_text}), 200
    except Exception as e:
        print("Erro:", e)
        return jsonify({'error': str(e)}), 500
