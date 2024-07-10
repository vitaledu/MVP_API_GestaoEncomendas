
# Encomendas API Frontend

Este é um frontend simples para consumir a `encomendas_api` e a `distancia_api`. Ele permite cadastrar encomendas, consultar detalhes de encomendas, e calcular a distância entre dois endereços.


## Requisitos

  

- Um servidor backend rodando a `encomendas_api` na porta `5000`.

- Um servidor backend rodando a `distancia_api` na porta `5001`.

  

## Estrutura do Projeto

  

-  `index.html`: Arquivo principal HTML contendo a estrutura da página.

-  `style.css`: Arquivo opcional para estilos customizados.

-  `script.js`: Arquivo JavaScript contendo a lógica para consumir as APIs.

-  `nginx.conf`: Configuração personalizada do Nginx.

-  `Dockerfile`: Arquivo para construção da imagem Docker.

-  `README.md`: Documentação do projeto.

  

## Como Usar

  

1. Clone o repositório:

```sh

git clone https://github.com/vitaledu/MVP_frontend_GestaoEncomendas.git

cd MVP_frontend_GestaoEncomendas

```

  

2. Certifique-se de que as APIs `encomendas_api` e `distancia_api` estão rodando nas portas corretas.

  

3. Abra o `index.html` no seu navegador.

  

## Usando Docker

  

### Construção da Imagem

  

Para construir a imagem Docker, execute o seguinte comando na raiz do projeto:

  

```sh
docker  build  -t  encomendas_frontend  .
```
Executar  o  Contêiner

Para  executar  o  contêiner  Docker  e  conectá-lo  à  mesma  rede  que  o  encomendas_api  e  distancia_api,  execute  o  seguinte  comando:

```sh
docker  run  -d  --name  encomendas_frontend  --network  minha_rede  -p  8585:8585  encomendas_frontend
```

## Funcionalidades

### Cadastrar Encomenda

- Preencha o formulário com o código de rastreamento, descrição, endereço de origem, e endereço de destino.
- Clique em "Cadastrar" para enviar a encomenda.

### Consultar Encomenda

- Insira o ID da encomenda no formulário de consulta.
- Clique em "Consultar" para buscar os detalhes da encomenda.

### Calcular Distância

- Preencha os endereços de origem e destino no formulário de distância.
- Clique em "Calcular" para obter a distância entre os endereços.

## Tecnologias Usadas

- HTML
- CSS
- JavaScript
- jQuery
- Bootstrap 4.5
- Nginx

## Repositórios Relacionados

Este projeto faz parte de um conjunto de três repositórios que se complementam, mas cada um pode ser utilizado separadamente em outros projetos, caso necessário.

- **API para Calcular Distância entre CEPs**
  - GitHub: [MVP_API_CalcularDistanciaCEP](https://github.com/vitaledu/MVP_API_CalcularDistanciaCEP)
- **API para Gestão de Encomendas**
  - GitHub: [MVP_API_GestaoEncomendas](https://github.com/vitaledu/MVP_API_GestaoEncomendas)
- **Frontend para Gestão de Encomendas (este repositório)**
  - GitHub: [MVP_frontend_GestaoEncomendas](https://github.com/vitaledu/MVP_frontend_GestaoEncomendas)

## Contato

Para mais informações, entre em contato com [eduardolimavital@gmail.com].
