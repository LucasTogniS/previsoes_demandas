import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

def treinar_previsao(dados, dias_previsao=7):
    df = pd.DataFrame({"ds": dados["data"], "y": dados["vendas"]})
    df["ds"] = pd.to_datetime(df["ds"])

    df["cap"] = df["y"].max() * 1.2
    df["floor"] = df["y"].min() * 0.8

    modelo = Prophet(
        growth="logistic",
        seasonality_mode="multiplicative",
        changepoint_prior_scale=0.05
    )

    modelo.add_seasonality(name="mensal", period=30.5, fourier_order=5)
    modelo.fit(df)

    futuro = modelo.make_future_dataframe(periods=dias_previsao)
    futuro["cap"] = df["cap"].max()
    futuro["floor"] = df["floor"].min()

    previsao = modelo.predict(futuro)

    resultado = previsao[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(dias_previsao)

    return {
        row["ds"].strftime("%Y-%m-%d"): {
            "previsao": round(row["yhat"], 2),
            "min": round(row["yhat_lower"], 2),
            "max": round(row["yhat_upper"], 2)
        }
        for _, row in resultado.iterrows()
    }

def avaliar(dados, dias_teste=7):
    df = pd.DataFrame({"ds": dados["data"], "y": dados["vendas"]})
    df["ds"] = pd.to_datetime(df["ds"])

    if df.shape[0] <= dias_teste:
        raise ValueError("Dados insuficiente para avaliação. Necessário mais históricos.")

    treino = df[:-dias_teste]
    teste = df[-dias_teste:]

    modelo = Prophet()
    modelo.fit(treino)

    futuro = modelo.make_future_dataframe(periods=dias_teste)
    previsao = modelo.predict(futuro)

    mae = mean_absolute_error(teste["y"], previsao["yhat"].tail(dias_teste))
    return mae
