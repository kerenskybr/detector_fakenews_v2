import requests
import os

from detectorfakenews import app


from flask import render_template, url_for
from bs4 import BeautifulSoup


@app.route('/pt_br/home', methods=['GET','POST'])
def index_pt_br():


	return render_template('/pt_br/index.html')


@app.route('/en/home', methods=['GET','POST'])
def index_en():


	return render_template('/en/index.html')