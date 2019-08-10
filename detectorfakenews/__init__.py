from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'klsdsdlki0230rweifi20fw'

from detectorfakenews import routes