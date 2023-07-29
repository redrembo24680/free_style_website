from website import app
from flask import render_template, url_for, request, redirect
from db import Users, Country, Products
from flask import session as session
from db import session as ses
from datetime import datetime
from sqlalchemy import select
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os



@app.route("/adult", methods=['POST', 'GET'])
def men():
    requests = select(Products)
    products = ses.scalars(requests)

    return render_template('adult.html', products=products)

