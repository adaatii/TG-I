from flask import Blueprint, request
from datetime import datetime
from pytz import timezone
from Src.Controller.Product import ProductController
from Src.Controller.SubCategory import SubCategoryController
from flask_api import status


Product = Blueprint('products', __name__)

@Product.get("/")
def listProduct():
    _productFilter = request.values.get("productName")
    if _productFilter == "None" or _productFilter is None:
        _productFilter = ""
    products = ProductController.List(_productFilter)
    subCategories = SubCategoryController.List("")
   
    return ProductController.List(_productFilter)


@Product.post("/")
def createProduct():
    params = request.json
    _description = params['description']
    _price = params['price']
    _idSubCategory = params['idSubCategory']
    _createdDate = datetime.now(
        timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
    _updatedDate = _createdDate
    _status = 1 if params['status'] else 0


    if any((x is None or x == "") for x in [_description, _idSubCategory, _price]):
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if ProductController.createProduct(
            _description, _price, _status, _idSubCategory, _createdDate, _updatedDate
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
    _status = 1 if params['status'] else 0

    if any((x is None or x == "") for x in [_description, _idSubCategory, _price]):
        return {'status': 'error', 'message': 'Fill all of the fields'}, status.HTTP_400_BAD_REQUEST
    else:
        if ProductController.updateProduct(id, _description, _price, _status, _idSubCategory, _updatedDate):
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Category already exists'}, status.HTTP_409_CONFLICT
