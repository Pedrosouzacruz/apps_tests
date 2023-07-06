from flask import Flask,request,json
from flask_restful import Resource,Api
from habilidades import Habilidades
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {   'id':'0',
        'nome': 'Pedro',
        'habilidades' : ['Python','Javascript','Java']},
     {  'id':1,
        'nome':'Luely',
        'habilidades':['Flask','Angular','Vue.js']}]

class desenvolvedor(Resource):
    def get(self,id):  
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'Status': 'Erro', 'Mensagem' : mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API.'
            response = {'Status': 'Erro', 'Mensagem' : mensagem}
        return response
    
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self,id):
        desenvolvedores.pop(id)
        return{'Status': 'Sucesso', 'mensagem': 'Registro Excluído'}
    


class listadesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    

api.add_resource(desenvolvedor, '/dev/<int:id>/')
api.add_resource(listadesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/dev/habilidades/','/dev/habilidades/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)
