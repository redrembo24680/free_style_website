from website import app
from flask import render_template, url_for, request, redirect
from db import Users, session, Country
from sqlalchemy import select
from datetime import datetime

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        country_id = request.form.get('country')
        new_user = Users(first_name=request.form['first_name'],
                         second_name=request.form['second_name'],
                         email=request.form['email'],
                         password=request.form['password'],
                         date=datetime.date(datetime.strptime(request.form["date"],'%Y-%m-%d')),
                         country=session.get(Country, country_id)
                         )
        try:
            session.add(
                new_user)

            session.commit()
            return render_template('reg.html')

        except Exception:
            session.rollback()

    return render_template("register.html" )


@app.route("/country", methods=["POST", "GET"])
def country():
    if request.method == "POST":
        title = Country(request.form['tittle'])
        try:
            session.add(title)

            session.commit()
            return redirect('/')

        except:
            session.rollback()

    else:

        return render_template("country.html")
