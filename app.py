from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir requisições de outros domínios (necessário para desenvolvimento local)

# Rota para registrar um usuário
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Aqui você pode adicionar lógica para salvar os dados em um banco de dados
    # Por exemplo, usando SQLAlchemy para interagir com um banco de dados SQL

    # Para este exemplo, vamos apenas retornar os dados recebidos
    return jsonify({
        'message': 'Usuário registrado com sucesso!',
        'email': email,
        'password': password
    })

if __name__ == '__main__':
        app.run(debug=True)