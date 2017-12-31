from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, DecimalField, validators, SubmitField, RadioField
from wtforms.validators import DataRequired
import os



class Transaction:

     def __init__(self, name, amt, plus_minus):
         self.name = name
         self.amt = amt
         self.plus_minus = plus_minus

class Initial_Form(Form):
    income = StringField("u'Whats your income? ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class Balance:

    def __init__(self, initial_income):
        self.initial_income = initial_income
        self.balance = self.initial_income



WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def add():
    form = Initial_Form()
    if form.is_submitted():
        balance = float(form.income.data)
        global bal
        bal = Balance(balance)
        return render_template("bal.html", balance=balance)
    return render_template("t.html", form=form)

@app.route("/main", methods=["GET", "POST"])
def hello():
    global bal
    try:
        if request.method == "POST":
            plus_minus = request.form["plus_minus"]
            obj = Transaction(request.form["name"], float(request.form["amount"]), plus_minus)
            bal.lst.append(obj)
            if plus_minus == "income":
                new_bal = bal.plus(obj)
                return render_template("bal.html", balance=new_bal)
            elif plus_minus == "expense":
                new_bal = bal.minus(obj)
                return render_template("bal.html", balance=new_bal)
    except:
        return "<h1>Press back and Try Again</h1>"
    else:
        return render_template("bal.html")


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
