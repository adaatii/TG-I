from flask import Blueprint
from Src.View.EmployeeView import Employee
from Src.View.CategoryView import Category
from Src.View.SubCategoryView import SubCategory
from Src.View.ProductView import Product


Router = Blueprint('router', __name__)

Router.register_blueprint(Employee, url_prefix='/employees')
Router.register_blueprint(Category, url_prefix='/categories')
Router.register_blueprint(SubCategory, url_prefix='/subCategories')
Router.register_blueprint(Product, url_prefix='/products')
