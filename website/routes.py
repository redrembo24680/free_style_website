from website import app
from flask import render_template, url_for, request, redirect
from db import Users, session


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        new_user = Users(first_name=request.form['first_name'],
                         second_name=request.form['second_name'],
                         email=request.form['email'],
                         password=request.form['password'],
                         date=request.form['date'],
                         ref_country_id=request.form['ref_country_id'])
        try:
            session.add(
                new_user)

            session.commit()
            return render_template('reg.html')
        except Exception:
            session.rollback()


    else:
        return render_template("register.html")
