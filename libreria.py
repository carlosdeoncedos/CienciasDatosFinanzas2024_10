import requests
import pandas as pd

def ejemplo_sumar(x, y):
    '''
    La función ejemplo_sumar, regresa la suma de dos números
    
    Parámetros:
    -x (int/float):  Primer número
    -y (int/float):  Segundo número
    
    Return:
    - int/float:  The sum of x + y
    '''
   
    if not(type(x) in [int, float] and type(y) in [int, float]):
        raise ValueError("los valores deben de ser numéricos")
    
    respuesta = x + y
    
    return respuesta


def precios_binance(par='BTCUSDT', intervalo='1d'):
    """
    Obtiene los precios históricos de una criptomoneda desde la API de Binance y los devuelve en un DataFrame de pandas.

    Esta función envía una solicitud a la API de Binance para obtener datos históricos de precios de una criptomoneda especificada 
    y devuelve la información en un DataFrame con las siguientes columnas: 'Date', 'Open', 'High', 'Low', 'Close', y 'Volume'.
    Los datos se formatean con tipos numéricos apropiados y se establece la fecha como índice.

    Parámetros:
    -----------
    par : str, opcional
        El par de criptomonedas a consultar, por defecto es 'BTCUSDT' (Bitcoin contra Tether).
    intervalo : str, opcional
        El intervalo de tiempo para los datos de precios, por defecto es '1d' (1 día).

        seconds	1s
        minutes	1m, 3m, 5m, 15m, 30m
        hours	1h, 2h, 4h, 6h, 8h, 12h
        days	1d, 3d
        weeks	1w
        months	1M

    Retorna:
    --------
    df : pandas.DataFrame
        Un DataFrame que contiene los precios históricos del par de criptomonedas con las columnas:
        - 'Date': Fecha y hora de los datos.
        - 'Open': Precio de apertura.
        - 'High': Precio máximo.
        - 'Low': Precio mínimo.
        - 'Close': Precio de cierre.
        - 'Volume': Volumen de la criptomoneda en el intervalo especificado.
    """
    
    url_klines = f'https://api.binance.com/api/v3/klines?symbol={par}&interval={intervalo}'
    cripto = requests.get(url_klines).json()
    df = pd.DataFrame(cripto)
    df.drop(columns=df.columns[6:], inplace=True)
    
    columnas = {
    0: 'Date',
    1: 'Open', 
    2: 'High',
    3: 'Low',
    4: 'Close',
    5: 'Volume'
    }

    df.rename(columns=columnas, inplace=True)
    
    lista = ['Open', 'High', 'Low', 'Close', 'Volume']
    lista_fechas = ['Date']

    df[lista] = df[lista].apply(pd.to_numeric)
    df[lista_fechas] = df[lista_fechas].apply(pd.to_datetime, unit='ms')
    df.set_index('Date', inplace=True)

    return df