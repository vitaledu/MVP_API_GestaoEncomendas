from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from model.encomenda_model import Encomenda, SessionLocal
from schemas.encomenda_schema import EncomendaSchema
from sqlalchemy.orm import Session
import logger
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, allow_headers="*", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])  # Permite todas as origens e métodos.

api = Api(app, version='1.0', title='Encomendas API', description='API para gerenciar encomendas')

# Logger
logger.setup_logger()
log = logger.get_logger(__name__)

encomenda_model = api.model('Encomenda', {
    'codigo_rastreamento': fields.String(required=True, description='Código de rastreamento da encomenda'),
    'descricao': fields.String(required=True, description='Descrição da encomenda'),
    'endereco_origem': fields.String(required=True, description='Endereço de origem da encomenda'),
    'endereco_destino': fields.String(required=True, description='Endereço de destino da encomenda'),
    'status': fields.String(description='Status da encomenda')
})

@api.route('/encomendas')
class EncomendaList(Resource):
    @api.expect(encomenda_model)
    @api.response(201, 'Encomenda adicionada com sucesso')
    def post(self):
        session: Session = SessionLocal()
        try:
            encomenda_data = request.json
            encomenda = Encomenda(**encomenda_data)
            session.add(encomenda)
            session.commit()
            session.refresh(encomenda)
            log.info(f"Encomenda adicionada: {encomenda.codigo_rastreamento}")
            return EncomendaSchema().dump(encomenda), 201
        except Exception as e:
            session.rollback()
            log.error(f"Erro ao adicionar encomenda: {e}")
            return {"error": "Erro ao adicionar encomenda"}, 500
        finally:
            session.close()

@api.route('/encomendas/<int:id>')
@api.param('id', 'O identificador da encomenda')
class EncomendaDetail(Resource):
    @api.response(200, 'Encomenda encontrada')
    @api.response(404, 'Encomenda não encontrada')
    def get(self, id):
        session: Session = SessionLocal()
        try:
            encomenda = session.query(Encomenda).filter(Encomenda.id == id).first()
            if encomenda:
                return EncomendaSchema().dump(encomenda)
            else:
                return {"error": "Encomenda não encontrada"}, 404
        except Exception as e:
            log.error(f"Erro ao obter encomenda: {e}")
            return {"error": "Erro ao obter encomenda"}, 500
        finally:
            session.close()

    @api.expect(encomenda_model)
    @api.response(200, 'Encomenda atualizada com sucesso')
    @api.response(404, 'Encomenda não encontrada')
    def put(self, id):
        session: Session = SessionLocal()
        try:
            encomenda_data = request.json
            encomenda = session.query(Encomenda).filter(Encomenda.id == id).first()
            if encomenda:
                for key, value in encomenda_data.items():
                    setattr(encomenda, key, value)
                session.commit()
                session.refresh(encomenda)
                log.info(f"Encomenda atualizada: {encomenda.codigo_rastreamento}")
                return EncomendaSchema().dump(encomenda)
            else:
                return {"error": "Encomenda não encontrada"}, 404
        except Exception as e:
            session.rollback()
            log.error(f"Erro ao atualizar encomenda: {e}")
            return {"error": "Erro ao atualizar encomenda"}, 500
        finally:
            session.close()

    @api.response(200, 'Encomenda deletada com sucesso')
    @api.response(404, 'Encomenda não encontrada')
    def delete(self, id):
        session: Session = SessionLocal()
        try:
            encomenda = session.query(Encomenda).filter(Encomenda.id == id).first()
            if encomenda:
                session.delete(encomenda)
                session.commit()
                log.info(f"Encomenda deletada: {encomenda.codigo_rastreamento}")
                return {"message": "Encomenda deletada com sucesso"}
            else:
                return {"error": "Encomenda não encontrada"}, 404
        except Exception as e:
            session.rollback()
            log.error(f"Erro ao deletar encomenda: {e}")
            return {"error": "Erro ao deletar encomenda"}, 500
        finally:
            session.close()

@api.route('/distancia')
@api.param('origem', 'Endereço de origem')
@api.param('destino', 'Endereço de destino')
class Distancia(Resource):
    @api.response(200, 'Distância calculada com sucesso')
    def get(self):
        origem = request.args.get('origem')
        destino = request.args.get('destino')
        distancia = calcular_distancia_externa(origem, destino)
        log.info(f"Distância calculada entre {origem} e {destino}: {distancia} km")
        return {"origem": origem, "destino": destino, "distancia": distancia}

@api.route('/encomendas/<int:id>/entregar')
@api.param('id', 'O identificador da encomenda')
class EncomendaEntregar(Resource):
    @api.response(200, 'Encomenda marcada como entregue')
    @api.response(404, 'Encomenda não encontrada')
    def put(self, id):
        session: Session = SessionLocal()
        try:
            encomenda = session.query(Encomenda).filter(Encomenda.id == id).first()
            if encomenda:
                encomenda.status = 'Entregue'
                session.commit()
                session.refresh(encomenda)
                log.info(f"Encomenda marcada como entregue: {encomenda.codigo_rastreamento}")
                return EncomendaSchema().dump(encomenda)
            else:
                return {"error": "Encomenda não encontrada"}, 404
        except Exception as e:
            session.rollback()
            log.error(f"Erro ao marcar encomenda como entregue: {e}")
            return {"error": "Erro ao marcar encomenda como entregue"}, 500
        finally:
            session.close()

    def options(self, id):
        return {'Allow': 'PUT'}, 200

@api.route('/encomendas/<int:id>/em_transito')
@api.param('id', 'O identificador da encomenda')
class EncomendaEmTransito(Resource):
    @api.response(200, 'Encomenda marcada como em trânsito')
    @api.response(404, 'Encomenda não encontrada')
    def put(self, id):
        session: Session = SessionLocal()
        try:
            encomenda = session.query(Encomenda).filter(Encomenda.id == id).first()
            if encomenda:
                encomenda.status = 'Em Trânsito'
                session.commit()
                session.refresh(encomenda)
                log.info(f"Encomenda marcada como em trânsito: {encomenda.codigo_rastreamento}")
                return EncomendaSchema().dump(encomenda)
            else:
                return {"error": "Encomenda não encontrada"}, 404
        except Exception as e:
            session.rollback()
            log.error(f"Erro ao marcar encomenda como em trânsito: {e}")
            return {"error": "Erro ao marcar encomenda como em trânsito"}, 500
        finally:
            session.close()

    def options(self, id):
        return {'Allow': 'PUT'}, 200

def calcular_distancia_externa(origem, destino):
    #chamada à API externa
    #return 10.0   Exemplo de distância
    try:
        response = requests.get(f'http://distancia_api:5001/calcular_distancia?origem={origem}&destino={destino}')
        if response.status_code == 200:
            data = response.json()
            return data['distancia']
        else:
            return {"error": "Erro ao calcular distância"}, response.status_code
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
