# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, request
from dataviva.apps.general.views import get_locale

from flask.ext.wtf import Form
from forms import RegistrationForm
from mock import Article, articles, ids
import time


mod = Blueprint('scholar', __name__,
                template_folder='templates',
                url_prefix='/<lang_code>/scholar')


@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.locale = values.pop('lang_code')


@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', get_locale())


@mod.route('/', methods=['GET'])
def index():
    return render_template('scholar/index.html', articles=articles)


@mod.route('/article/<id>', methods=['GET'])
def show(id):
    id = int(id.encode())
    article = articles[id]
    return render_template('scholar/show.html', article=article, id=id)


@mod.route('/article/new', methods=['GET'])
def new():
    form = RegistrationForm()
    return render_template('scholar/new.html', form=form)


@mod.route('/article/<id>/edit', methods=['GET'])
def edit(id):
    return render_template('scholar/edit.html')


@mod.route('/article', methods=['POST'])
def create():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('scholar/new.html', form=form)
        else:
            title = form.title.data
            theme = form.theme.data
            author = form.author.data
            key_words = form.key_words.data
            abstract = form.abstract.data
            postage_date = time.strftime("%d/%m/%Y")
            id = ids[-1] + 1

            ids.append(id)
            articles.update({id:Article(title, theme, author, key_words, abstract, postage_date)})

            return '''
                    Muito obrigado! Seu estudo foi submetido com sucesso e será analisado pela equipe do DataViva.
                    Em até 15 dias você receberá um retorno sobre sua publicação no site!
                   '''

@mod.route('/article/<id>', methods=['PATCH', 'PUT'])
def update():
    pass


@mod.route('/article/<id>', methods=['DELETE'])
def destroy(id):
    articles.pop(int(id.encode()))
