
# Microsserviço Serverless para Validação de CPF

Este projeto implementa um microsserviço serverless na **Azure Functions** para validar CPF.

Ele recebe um CPF via requisição HTTP e retorna um JSON indicando se o CPF é válido ou não.

## 🚀 Funcionalidades

- Validação de formato do CPF.
- Verificação do dígito verificador.
- Resposta em formato JSON.

## 🛠️ Tecnologias Utilizadas

- [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/)
- Python 3.x
- Azure CLI
- Azure Functions Core Tools

  ## 🧑‍💻  Para Executar Localmente

### Pré-requisitos

- Python 3.x instalado
- Azure Functions Core Tools instalado
- Azure CLI instalado

### 

1. Clonando o repositório:
   (bash)
  git clone https://github.com/Eduardo-Nunes-Santos/microsservicos-serverless-validacao-cpf-azure.git
  cd microsservicos-serverless-validacao-cpf-azure
   

2. Instale as dependências:
   (bash)
   
  pip install -r requirements.txt
  
4. Inicie o servidor local:
   (bash)
   
 func start
  
5. Faça uma requisição HTTP:
   (bash)
   
   curl -X POST http://localhost:7071/api/ValidateCPF -H "Content-Type: application/json" -d '{"cpf": "12345678909"}'


## 📌 Testando Localmente

1️⃣ Inicie o Azure Functions localmente:

 func start
 
2️⃣ A API estará disponível em:

http://localhost:7071/api/ValidateCPF

3️⃣ Para testar, use Postman, cURL ou Python Requests:

### Usando cURL

curl -X POST "http://localhost:7071/api/ValidateCPF" \
     -H "Content-Type: application/json" \
     -d '{"cpf": "12345678909"}'

     
### Se o CPF for válido, a resposta será:


{
    "cpf": "12345678909",
    "valid": true
}


### Usando Python Requests

import requests


url = "http://localhost:7071/api/ValidateCPF"

data = {"cpf": "12345678909"}

response = requests.post(url, json=data)

print(response.json())

  
