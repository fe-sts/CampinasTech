from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/imobiliaria'
app.debug = True
appi = Api(app=app, version="1", title="Imobiliaria",
           description="Sistema imobiliaria")
db = SQLAlchemy(app)

#CRIAR NAMESPACES E MODELS
CLIENTES = appi.namespace('CLIENTES', description="CLIENTES")
MODEL_CLIENTE = appi.model('CLIENTES', {'NOME_CLIENTE ': fields.String(required=True,
                                                                          description="NOME_CLIENTE"),
                                             'CPF': fields.String(required=True,
                                                                         description="CPF"),
                                             'RG': fields.String(required=True,
                                                                       description="RG"),
                                             'CEP': fields.String(required=True,
                                                                  description="CEP"),
                                             'DT_NASCIMENTO': fields.String(required=True,
                                                                 description="DT_NASCIMENTO"),
                                             'ESTADO_CIVIL': fields.Date(required=True,
                                                                            description="ESTADO_CIVIL")})
CLIENTE_PUT = appi.model('CLIENTES', {'NOME_CLIENTE': fields.String(description="NOME_CLIENTE"),
                                                 'CPF': fields.String(description="CPF"),
                                                 'RG': fields.String(description="RG"),
                                                 'CEP': fields.String(description="CEP"),
                                                 'DT_NASCIMENTO': fields.String(description="DT_NASCIMENTO"),
                                                 'ESTADO_CIVIL': fields.String(description="ESTADO_CIVIL")})

#TABELAS / OBJETOS
class CLIENTES(db.Model):
    ID_CLIENTE = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    NOME_CLIENTE = db.Column(db.String)
    CPF = db.Column(db.String)
    RG = db.Column(db.String)
    DT_NASCIMENTO = db.Column(db.String)
    ESTADO_CIVIL = db.Column(db.String)
    
    def __init__(self, NOME_CLIENTE, CPF, RG, DT_NASCIMENTO, ESTADO_CIVIL):
        self.NOME_CLIENTE = NOME_CLIENTE
        self.CPF = CPF
        self.RG = RG
        self.DT_NASCIMENTO = DT_NASCIMENTO
        self.ESTADO_CIVIL = ESTADO_CIVIL
db.create_all()


# CLIENTE - POST, GET, PUT, DELETE
@CLIENTES.route('/CLIENTES', methods=['GET', 'POST'])
class CLASSE_CLIENTE(Resource):

    @appi.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        try:
            CLIENTES = CLIENTES.query.all()
            LISTA_CLIENTES = []
            for CLIENTES in CLIENTES:
                CURRCLIENTES = {}
                CURRCLIENTES['ID_CLIENTE'] = CLIENTES.ID_CLIENTE
                CURRCLIENTES['NOME_CLIENTE'] = CLIENTES.NOME_CLIENTE
                CURRCLIENTES['CPF'] = CLIENTES.CPF
                CURRCLIENTES['RG'] = CLIENTES.RG
                CURRCLIENTES['DT_NASCIMENTO'] = CLIENTES.DT_NASCIMENTO
                CURRCLIENTES['ESTADO_CIVIL'] = CLIENTES.ESTADO_CIVIL
                cli.append(CURRCLIENTES)
            return jsonify(cli)

    @appi.expect(CLIENTES)
    def post(self):
        try:
            DADOS_CLIENTE = request.get_json()
            DADOS_CLIENTE = CLIENTES(
                NOME_CLIENTE=DADOS_CLIENTE['NOME_CLIENTE'],
                CPF=DADOS_CLIENTE['CPF'],
                RG=DADOS_CLIENTE['RG'],
                endereco=DADOS_CLIENTE['DT_NASCIMENTO'],
                cep=DADOS_CLIENTE['ESTADO_CIVIL'])
            db.session.add(CLIENTES)
            db.session.commit()
            return jsonify(DADOS_CLIENTE)

@CLIENTES.route('/CLIENTE/<int:ID_CLIENTE>')
class CLASSE_CLIENTE(Resource):
    def delete(self, ID_CLIENTE):
        try:
            DELETA_CLIENTE = CLIENTES.query.filter(
                CLIENTES.ID_CLIENTE == ID_CLIENTE).delete()
            db.session.commit()
            return jsonify(DELETA_CLIENTE)

@CLIENTES.route('/CLIENTE/<int:ID>')
class CLASSE_CLIENTE(Resource):
    @appi.expect(CLIENTES)
    def put(self, id):
        try:
            CLIENTES_PUT = CLIENTES.query.get(id)
            CLIENTES_PUT.NOME_CLIENTE = request.json.get('NOME_CLIENTE', CLIENTES_PUT.NOME_CLIENTE)
            CLIENTES_PUT.CPF = request.json.get('CPF', CLIENTES_PUT.CPF)
            CLIENTES_PUT.RG = request.json.get('RG', CLIENTES_PUT.RG)
            CLIENTES_PUT.DT_NASCIMENTO = request.json.get('DT_NASCIMENTO', CLIENTES_PUT.DT_NASCIMENTO)
            CLIENTES_PUT.ESTADO_CIVIL = request.json.get('ESTADO_CIVIL', CLIENTES_PUT.ESTADO_CIVIL)
            db.session.commit()
            return jsonify({
                'NOME_CLIENTE': CLIENTES_PUT.NOME_CLIENTE,
                'CPF': CLIENTES_PUT.CPF,
                'RG': CLIENTES_PUT.RG,
                'DT_NASCIMENTO': CLIENTES_PUT.DT_NASCIMENTO,
                'ESTADO_CIVIL': CLIENTES_PUT.ESTADO_CIVIL
            })