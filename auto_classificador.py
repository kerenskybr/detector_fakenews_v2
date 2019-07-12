import csv
import os
import pandas as pd
import numpy as np 


import nltk

from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
'''
with open("/falsa/saude_gov_fake_news_titulo.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        print 'line[{}] = {}'.format(i, line)
'''
'''
data = pd.read_csv('scraper/falsa/saude_gov_fake_news_titulo.csv')

# read row line by line
for d in data.values:
  # read column by index
  print(d[1])
'''

class ProcessadorDados:
    """
    A classe contém todos atributos para execução.
    Para utilizar, basta instanciar passando o diretório
    do arquivo csv, e depois chamar os métodos. Ex:
    ProcessadorDados('/dados/meu.csv')
    """
    
    def __init__(self, arquivo_csv):
        """
        Carrega o modelo ja treinado. Pode ser subistituido bastando
        para isso alterar a linha abaixo. É necessário em alguns casos
        também gerar um novo TFID
        """
        carrega_modelo = joblib.load('algoritmo/saves/modelo_reg_log.sav')

        tfidf_load = joblib.load('algoritmo/saves/tfid.sav')

        #0 pra verdadeira e 1 pra falsa
        lista_falsa = []
        lista_verdadeira = []

        self.arquivo_csv = arquivo_csv
        pagina = 1
        for d in arquivo_csv.values:

            titulo_fit = tfidf_load.transform([d[1]])

            predito = carrega_modelo.predict(titulo_fit)

            if predito == 0:
                #Criando a lista de noticias preditas como verdadeiras
                lista_verdadeira.append(d[1])
            else:
                lista_falsa.append(d[1])

            
            #print([d[1]], predito)
        verdadeira = pd.Series(lista_verdadeira)
        falsa = pd.Series(lista_falsa)

        verdadeira.to_csv('verdadeira.csv')
        falsa.to_csv('falsa.csv')

    #def preProcessamento(self):

        #self.arquivo

dados = pd.read_csv('scraper/falsa/saude_gov_fake_news_titulo.csv')

teste = ProcessadorDados(dados)