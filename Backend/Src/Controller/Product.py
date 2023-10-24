from Src.Model.DataBase import CategoryDb, ProductDb
from sqlalchemy.exc import IntegrityError
from setting import db


class ProductController:
    def createProduct(_description, _price, _idSubCategory, _createdDate, _updatedDate):
        employee = ProductDb(
            _description.upper(), _price, _idSubCategory,  _createdDate, _updatedDate
        )
        db.session.add(employee)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    def updateProduct(id, _description,_price, _idSubCategory,  _updatedDate):
        try:
            ProductDb.query.filter_by(id=id).update(
                {
                    'description': _description.upper(),
                    'price': _price,                   
                    'idSubCategory': _idSubCategory,              
                    'updatedDate': _updatedDate
                }
            )
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    def List(_productFilter) -> str:
        #        if len(_productFilter) < 1:
        #             query = ProductDb.query\
        #                 .join(CategoryDb, ProductDb.id_category == CategoryDb.id)\
        #                 .add_columns(ProductDb.name, ProductDb.phone, ProductDb.email,\
        #                 CategoryDb.description, ProductDb.status, ProductDb.createdDate,\
        #                 ProductDb.updatedDate, ProductDb.id)\
        #                 .filter(ProductDb.id_category == CategoryDb.id).all()
        #
        #             var = []
        #
        #             for employee in query:
        #                 var.append({
        #                     "createdDate": employee[6],
        #                     "email": employee[3],
        #                     "id": employee[-1],
        #                     "label_category": employee[4],
        #                     "name": employee[1],
        #                     "phone": employee[2],
        #                     "status": employee[5],
        #                     "updatedDate": employee[7]
        #                 })
        #
                 return {
                     "employees": var
                 }
