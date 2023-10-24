from Src.Model.DataBase import SubCategoryDb
from sqlalchemy.exc import IntegrityError
from setting import db


class SubCategoryController:
    def createSubCategory(_description, _status, _createdDate, _updatedDate,_idCategory):
        category = SubCategoryDb(
            _description.upper(), _status, _createdDate, _updatedDate,_idCategory
        )
        db.session.add(category)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    def updateSubCategory(id, _description, _status, _updatedDate,_idCategory):
        try:
            SubCategoryDb.query.filter_by(id=id).update(
                {
                    'description': _description.upper(),
                    'status': _status,
                    'updatedDate': _updatedDate,
                    'idCategory': _idCategory
                }
            )
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    def List(_subCategoryFilter) -> str:
        if len(_subCategoryFilter) < 1:
            query = SubCategoryDb.query.all()
            queryCount = SubCategoryDb.query.count()

        return {
            "subCategories": [row.as_dict() for row in query],
            "count": queryCount
        }
