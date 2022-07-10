""" FAST API - Imdb"""
import os
import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """ API publica de consulta de filmes na base do IMDB """
    return {"Titulo": "Imdb - Consultas sobre Filmes"}


@app.get("/imdb/top-250")
def read_top250():
    """ Top 250 Melhores filmes """
    host = os.environ.get('HOST_IMDB')
    api_key = os.getenv('API_KEY')
    url = f'{host}/en/API/Top250Movies/{api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        data = response.content
    return data