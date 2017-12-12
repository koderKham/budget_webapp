from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, DecimalField, validators, SubmitField, RadioField
from wtforms.validators import DataRequired

#def bal():
    #take the income & remove the field, but display balance
    #take the name and amount and make it a dictionary then add it to a list
    #do calculation
class transactionForm(Form):
    name = StringField("Name", validators=[DataRequired()])
    amount = StringField("Amount", validators=[DataRequired()])
    plus_minus = RadioField('Label', choices=[('plus','income'),('minus','expense')])
    submit = SubmitField()

class Transaction:

     def __init__(self, name, amt, plus_minus):
         self.name = name
         self.amt = amt
         self.plus_minus = plus_minus

class Initial_Form(Form):
    income = StringField("Whats your income? ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class Balance:

    def __init__(self, initial_income):
        self.initial_income = initial_income
        self.balance = self.initial_income

    def minus(self, y):
        self.balance = self.balance - y.amt
        return self.balance

    def plus(self, y):
        self.balance = self.balance + y.amt
        return self.balance

    def perc(self, y):
        math = y.amt / self.initial_income
        return math * 100

    def request(self):
        return self.balance


def empty_list():
    for i in lst:
        lst.remove(i)

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

lst = []
bal_lst = []
def empty_list(it):
    for i in it:
        it.remove(i)

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def add():
    empty_list(lst)
    empty_list(bal_lst)
    form = Initial_Form()
    t_form = transactionForm()
    if form.is_submitted():
        balance = float(form.income.data)
        bal = Balance(balance)
        #bal_lst.append(bal)
        return render_template("bal.html", t_form=t_form, balance=balance)
    return render_template("t.html", form=form)

@app.route("/main", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        plus_minus = request.form["plus_minus"]
        obj = Transaction(request.form["name"], float(request.form["amount"]), plus_minus)
        lst.append(obj)
        if plus_minus == "income":
            new_bal = bal.plus(obj)#bal_lst[0].plus(obj)
            return render_template("bal.html", balance=new_bal)
        elif plus_minus == "expense":
            new_bal = bal.minus(obj)#bal_lst[0].minus(obj)
            return render_template("bal.html", balance=new_bal)
    else:
        return render_template("bal.html")

@app.route("/table", methods=["GET", "POST"])
def table():
    return render_template("table.html", lst=lst, bal=bal)#bal_lst=bal_lst)


if __name__ == '__main__':
    app.run(debug=True)
