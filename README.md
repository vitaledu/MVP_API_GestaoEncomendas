# Encomendas API

## Descrição

A Encomendas API é uma API RESTful construída com Flask e SQLAlchemy para gerenciar encomendas e calcular distâncias entre endereços. A API permite criar, atualizar, visualizar e deletar encomendas, além de calcular a distância entre dois endereços fornecidos.

## Funcionalidades

- **Adicionar uma Encomenda**: Permite adicionar uma nova encomenda ao sistema.
- **Visualizar uma Encomenda**: Permite visualizar os detalhes de uma encomenda específica usando o ID da encomenda.
- **Atualizar uma Encomenda**: Permite atualizar os detalhes de uma encomenda existente.
- **Deletar uma Encomenda**: Permite deletar uma encomenda existente do sistema.
- **Calcular Distância**: Calcula a distância entre dois endereços fornecidos.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu_usuario/encomendas_api.git
    cd encomendas_api
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Execute a aplicação:
    ```sh
    flask run
    ```

## Estrutura do Projeto

- `model/`: Contém o modelo de dados `Encomenda`.
- `schemas/`: Contém os esquemas Marshmallow para serialização de dados.
- `app.py`: Arquivo principal da aplicação Flask.
- `logger.py`: Configuração do logger.
- `requirements.txt`: Arquivo de dependências.
- `README.md`: Documentação do projeto.

## Rotas da API

- `POST /encomendas`: Adiciona uma nova encomenda.
- `GET /encomendas/<id>`: Obtém o status de uma encomenda específica.
- `PUT /encomendas/<id>`: Atualiza informações da encomenda.
- `DELETE /encomendas/<id>`: Remove uma encomenda.
- `GET /distancia`: Calcula a distância entre dois endereços.

## Swagger

A documentação e testes da API podem ser acessados via Swagger em `http://localhost:5000/`.

## Docker

### Construção da Imagem

Para construir a imagem Docker, execute o seguinte comando na raiz do projeto:

```sh
docker build -t encomendas_api .
Executar o Contêiner
Para executar o contêiner Docker, execute o seguinte comando:

sh
Copy code
docker run -d -p 5000:5000 encomendas_api
Exemplo de Uso
Adicionar uma Encomenda
sh
Copy code
curl -X POST "http://localhost:5000/encomendas" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"codigo_rastreamento\": \"123456\", \"descricao\": \"Encomenda 1\", \"endereco_origem\": \"Origem\", \"endereco_destino\": \"Destino\", \"status\": \"Em trânsito\"}"
Visualizar uma Encomenda
sh
Copy code
curl -X GET "http://localhost:5000/encomendas/1" -H "accept: application/json"
Atualizar uma Encomenda
sh
Copy code
curl -X PUT "http://localhost:5000/encomendas/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"codigo_rastreamento\": \"654321\", \"descricao\": \"Encomenda Atualizada\", \"endereco_origem\": \"Origem Atualizada\", \"endereco_destino\": \"Destino Atualizado\", \"status\": \"Entregue\"}"
Deletar uma Encomenda
sh
Copy code
curl -X DELETE "http://localhost:5000/encomendas/1" -H "accept: application/json"
Calcular Distância
sh
Copy code
curl -X GET "http://localhost:5000/distancia?origem=Origem&destino=Destino" -H "accept: application/json"
