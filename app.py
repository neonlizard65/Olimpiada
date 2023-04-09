from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from models import Visitor, Subdivision, Employee, Request, Visit, VisitorPass, VisitorRequest
from connection import db
import pandas as pd
from models import Visitor


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://aleksei:123@localhost/olimp" #Connection to db, imports are postgresql and psycopg2-binary
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/request.html")
def request_form():
  return render_template('request.html')  


@app.route("/visitors", methods=['GET'])
def visitors():
    """
    excel_data = pd.read_excel("import/Сессия_1.xlsx")
    data = pd.DataFrame(excel_data)
    for index, row in data.iterrows():
        fio = row[0].split(" ")
        passport = row[4].split(" ")
        db.session.add(Visitor(visitorID=None, organization=None, surname=fio[0] ,firstname=fio[1], patronym=fio[2], phone=row[1], email=str(row[2]).lower(), birthdate=row[3], passport_number=passport[0], passport_series=passport[1], login=row[5], password=row[6]))
    db.session.commit()
    """
    if request.method == 'GET':
        visitors = db.session.query(Visitor).all()
        return str(visitors)
    
@app.route("/visitors/<int:id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def visitor_by_id(id):
    if request.method == 'GET':
        visitor = db.get_or_404(Visitor, id)
        return str(visitor)
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    
    
@app.route("/subdivision")
def subdivision():
    subdivisions = db.session.query(Subdivision).all()
    return str(subdivisions)


@app.route("/employee")
def employee():
    employees = db.session.query(Employee).all()
    return str(employees)


@app.route("/request")
def requests():
    requests = db.session.query(Request).all()
    return str(requests)

@app.route("/visit")
def visit():
    visits = db.session.query(Visit).all()
    return str(visits)

@app.route("/visitorpass")
def VisitorPass():
    visitorpasses = db.session.query(VisitorPass).all()
    return str(visitorpasses)

@app.route("/visitorrequest")
def VisitorRequest():
    visitorrequests = db.session.query(VisitorRequest).all()
    return str(visitorrequests)

@app.route("/import")
def imported():
    excel_data = pd.read_excel("import/Сессия_1.xlsx", 2)
    data = pd.DataFrame(excel_data)
    for index, row in data.iterrows():
        subdivision = db.session.query(Subdivision).filter_by(name=row[1]).first()

        db.session.add(Employee(employeeID=row[2], fio=row[0], subdivisionId=subdivision.subdivisionID, login=None, password=None))
    db.session.commit()
    return "ok"