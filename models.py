from connection import db
from dataclasses import dataclass

@dataclass
class Subdivision(db.Model):
    __tablename__ = "subdivision" #Table name
    
    subdivisionID: int
    name: str
    
    subdivisionID = db.Column("subdivisionID", db.Integer, primary_key=True) #ID, PK
    name = db.Column("name", db.String(30), nullable=False) #Name of subdivision
    
@dataclass
class Employee(db.Model):
    __tablename__ = "employee"
    
    employeeID: int
    fio: str
    subdivisionId: int
    isotdel: bool
    login: str
    password: str
    
    employeeID = db.Column("employeeID", db.Integer, primary_key=True)
    fio = db.Column("fio", db.String(50), nullable=False)
    subdivisionId = db.Column("subdivisionId", db.ForeignKey("subdivision.subdivisionID"), nullable=False)
    isotdel = db.Column("isotdel", db.Boolean)
    login = db.Column("login", db.String(30))
    password = db.Column("password", db.String(30))


@dataclass
class Visitor(db.Model):
    __tablename__ = "visitor"
    
    visitorID: int
    login: str
    password: str
    email: str
    surname: str
    firstname: str
    patronym: str
    birthdate: str
    phone: str
    organization: str
    passport_series: str
    passport_number: str
    passport_scan: str
    photo: str
    
    visitorID = db.Column("visitorID", db.Integer, primary_key=True)
    login = db.Column("login", db.String(20))
    password = db.Column("password", db.String(20))
    email = db.Column("email", db.String(50), nullable=False)
    surname = db.Column("surname", db.String(50), nullable=False)
    firstname = db.Column("firstname", db.String(50), nullable=False)
    patronym = db.Column("patronym", db.String(50), nullable=True)
    birthdate = db.Column("birthdate", db.DateTime, nullable=False)
    phone = db.Column("phone", db.String(20), nullable=False)
    organization = db.Column("organization", db.String(50), nullable=True)
    passport_series = db.Column("passport_series", db.String)
    passport_number = db.Column("passport_number", db.String)
    passport_scan = db.Column("passport_scan", db.String(255))
    photo = db.Column("photo", db.String(255))
        
@dataclass
class Request(db.Model):
    __tablename__ = "request"
    
    requestID: int
    date: str
    type: bool
    start_date: str
    end_date: str
    reason: str
    subdivisionId: int
    approved: bool
    employeeId: int
    
    requestID = db.Column("requestID", db.Integer, primary_key=True)
    date = db.Column("date", db.DateTime)
    type = db.Column("type", db.Boolean)
    start_date = db.Column("start_date", db.DateTime)
    end_date = db.Column("end_date", db.DateTime)
    reason = db.Column("reason", db.String)
    subdivisionId = db.Column("subdivisionId", db.ForeignKey("subdivision.subdivisionID"))
    approved = db.Column("approved", db.Boolean)
    employeeId = db.Column("employeeId", db.ForeignKey("employee.employeeID"))
    
@dataclass    
class Visit(db.Model):
    
    __tablename__ = "visit"
    
    visitID: int
    employeeId: int
    date: str
    group: int
    
    visitID = db.Column("visitID", db.Integer, primary_key=True)
    employeeId = db.Column("employeeId", db.ForeignKey("employee.employeeID"))
    date = db.Column("date", db.DateTime)
    group = db.Column("group", db.Integer)

@dataclass
class VisitorPass(db.Model):
    
    __tablename__ = "visitor_pass"
    
    visitor_passID: int
    visitorId: int
    start_date: str
    end_date: str
    reason: str
    group: int
    subdivisionId: int
    
    visitor_passID = db.Column("visitor_passID", db.Integer, primary_key=True)
    visitorId = db.Column("visitorId", db.ForeignKey("visitor.visitorID"))
    visitId = db.Column("visitId", db.ForeignKey("visit.visitID"))
    start_date = db.Column("start_date", db.DateTime)
    end_date = db.Column("end_date", db.DateTime)
    reason = db.Column("reason", db.String)
    group = db.Column("group", db.Integer)
    subdivisionId = db.Column("subdivisionId", db.ForeignKey("subdivision.subdivisionID"))
    
@dataclass
class VisitorRequest(db.Model):
    
    __tablename__ = "visitor_request"
    
    visitor_requestID: int
    visitorId: int
    requestId: int
    group: int
    
    visitor_requestID = db.Column("visitor_requestID", db.Integer, primary_key=True)
    visitorId = db.Column("visitorId", db.ForeignKey("visitor.visitorID"))
    requestId = db.Column("requestId", db.ForeignKey("request.requestID"))
    group = db.Column("group", db.Integer)
        
        