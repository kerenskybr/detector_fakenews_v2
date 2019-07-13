from sklearn.externals import joblib

class carregaCache(object):

    
    def __init__(self):

        self.x_train_tfidf = joblib.load('cache/x_train_tfidf.sav')            
        self.x_test_tfidf = joblib.load('cache/x_test_tfidf.sav')

        self.y_test = joblib.load('cache/y_test.sav')
        self.y_train = joblib.load('cache/y_train.sav')

        self.x = joblib.load('cache/x_save.sav')
        self.y = joblib.load('cache/y_save.sav')

        print('Modelo de Treino e Teste carregado do cache.')


    def __call__(self):

        return self.x_train_tfidf, x_test_tfidf, y_test, y_train, x, y
