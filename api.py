from fastapi import FastAPI
from pydantic import BaseModel
from model import treinar_previsao, avaliar

app = FastAPI()

class DadosEntrada(BaseModel):
    data: list[str]
    vendas: list[float]

@app.post("/predict")
def previsao(dados: DadosEntrada):
    resultado = treinar_previsao(dados.dict())
    return {"previsao": resultado}

@app.post("/evaluate")
def avaliacao(dados: DadosEntrada):
    erro = avaliar(dados.dict())
    return {"erro_medio_absoluto": round(erro, 2)}
