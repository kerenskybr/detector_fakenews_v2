#Algoritmo utilizando o TITULO das noticias
import os

import collections

import numpy as np 

import pandas as pd

import nltk

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn import svm

#Noticias verdadeiras

ciencia = pd.read_csv(r'../scraper/verdadeira/ciencia.csv') 
cultura = pd.read_csv(r'../scraper/verdadeira/cultura.csv')
economia = pd.read_csv(r'../scraper/verdadeira/economia.csv')
esportes = pd.read_csv(r'../scraper/verdadeira/esportes.csv')
estilo = pd.read_csv(r'../scraper/verdadeira/estilo.csv')
internacional = pd.read_csv(r'../scraper/verdadeira/internacional.csv')
politica = pd.read_csv(r'../scraper/verdadeira/politica.csv')
tecnologia = pd.read_csv(r'../scraper/verdadeira/tecnologia.csv')

verdadeira = pd.concat([ciencia, cultura, economia, esportes, estilo, internacional, politica, tecnologia])

#Noticias Falsas

boatos = pd.read_csv(r'../scraper/falsa/boatos_org_titulo.csv')
boatos = boatos.drop(columns=['quant','tema','url'])


ff = pd.read_csv(r'../scraper/falsa/fato_ou_fake.csv')
ff = ff.drop(columns=['id','corpo','corpo_titulo','url'])

falsa = pd.concat([boatos, ff])

#Excluido colunas desnecesssarias
verdadeira = verdadeira.drop(columns=['id', 'corpo', 'url'])

#Verificando o shape
print('shape noticias verdadeiras',verdadeira.shape)
print('shape noticias falsa',falsa.shape)

#Removendo espaços em branco, caracteres especiais e colocando em minusculo
verdadeira['titulo'] = verdadeira['titulo'].str.replace(r'\d+',' ')
verdadeira['titulo'] = verdadeira['titulo'].str.replace('|""=(),“{!‘?´$%[^\w\s]','')
verdadeira['titulo'] = verdadeira['titulo'].str.lower()
verdadeira = verdadeira.dropna()

print(verdadeira.head())

falsa['titulo'] = falsa['titulo'].str.replace(r'\d+',' ')
falsa['titulo'] = falsa['titulo'].str.replace('|""=(),“{!‘?´$%[^\w\s]','')
falsa['titulo'] = falsa['titulo'].str.lower()
falsa = falsa.dropna()

print(falsa.head())

#Atribuindo a classe classificadora
# 1 para falso, 0 para verdadeiro

falsa['label'] = 1
verdadeira['label'] = 0

dados = pd.concat([verdadeira,falsa], axis=0, sort=True)

y = dados.label.values
x = dados.titulo.values

#Dividindo entre teste e treino
#Stratify = retorna mesma proporção
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.25, stratify=y)

#Baixando o 'bag of words'
#nltk.download('stopwords')

#Vetorizando palavras para numeros

pt_stopwords = set(nltk.corpus.stopwords.words('portuguese'))

tfidf = TfidfVectorizer(min_df = 1, strip_accents = 'unicode', max_features = 3000,
						analyzer = 'word', ngram_range = (1,3), sublinear_tf = 1, 
						encoding='utf-8', stop_words = pt_stopwords)

x_train_tfidf = tfidf.fit_transform(x_train)
x_test_tfidf = tfidf.transform(x_test)

#Classificando com Regressao Logistica
classificador = LogisticRegression()
classificador.fit(x_train_tfidf, y_train)

print('Acuracia do modelo Regressão Logística: {:.4f}'.format(classificador.score(x_test_tfidf, y_test)))

clf_log_reg = make_pipeline(TfidfVectorizer(), LogisticRegression())

scores_a = cross_val_score(clf_log_reg, x, y, cv=10)
print('Validação Cruzada Reg Log', scores_a)

#Classificando com AdaBoost

clf_ada = AdaBoostClassifier(n_estimators=100, random_state=0)
clf_ada.fit(x_train_tfidf, y_train)

print('Acuracia AdaBoost: {:.4f}'.format(clf_ada.score(x_test_tfidf, y_test)))

clf_ada_pipe = make_pipeline(TfidfVectorizer(), AdaBoostClassifier())

scores = cross_val_score(clf_ada_pipe, x, y, cv=10)
print('Validação Cruzada Ada', scores)

#Classificando com Naive Bayes

clf_nb = MultinomialNB().fit(x_train_tfidf,y_train)

preditor_nb = clf_nb.predict(x_test_tfidf)

print('Acuracia do modelo Naive Bayes: {:.4f}'.format(np.mean(preditor_nb == y_test)))

clf_naive = make_pipeline(TfidfVectorizer(), MultinomialNB())

scores = cross_val_score(clf_naive, x, y, cv=10)
print('Validação Cruzada Naive', scores)

#Classificando com o SVM

clf_svm = svm.SVC(gamma=0.001, kernel='linear')
clf_svm.fit(x_train_tfidf, y_train)

clf_svm.predict(x_test_tfidf)

print('Acuracia do modelo SVM: {:.4f}'.format(clf_svm.score(x_test_tfidf, y_test, sample_weight=None)))

clf_svm_pipe = make_pipeline(TfidfVectorizer(), svm.SVC())

scores = cross_val_score(clf_svm_pipe, x, y, cv=10)
print('Validação Cruzada SVM', scores)