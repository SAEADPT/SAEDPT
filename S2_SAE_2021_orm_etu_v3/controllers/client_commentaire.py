#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request, redirect

from connexion_db import get_db

client_commentaire = Blueprint('client_commentaire', __name__,
                        template_folder='templates')

@client_commentaire.route('/client/comment/add', methods=['POST'])
def client_comment_add():
    mycursor = get_db().cursor()
    chaussure_id = request.form.get('id_chaussure', None)

    return redirect('/client/chaussure/details/'+chaussure_id)
    #return redirect(url_for('client_chaussure_details', id=int(chaussure_id)))

@client_commentaire.route('/client/comment/delete', methods=['POST'])
def client_comment_detete():
    mycursor = get_db().cursor()
    chaussure_id = request.form.get('id_chaussure', None)

    return redirect('/client/chaussure/details/'+chaussure_id)
    #return redirect(url_for('client_chaussure_details', id=int(chaussure_id)))