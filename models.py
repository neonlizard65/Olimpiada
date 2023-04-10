from connection import db

class Subdivision(db.Model):
    __tablename__ = "subdivision" #Table name
    
    subdivisionID = db.Column("subdivisionID", db.Integer, primary_key=True) #ID, PK
    name = db.Column("name", db.String(30), nullable=False) #Name of subdivision
    
    #Constructor
    def __init__(self, subdivisionID, name):
        self.subdivisionID = subdivisionID
        self.name = name
    
    #db.String representation
    def __repr__(self):
        return f"({self.subdivisionID}) {self.name}"
    

class Employee(db.Model):
    __tablename__ = "employee"
    
    employeeID = db.Column("employeeID", db.Integer, primary_key=True)
    fio = db.Column("fio", db.String(50), nullable=False)
    subdivisionId = db.Column("subdivisionId", db.ForeignKey("subdivision.subdivisionID"), nullable=False)
    isotdel = db.Column("isotdel", db.Boolean)
    login = db.Column("login", db.String(30))
    password = db.Column("password", db.String(30))
    
    def __init__(self, employeeID, fio, subdivisionId, login, password):
        self.employeeID = employeeID
        self.fio = fio
        self.subdivisionId = subdivisionId
        self.login = login
        self.password = password
        
    def __repr__(self):
        return f"({self.employeeID}) {self.fio}, {self.subdivisionId}, {self.login}, {self.password}"

class Visitor(db.Model):
    __tablename__ = "visitor"
    
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
    
    def __init__(self, visitorID:int, login:str, password, email, surname, firstname, patronym, phone, birthdate, organization, passport_series, passport_number):
        self.visitorID = visitorID
        self.login = login
        self.password = password
        self.email = email
        self.surname = surname
        self.firstname = firstname
        self.patronym = patronym
        self.birthdate = birthdate
        self.phone = phone
        self.organization = organization
        self.passport_number = passport_number
        self.passport_series = passport_series
        
    def __repr__(self):
        return f"({self.visitorID}) {self.surname} {self.firstname} {self.patronym}"
      
class Request(db.Model):
    __tablename__ = "request"
    
    requestID = db.Column("requestID", db.Integer, primary_key=True)
    date = db.Column("date", db.DateTime)
    type = db.Column("type", db.Boolean)
    start_date = db.Column("start_date", db.DateTime)
    end_date = db.Column("end_date", db.DateTime)
    reason = db.Column("reason", db.String)
    subdivisionId = db.Column("subdivisionId", db.ForeignKey("subdivision.subdivisionID"))
    approved = db.Column("approved", db.Boolean)
    employeeId = db.Column("employeeId", db.ForeignKey("employee.employeeID"))
    
    def __init__(self, requestID, date, type, start_date, end_date, reason, subdivisionId, approved, employeeId):
        self.requestID = requestID
        self.date = date
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.subdivisionId = subdivisionId
        self.approved = approved
        self.employeeId = employeeId
    
    def __repr__(self):
        pass  
    
class Visit(db.Model):
    
    __tablename__ = "visit"
    
    visitID = db.Column("visitID", db.Integer, primary_key=True)
    employeeId = db.Column("employeeId", db.ForeignKey("employee.employeeID"))
    date = db.Column("date", db.DateTime)
    group = db.Column("group", db.Integer)
    
    def __init__(self, visitID, employeeId, date, group):
        self.visitID = visitID
        self.employeeId = employeeId
        self.date = date
        self.group = group
        
    def __repr__(self):
        pass  

class VisitorPass(db.Model):
    
    __tablename__ = "visitor_pass"
    
    visitor_passID = db.Column("visitor_passID", db.Integer, primary_key=True)
    visitorId = db.Column("visitorId", db.ForeignKey("visitor.visitorID"))
    visitId = db.Column("visitId", db.ForeignKey("visit.visitID"))
    start_date = db.Column("start_date", db.DateTime)
    end_date = db.Column("end_date", db.DateTime)
    reason = db.Column("reason", db.String)
    group = db.Column("group", db.Integer)
    subdivisionId = db.Column("subdivisionId", db.ForeignKey("subdivision.subdivisionID"))
    
    
    def __init__(self, visitor_passID, visitorId, visitId, start_date, end_date, reason, group, subdivisionId):
        self.visitor_passID = visitor_passID
        self.visitorId = visitorId
        self.visitId = visitId
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.group = group
        self.subdivisionId = subdivisionId
    
    def __repr__(self):
        pass  
    
class VisitorRequest(db.Model):
    
    __tablename__ = "visitor_request"
    
    visitor_requestID = db.Column("visitor_requestID", db.Integer, primary_key=True)
    visitorId = db.Column("visitorId", db.ForeignKey("visitor.visitorID"))
    requestId = db.Column("requestId", db.ForeignKey("request.requestID"))
    group = db.Column("group", db.Integer)
    
    def __init__(self, visitor_requestID, visitorId, requestId, group):
        self.visitor_requestID = visitor_requestID
        self.visitorId = visitorId
        self.requestId = requestId
        self.group = group
        
    def __repr__(self):
        pass  
        