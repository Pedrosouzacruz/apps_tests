from flask_restful import Resource
from flask import json, request

lista_habilidades =[{'id':'0' ,'Habilidade':'Python'}, 
                    {'id':1 ,'Habilidade':'Javascript'},
                     {'id': 2,'Habilidade':'Java'},
                     {'id': 3,'Habilidade':'Ruby'}, 
                     {'id':4 ,'Habilidade':'Angular'},
                    {'id':5 ,'Habilidade':'Nodejs'}, 
                    {'id':6 ,'Habilidade':'Vue:js'}, 
                    {'id':7,'Habilidade':'PHP'}, 
                   {'id': 8,'Habilidade':'html'}]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def put(self, id):
        for habilidade in lista_habilidades:
            if str(habilidade['id']) == id:
                habilidade['Habilidade'] = request.json['Habilidade']
                return habilidade
        return {'error': 'Habilidade not found.'}, 404
    
    def delete(self, id):
            for habilidade in lista_habilidades:
                if str(habilidade['id']) == id:
                    lista_habilidades.remove(habilidade)
                    return {'message': 'Habilidade deleted.'}
            return {'error': 'Habilidade not found.'}, 404
    
    def post(self):
        nova_habilidade = {'id': len(lista_habilidades), 'Habilidade': request.json['Habilidade']}
        lista_habilidades.append(nova_habilidade)
        return nova_habilidade