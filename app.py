from math import e
from flask import Flask, render_template, request, redirect, jsonify, Response
from flask_migrate import Migrate
from models import Visitor, Subdivision, Employee, Request, Visit, VisitorPass, VisitorRequest
from connection import db
import pandas as pd
from models import Visitor
import json

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

@app.route("/visitors", methods=['GET', 'POST'])
def visitors():
    if request.method == 'GET':
        visitors = db.session.query(Visitor).all()
        return jsonify(visitors)
    elif request.method == 'POST':
        login = request.json['login']
        password = request.json['password']
        email = request.json['email']
        surname = request.json['surname']
        firstname = request.json['firstname']
        patronym = request.json['patronym']
        birthday = request.json['birthday']
        phone = request.json['phone']
        organization = request.json['organization']
        passport_series = request.json['passport_series']
        passport_number = request.json['passport_number']
        passport_scan = request.json['passport_number']
        photo = request.json['photo']
        visitor = Visitor(visitorID=None, login=login, password=password, email=email, surname=surname, firstname=firstname, patronym=patronym, birthday=birthday, phone=phone, organization=organization, passport_series=passport_series, passport_number=passport_number, passport_scan=passport_scan, photo=photo)
        db.session.add(visitor)
        db.session.commit()
        return Response("Объект успешно создан", status=201)
    
@app.route("/visitors/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def visitor_by_id(id):
    if request.method == 'GET':
        visitor = db.get_or_404(Visitor, id)
        return jsonify(visitor)
    elif request.method == 'PUT':
        visitor = db.get_or_404(Visitor, id)
        visitor.visitorID = request.json['visitorID']
        visitor.login = request.json['login']
        visitor.password = request.json['password']
        visitor.email = request.json['email']
        visitor.surname = request.json['surname']
        visitor.firstname = request.json['firstname']
        visitor.patronym = request.json['patronym']
        visitor.birthday = request.json['birthday']
        visitor.phone = request.json['phone']
        visitor.organization = request.json['organization']
        visitor.passport_series = request.json['passport_series']
        visitor.passport_number = request.json['passport_number']
        visitor.passport_scan = request.json['passport_number']
        visitor.photo = request.json['photo']
        db.session.commit()
        return Response("Объект успешно обновлен", status=204)
    elif request.method == 'DELETE':
        visitor = db.get_or_404(Visitor, id)
        db.session.delete(visitor)
        db.session.commit()
        return Response("Объект Удален", status=204)
    
    
@app.route("/subdivision", methods=['GET', 'POST'])
def subdivision():
    if request.method == 'GET':
        subdivisions = db.session.query(Subdivision).all()
        return jsonify(subdivisions) 
    elif request.method == 'POST':
        name = request.json['name']
        db.session.add(Subdivision(subdivisionID = None, name=name))
        db.session.commit()
        return Response("Объект создан", status=201)

@app.route("/subdivision/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def subdivision_by_id(id):
    if request.method == 'GET':
        subdivision = db.get_or_404(Subdivision, id)
        return jsonify(subdivision)
    elif request.method == 'PUT':
        subdivision = db.get_or_404(Subdivision, id)
        subdivision.subdivisionID = request.json['subdivisionID']
        subdivision.name = request.json['name']
        db.session.commit()
        return Response("Объект обновлен", status=204)
    elif request.method == 'DELETE':
        subdivision = db.get_or_404(Subdivision, id)
        db.session.delete(subdivision)
        db.session.commit()
        return Response("Объект Удален", status=204)
        
        
@app.route("/employee", methods=['GET', 'POST'])
def employee():
    if request.method == 'GET':
        employees = db.session.query(Employee).all()
        return jsonify(employees)
    elif request.method == 'POST':
        fio = request.json['fio']
        subdivisionId = request.json['subdivisionId']
        isotdel = request.json['isotdel']
        login = request.json['login']
        password = request.json['password']
        db.session.add(Employee(fio = fio, subdivisionId = subdivisionId, isotdel = isotdel, login = login, password = password))
        db.session.commit()
        return Response("Объект создан", status=201)

@app.route("/employee/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def employee_by_id(id):
    if request.method == 'GET':
        employee = db.get_or_404(Employee, id)
        return jsonify(employee)
    elif request.method == 'PUT':
        employee = db.get_or_404(Employee, id)
        employee.fio = request.json['fio']
        employee.subdivisionId = request.json['subdivisionId']
        employee.isotdel = request.json['isotdel']
        employee.login = request.json['login']
        employee.password = request.json['password']
        db.session.commit()
        return Response("Объект обновлен", status=204)
    elif request.method == 'DELETE':
        db.session.delete(db.get_or_404(Employee, id))
        db.session.commit()
        return Response("Объект Удален", status=204)

@app.route("/request", methods=['GET', 'POST'])
def requests():
    if request.method == 'GET':
        requests = db.session.query(Request).all()
        return jsonify(requests)
    elif request.method == 'POST':
        date = request.json['date']
        type = request.json['type']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        reason = request.json['reason']
        subdivisionId = request.json['subdivisionId']
        approved = request.json['approved']
        employeeId = request.json['employeeId']
        db.session.add(Request(date = date, type = type, start_date = start_date, end_date = end_date, reason = reason, subdivisionId = subdivisionId, approved = approved, employeeId = employeeId))
        db.session.commit()
        return Response("Объект создан", status = 204)


@app.route("/request/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def requests_by_id(id):
    if request.method == 'GET':
        user_request = db.get_or_404(Request, id)
        return jsonify(user_request)
    elif request.method == 'PUT':
        user_request = db.get_or_404(Request, id)
        user_request.date = request.json['date']
        user_request.type = request.json['type']
        user_request.start_date = request.json['start_date']
        user_request.end_date = request.json['end_date']
        user_request.reason = request.json['reason']
        user_request.subdivisionId = request.json['subdivisionId']
        user_request.approved = request.json['approved']
        user_request.employeeId = request.json['employeeId']
        db.session.commit()
        return Response("Объект обновлен", status=204)
    elif request.method == 'DELETE':
        user_request = db.get_or_404(Request, id)
        db.session.delete(user_request)
        db.session.commit()
        return Response("Объект удален", status=204)


@app.route("/visit", methods=['GET', 'POST'])
def visit():
    if request.method == 'GET':
        visits = db.session.query(Visit).all()
        return jsonify(visits)
    elif request.method == 'POST':
        employeeId = request.json['employeeId']
        date = request.json['date']
        group = request.json['group']
        db.session.add(Visit(employeeId = employeeId, date = date, group = group))
        db.session.commit()
        return Response("Объект создан", status = 204)
        
@app.route("/visit/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def visit_by_id(id):
    if request.method == 'GET':
        return jsonify(db.get_or_404(Visit, id))
    elif request.method == 'POST':
        visit = db.get_or_404(Visit, id)
        visit.employeeId = request.json['employeeId']
        visit.date = request.json['date']
        visit.group = request.json['group']
        db.session.commit()
        return Response("Объект обновлен", status=204)
    elif request.method == 'DELETE':
        visit = db.get_or_404(Visit, id)
        db.session.delete(visit)
        db.session.commit()
        return Response("Объект удален", status=204)


@app.route("/visitorpass", methods=['GET', 'POST'])
def visitorpass():
    if request.method == 'GET':
        visitorpasses = db.session.query(VisitorPass).all()
        return jsonify(visitorpasses)
    elif request.method == 'POST':
        visitorId = request.json['visitorId']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        reason = request.json['reason']
        group = request.json['group']
        subdivisionId = request.json['subdivisionId']
        db.session.add(VisitorPass(visitorId=visitorId, start_date=start_date, end_date=end_date, reason=reason, group=group, subdivisionId=subdivisionId))
        db.session.commit()
        return Response("Объект создан", status = 204)

@app.route("/visitorpass/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def visitorpass_by_id(id):
    if request.method == 'GET':
        return jsonify(db.get_or_404(VisitorPass, id))
    elif request.method == 'PUT':
        visitorpass = db.get_or_404(VisitorPass, id)
        visitorpass.visitorId = request.json['visitorId']
        visitorpass.start_date = request.json['start_date']
        visitorpass.end_date = request.json['end_date']
        visitorpass.reason = request.json['reason']
        visitorpass.group = request.json['group']
        visitorpass.subdivisionId = request.json['subdivisionId']
        db.session.commit()
        return Response("Объект обновлен", status=204)
    elif request.method == 'DELETE':
        db.session.delete(db.get_or_404(VisitorPass, id))
        db.session.commit()
        return Response("Объект удален", status=204)
        


@app.route("/visitorrequest", methods=['GET', 'POST'])
def visitorrequest():
    if request.method == 'GET':
        visitorrequests = db.session.query(VisitorRequest).all()
        return jsonify(visitorrequests)
    elif request.method == 'POST':
        visitorId = request.json['visitorId']
        requestId = request.json['requestId']
        group = request.json['group']
        db.session.add(VisitorRequest(visitorId=visitorId, requestId=requestId, group=group))
        db.session.commit()
        return Response("Объект создан", status = 204)

@app.route("/visitorrequest/<int:id>", methods=['GET', 'POST'])
def visitorrequest_by_id(id):
    if request.method == 'GET':
        return jsonify(db.get_or_404(VisitorRequest, id))
    elif request.method == 'PUT':
        visitorrequest = db.get_or_404(VisitorRequest, id)
        visitorrequest.visitorId = request.json['visitorId']
        visitorrequest.requestId = request.json['requestId']
        visitorrequest.group = request.json['group']
        db.session.commit()
        return Response("Объект обновлен", status=204)
    elif request.method == 'DELETE':
        db.session.delete(db.get_or_404(VisitorRequest, id))
        db.session.commit()
        return Response("Объект удален", status=204)


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



@app.route("/test")
def test():
    with app.test_client() as client:    
        post_request = client.post('/subdivision', json=json.loads(
            """
            {
                "subdivisionID" : null,
                "name": "Новый"
            }
            """))
    return "Ok"


@app.route("/testput/<int:id>")
def testput(id):
    with app.test_client() as client:    
        put_request = client.put(f'/subdivision/{id}', json=json.loads(
            """
            {
                "subdivisionID" : "%d",
                "name": "Старый"
            }
            """ % id))
    return "Ok"