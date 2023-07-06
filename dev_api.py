from flask import Flask
from flask import jsonify
from flask import json
from flask import request
import io
import requests

app = Flask(__name__)
desenvolvedores = [
    {   'id':'0',
        'nome': 'Pedro',
        'habilidades' : ['Python','Javascript','Java']},
     {  'id':1,
        'nome':'Luely',
        'habilidades':['Flask','Angular','Vue.js']}]
# Devolve um desenvolvedor pleo ID, tambem altera e deleta pelo id
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'Status': 'Erro', 'Mensagem' : mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API.'
            response = {'Status': 'Erro', 'Mensagem' : mensagem}
        return jsonify(response)
    
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'Sucesso', 'mensagem': 'Registro Excluído'})
    
         
@app.route('/dev/', methods=['GET', 'POST'])       
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)