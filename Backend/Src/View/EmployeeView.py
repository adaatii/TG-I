from flask import Blueprint, request
from datetime import datetime
from pytz import timezone
from Src.Controller.Employee import EmployeeController
from flask_api import status


Employee = Blueprint('employees', __name__)

@Employee.get("/")
def listEmployee():
    _employeeFilter = request.values.get("employeeName")
    if _employeeFilter == "None" or _employeeFilter is None:
        _employeeFilter = ""
    return EmployeeController.List(_employeeFilter)


@Employee.post("/")
def createEmployee():
    params = request.json
    _name = params['name']
    _cpf = params['cpf']
    _email = params['email']
    _passwd = params['passwd']
    _status = 1 if params['status'] else 0
    _createdDate = datetime.now(
        timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
    _updatedDate = _createdDate

    if any((x is None or x == "") for x in [_name, _passwd, _status]):
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if EmployeeController.createEmployee(
            _name,_cpf, _email, _passwd, _status, _updatedDate, _createdDate
        ):
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Employee already exists'}, status.HTTP_409_CONFLICT


@Employee.put("/<int:id>")
def updateEmployee(id):
    params = request.json
    _name = params['name']
    _cpf = params['cpf']
    _email = params['email']
    _passwd = params['passwd']
    _status = 1 if params['status'] else 0
    _updatedDate = datetime.now(
        timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")

    if any((x is None or x == "") for x in [_name,_cpf,_email, _passwd, _status]):
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if EmployeeController.updateEmployee(id, _name,_cpf, _email, _passwd, _status, _updatedDate):
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Category already exists'}, status.HTTP_409_CONFLICT
