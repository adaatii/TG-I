from Src.Model.DataBase import ProductDb, SubCategoryDb
from sqlalchemy.exc import IntegrityError
from setting import db


class ProductController:
    def createProduct(_description, _price, _status, _idSubCategory, _createdDate, _updatedDate):
        product = ProductDb(
            _description.upper(), _price,  _status, _createdDate, _updatedDate, _idSubCategory
        )
        db.session.add(product)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    def updateProduct(id, _description,_price,_status, _idSubCategory,  _updatedDate):
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
        if len(_productFilter) < 1:
            query = ProductDb.query\
                .join(SubCategoryDb, ProductDb.idSubCategory == SubCategoryDb.id)\
                .add_columns(ProductDb.id, ProductDb.description, ProductDb.price, ProductDb.updatedDate, ProductDb.createdDate, ProductDb.status, SubCategoryDb.id)\
                .filter(ProductDb.idSubCategory == SubCategoryDb.id).all()

            var = []

            for product in query:
                var.append({
                    "id": product[1],
                    "description": product[2] ,
                    "price": product[3],
                    "updatedDate": product[4],
                    "createdDate": product[5],
                    "status": product[6],
                    "idSubCategory": product[-1]

                })

        return {
            "products": var
        }
