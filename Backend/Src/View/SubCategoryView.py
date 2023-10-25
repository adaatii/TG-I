from flask import Blueprint, request
from datetime import datetime
from pytz import timezone
from Src.Controller.SubCategory import SubCategoryController
from flask_api import status


SubCategory = Blueprint("subCategories", __name__)

@SubCategory.get("/")
def listSubCategory():
    _subCategoryFilter = request.values.get("subCategoryName")
    if _subCategoryFilter == "None" or _subCategoryFilter is None:
        _subCategoryFilter = ""
    return SubCategoryController.List(_subCategoryFilter)


@SubCategory.post("/")
def createSubCategory():
    params = request.json
    _description = params['description']
    _status = 1 if params['status'] else 0
    _createdDate = datetime.now(
        timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
    _updatedDate = _createdDate
    _idCategory = params['idCategory']

    if _description is None or len(_description) < 1:
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if SubCategoryController.createSubCategory(
            _description, _status, _updatedDate, _createdDate,_idCategory
        ):
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Category already exists'}, status.HTTP_409_CONFLICT


@SubCategory.put("/<int:id>")
def updateSubCategory(id):
    params = request.json
    _description = params['description']
    _status = 1 if params['status'] else 0
    _updatedDate = datetime.now(
        timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
    _idCategory = params['idCategory']

    if _description is None or len(_description) < 1:
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if SubCategoryController.updateSubCategory(id, _description, _status, _updatedDate,_idCategory):
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'SubCategory already exists'}, status.HTTP_409_CONFLICT
