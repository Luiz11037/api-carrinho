from flask import Flask
#Instanciando app.
app = Flask(__name__)

#importando as rotas(GET, POST, DELETE, PUT)
from routes import *

#Isso precisa estar no final.
if __name__ == "__main__":
    app.run(debug=True)
