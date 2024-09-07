from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return jsonify("'message': 'Bem vindo ao Flask' ")

@app.route('/cliente', methods=['POST'])
def cliente():
    data = request.get_json()
    return jsonify(data)


@app.route('/produto', methods=['POST'])
def produto():
     request.get_json()
     return jsonify("'message': 'Cadastro de Produtos' ")


if __name__ == '__main__':
    app.run(debug=True)