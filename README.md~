# 📊 Previsão de Demandas com IA (FastAPI + Prophet)

Este projeto utiliza **Inteligência Artificial (IA)** para prever demandas futuras com base em dados históricos. A solução foi desenvolvida com **FastAPI** para a criação da API e **Prophet** (do Facebook) para modelagem de séries temporais.

---
## 🚀 Tecnologias Utilizadas
- **Python 3.12**
- **FastAPI** (Framework para API)
- **Prophet** (Modelo de previsão de séries temporais)
- **Pandas** (Manipulação de dados)
- **Scikit-learn** (Métricas de avaliação)
- **Uvicorn** (Servidor ASGI)

---
## 📌 Como Executar o Projeto
### 1️⃣ Clonar o Repositório
```sh
git clone <URL_DO_REPOSITORIO>
cd previsao-demanda
```

### 2️⃣ Iniciar o Servidor FastAPI
```sh
uvicorn api:app --reload
```
A API ficará acessível em **http://127.0.0.1:8000**.

### 3️⃣ Testar 
Acesse **http://127.0.0.1:8000/docs** para testar os endpoints.

---
## 📡 Endpoints da API

### 🔹 **Prever Demanda** (`POST /predict`)
**Entrada:**
```json
{
    "data": ["2025-03-01", "2025-03-02", "2025-03-03"],
    "vendas": [150, 160, 170]
}
```
**Saída:**
```json
{
    "previsao": {
        "2025-03-04": 180.5,
        "2025-03-05": 190.7
    }
}
```

### 🔹 **Avaliar o Modelo** (`POST /evaluate`)
**Entrada:** Mesmo formato do `/predict`.
**Saída:**
```json
{
    "erro_medio_absoluto": 3.77
}
```

---
## 📌 Explicação da IA Utilizada
O **Prophet** é um modelo avançado de previsão de séries temporais que considera:
✅ Tendências de longo prazo  
✅ Sazonalidades diárias, semanais e anuais  
✅ Eventos específicos (como feriados)  
Isso torna a previsão mais precisa do que métodos simples de regressão!

---
## 🤖 Autor
👤 **Lucas de Togni**  
📌 Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/lucas-de-togni/)

---


 
 
