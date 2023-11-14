from Src.Model.DataBase import EmployeeDb
from sqlalchemy.exc import IntegrityError
from setting import db
from werkzeug.security import generate_password_hash


class EmployeeController:
    def createEmployee(_name, _cpf, _email, _passwd , _status, _updatedDate,_createdDate):
        _passwdHash = generate_password_hash(_passwd)
        employee = EmployeeDb(
            _name.upper(), _cpf, _email.upper(), _passwdHash , _status, _updatedDate,_createdDate)
        db.session.add(employee)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    def updateEmployee(id, _name, _cpf, _email, _passwd , _status, _updatedDate):
#        _passwdHash = generate_password_hash(_passwd)
        try:
            EmployeeDb.query.filter_by(id=id).update(
                {
                    'name': _name.upper(),
                    'cpf': _cpf,
                    'email': _email.upper(),
                    'passwd': _passwd,
                    'status': _status,
                    'updatedDate': _updatedDate
                }
            )
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    # def List(_employeeFilter) -> str:
    #     if len(_employeeFilter) < 1:
    #         query = EmployeeDb.query.all()

    #         var = []

    #         for employee in query:
    #             var.append({
    #                 "id": employee[-1],
    #                 "name": employee[1],
    #                 "email": employee[2],
    #                 "cpf": employee[3],
    #                 "passwd": employee[4],
    #                 "status": employee[5],
    #                 "updatedDate": employee[6],
    #                 "createdDate": employee[7]
    #             })

    #     return {
    #         "employees": var
    #     }

    def List(_employeeFilter) -> str:
        if len(_employeeFilter) < 1:
            query = EmployeeDb.query.all()
            queryCount = EmployeeDb.query.count()

        return {
            "employees": [row.as_dict() for row in query],
            "count": queryCount
        }
