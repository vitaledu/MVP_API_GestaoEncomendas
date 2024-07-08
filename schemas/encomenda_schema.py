from marshmallow import Schema, fields

class EncomendaSchema(Schema):
    id = fields.Int(dump_only=True)
    codigo_rastreamento = fields.Str(required=True)
    descricao = fields.Str(required=True)
    endereco_origem = fields.Str(required=True)
    endereco_destino = fields.Str(required=True)
    status = fields.Str(required=True)
