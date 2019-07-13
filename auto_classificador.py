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

        print('Processando dados. Este processo pode demorar...')
        
        for linha in arquivo_csv.values:

            #linha[1] e a posicao que sera analisada, no caso a segunda coluna
            titulo_fit = tfidf_load.transform([linha[1]])

            predito = carrega_modelo.predict(titulo_fit)

            if predito == 0:
                #Criando a lista de noticias preditas como verdadeiras
                lista_verdadeira.append(linha[1])
            else:
                lista_falsa.append(linha[1])

        print('Criando arquivos csv para notícias falsas e verdadeiras.')

        verdadeira = pd.Series(lista_verdadeira)
        falsa = pd.Series(lista_falsa)

        verdadeira.to_csv('verdadeira.csv')
        falsa.to_csv('falsa.csv')


    def preProcessamento(self):
        
        falsa = pd.read_csv('falsa.csv', index_col=[0])
        falsa.columns = ['titulo']
        
        verdadeira = pd.read_csv('verdadeira.csv', index_col=[0])
        verdadeira.columns = ['titulo']

        #Removendo espaços em branco, caracteres especiais e colocando em minusculo
        verdadeira['titulo'] = verdadeira['titulo'].str.replace(r'\d+',' ')
        verdadeira['titulo'] = verdadeira['titulo'].str.replace('|""=(),“{!`ºª‘?´$%[^\w\s]','')
        verdadeira['titulo'] = verdadeira['titulo'].str.lower()
        verdadeira = verdadeira.dropna()

        #print(verdadeira.head())

        falsa['titulo'] = falsa['titulo'].str.replace(r'\d+',' ')
        falsa['titulo'] = falsa['titulo'].str.replace('|""=(),“{!`ºª‘?´$%[^\w\s]','')
        falsa['titulo'] = falsa['titulo'].str.lower()
        falsa = falsa.dropna()

        falsa['label'] = 1
        verdadeira['label'] = 0

        dados = pd.concat([verdadeira,falsa], axis=0, sort=True)

        y = dados.label.values
        x = dados.titulo.values

        #Dividindo entre teste e treino
        #Stratify = retorna mesma proporção
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.25, stratify=y)
        
        #Baixando o 'bag of words'
        nltk.download('stopwords')

        #Vetorizando palavras para numeros

        pt_stopwords = set(nltk.corpus.stopwords.words('portuguese'))

        tfidf = TfidfVectorizer(min_df = 1, strip_accents = 'unicode', max_features = 3000,
                                analyzer = 'word', ngram_range = (1,3), sublinear_tf = 1, 
                                encoding='utf-8', stop_words = pt_stopwords)

        x_train_tfidf = tfidf.fit_transform(x_train)
        x_test_tfidf = tfidf.transform(x_test)
        

    def modeloRegressaoLogistica(self):
        #Classificando com Regressao Logistica
        classificador = LogisticRegression()
        classificador.fit(x_train_tfidf, y_train)
        print('#' * 40)
        print('Acuracia do modelo Regressão Logística: {:.4f}'.format(classificador.score(x_test_tfidf, y_test)))

        clf_log_reg = make_pipeline(TfidfVectorizer(), LogisticRegression())

        scores_a = cross_val_score(clf_log_reg, x, y, cv=10)
        print('Validação Cruzada Reg Log', np.mean(scores_a))
        print('#' * 40)
        

    def modeloNaiveBayes(self):

        pass

    def modeloRedeNeural(self):

        pass










if __name__ == "__main__":

    #Caminho para os dados que serão analisados
    dados = pd.read_csv('scraper/falsa/saude_gov_fake_news_titulo.csv')

    
    """
    Instanciando a classe que processa os dados e
    retorna os arquivos csv's separados por falsa
    e verdadeira
    """
    teste = ProcessadorDados(dados)

    #Chamando o metodo que avalia os novos dados
    teste.preProcessamento()

    #Processando os dados gerados com RL
    #teste.modeloRegressaoLogistica()