from flask import Flask, render_template, request
app = Flask(__name__)



class Item():
    def __init__(self,name, amount):
        self.name = name
        self.amount = amount


@app.route("/")
def hello():
    
    items = [
        Item("Apfel",5),
        Item("Computer", 1),
        Item("Birne", 4)
    ]

    for item in items:
        item.amount = item.amount * 2

    person =("Max","Mustermann")
    return render_template ("start.html", name="made by Dominik", person=person , items=items)


@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")

    print(name)
    print(age)
    return render_template ("test.html", name = name, age=age)

@app.route("/currency")
def currency():

    currency1 = request.args.get("Currency1","EUR")
    currency2 = request.args.get("Currency2","USD")
    rate = float(request.args.get("rate","1.14"))


    table1= []
    for x in range(1,10):
        table1.append((x,round((x*rate),2)))
    table2 = []
    for x in range(1, 10):
        table2.append((x, round((x / rate),2)))
    print(table2)
    return render_template("currency.html",
                           rate=rate,
                           currency1=currency1,
                           currency2=currency2,
                           table1=table1,
                           table2=table2)
