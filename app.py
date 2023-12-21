from flask import Flask, request, jsonify
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases_create import Usuario

import json

os.system("python execute_request.py")

app = Flask(__name__)

@app.route('/get-endpoint', methods=['GET'])
def handle_get():

    return "Rquisição GET recebida!"

@app.route('/post-endpoint', methods=['POST'])
def handle_post():
    post_data = request.get_json()

    print(" Dados recebidos", post_data)

    # with open("saida_endpoint.json","a") as file:
    #     json.dump(post_data,file)
    #     file.write("\n")
    
    # with open("saida_endpoint.json", 'r') as arquivo:
    #     registros = json.load(arquivo)

    
    engine = create_engine('sqlite:///user_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    for data in post_data:
        novo_usuario = Usuario(id=data['id'],nome=data['nome'],idade=data['idade'],email=data['email'])
        session.add(novo_usuario)
        session.commit()
    session.close()



    

    return jsonify(message="Dados recebidos e salvos com sucesso!")

if __name__ == '__main__':
    app.run(debug=True, port=5000)