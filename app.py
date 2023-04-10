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
    
    
@app.route("/subdivision", methods=['GET'])
def subdivision():
    subdivisions = db.session.query(Subdivision).all()
    return str(subdivisions)


@app.route("/employee", methods=['GET'])
def employee():
    employees = db.session.query(Employee).all()
    return str(employees)


@app.route("/request", methods=['GET'])
def requests():
    requests = db.session.query(Request).all()
    return str(requests)

@app.route("/visit", methods=['GET'])
def visit():
    visits = db.session.query(Visit).all()
    return str(visits)

@app.route("/visitorpass", methods=['GET'])
def visitorpass():
    visitorpasses = db.session.query(VisitorPass).all()
    return str(visitorpasses)

@app.route("/visitorrequest", methods=['GET'])
def visitorrequest():
    visitorrequests = db.session.query(VisitorRequest).all()
    return str(visitorrequests)

"""
#Импорт
@app.route("/import")
def imported():
    
    #Импорт работников и подразделений
    excel_data = pd.read_excel("import/Сессия_1.xlsx", 2)
    data = pd.DataFrame(excel_data)
    for index, row in data.iterrows():
        
        subdivision = Subdivision(subdivisionID=None, name=row[1])
        db.session.add(subdivision)
        db.session.commit()
        db.session.add(Employee(employeeID=row[2], fio=row[0], subdivisionId=subdivision.subdivisionID, login=None, password=None))
        db.session.commit()
    
    
    #Импорт одиночных заявок
    excel_data = pd.read_excel("import/Сессия_1.xlsx", 0)
    data = pd.DataFrame(excel_data)
    for index, row in data.iterrows():
        fio = row[0].split(" ")
        passport = row[4].split(" ")
        
        visitor = Visitor(visitorID=None, organization=None, surname=fio[0] ,firstname=fio[1], patronym=fio[2], phone=row[1], email=str(row[2]).lower(), birthdate=row[3], passport_number=passport[0], passport_series=passport[1], login=row[5], password=row[6])
        db.session.add(visitor)
        visit_data = row[7].split('_')
        db.session.commit()
        employee = db.session.query(Employee).filter(Employee.employeeID == int(visit_data[1])).first()
        visit = Visit(visitID=None, date=visit_data[0], group=None, employeeId=employee.employeeID)
        db.session.add(visit)
        db.session.commit()
        db.session.add(VisitorPass(visitor_passID = None, start_date=visit_data[0], end_date=visit_data[0], group=None, reason=None, visitId=visit.visitID, visitorId=visitor.visitorID, subdivisionId = employee.subdivisionId))
        db.session.commit()
 
    
    #Импорт групповых заявок
    excel_data = pd.read_excel("import/Сессия_1.xlsx", 1)
    data = pd.DataFrame(excel_data)
    for index, row in data.iterrows():
        fio = row[0].split(" ")
        passport = row[4].split(" ")
        visitor = Visitor(visitorID=None, organization=None, surname=fio[0] ,firstname=fio[1], patronym=fio[2], phone=row[1], email=str(row[2]).lower(), birthdate=row[3], passport_number=passport[0], passport_series=passport[1], login=row[5], password=row[6])
        db.session.add(visitor)
        visit_data = row[7].split('_')
        visit = None
        if db.session.query(Visit).filter(Visit.group == int(str(visit_data[4]).replace("ГР", ""))).count() == 0:    
            visit = Visit(visitID=None, employeeId=visit_data[3], date=visit_data[0], group = int(str(visit_data[4]).replace("ГР", "")))
            db.session.add(visit)
        elif db.session.query(Visit).all().__len__() == 0:
            visit = Visit(visitID=None, employeeId=visit_data[3], date=visit_data[0], group = int(str(visit_data[4]).replace("ГР", "")))
            db.session.add(visit)
        else:
            visit = db.session.query(Visit).all()[-1]
        db.session.commit()
        db.session.add(VisitorPass(visitor_passID = None, start_date=visit_data[0], end_date=visit_data[0], group=int(str(visit_data[4]).replace("ГР", "")), reason=None, visitId=visit.visitID, visitorId=visitor.visitorID, subdivisionId = db.session.query(Subdivision).filter(Subdivision.name==visit_data[1]).first().subdivisionID))
        db.session.commit()
    
    return "ok"
"""