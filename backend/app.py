from flask import Flask
from flask_cors import CORS
from controllers.carro_controller import carro_bp

app = Flask(__name__)
CORS(app) # Permite o Front conversar com o Back

# Rota para a página inicial (evita o erro 404 no Render)
@app.route('/')
def home():
    return "API da Garagem Motors está rodando! 🚗💨 Use a rota /carros"

# Registra as rotas do controller
app.register_blueprint(carro_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)