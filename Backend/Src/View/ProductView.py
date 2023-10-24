from flask import Blueprint, request
from datetime import datetime
from pytz import timezone
from Src.Controller.Product import ProductController
from Src.Controller.Category import CategoryController
from flask_api import status


Product = Blueprint('employees', __name__)

@Product.get("/")
def listProduct():
    _employeeFilter = request.values.get("employeeName")
    if _employeeFilter == "None" or _employeeFilter is None:
        _employeeFilter = ""
    employees = ProductController.List(_employeeFilter)
    categories = CategoryController.List("")

   
    
    
    return ProductController.List(_employeeFilter)


@Product.post("/")
def createProduct():
    params = request.json
    _description = params['description']
    _price = params['price']
    _idSubCategory = params['idSubCategory']
    _createdDate = datetime.now(
        timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
    _updatedDate = _createdDate

    if any((x is None or x == "") for x in [_description, _idSubCategory, _price]):
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if ProductController.createProduct(
            _description, _price, _idSubCategory, _createdDate, _updatedDate
        ):
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Product already exists'}, status.HTTP_409_CONFLICT


@Product.put("/<int:id>")
def updateProduct(id):
    params = request.json
    _description = params['description']
    _price = params['price']
    _idSubCategory = params['idSubCategory']
    _updatedDate = datetime.now(
        timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
    if any((x is None or x == "") for x in [_description, _idSubCategory, _price]):
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if ProductController.updateProduct(id, _description, _price, _idSubCategory, _updatedDate):
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Category already exists'}, status.HTTP_409_CONFLICT
