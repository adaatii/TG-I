from setting import db

class EmployeeDb(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True)
    passwd = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    updatedDate = db.Column(db.String(20), nullable=False)
    createdDate = db.Column(db.String(20), nullable=False)
    sale = db.relationship('SaleDb', backref='employee')

    def __init__(self, _name, _cpf, _email,_passwd, _status, _updatedDate, _createdDate):
        self.name = _name
        self.cpf = _cpf
        self.email = _email
        self.passwd = _passwd
        self.status = _status
        self.updatedDate = _updatedDate
        self.createdDate = _createdDate

    def as_dict(self):      
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class CategoryDb(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    updatedDate = db.Column(db.String(20), nullable=False)
    createdDate = db.Column(db.String(20), nullable=False)
    subCategory = db.relationship('SubCategoryDb', backref='category')
    def __init__(self, _description, _status, _updatedDate, _createdDate):
        self.description = _description
        self.status = _status
        self.updatedDate = _updatedDate
        self.createdDate = _createdDate

    def as_dict(self):        
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class SaleDb(db.Model):
    __tablename__ = 'sale'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idEmployee = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    itensSale =  db.relationship('ItensSaleDb', backref='sale')

    def __init__(self, _idEmployee):
        self.idEmployee = _idEmployee

    def as_dict(self):        
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class ItensSaleDb(db.Model):
    __tablename__ = 'itensSale'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idProduct = db.Column(db.Integer, db.ForeignKey(
       'product.id'), nullable=False)
    idSale =  db.Column(db.Integer, db.ForeignKey(
       'sale.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, _idProduct, _idSale, _quantity):
        self.idProduct = _idProduct
        self.idSale = _idSale
        self.quantity = _quantity

    def as_dict(self):        
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class ProductDb(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    updatedDate = db.Column(db.String(20), nullable=False)
    createdDate = db.Column(db.String(20), nullable=False)
    idSubCategory = db.Column(db.Integer, db.ForeignKey('subCategory.id'), nullable=False)
    itensSale =  db.relationship('ItensSaleDb', backref='product')

    def __init__(self, _description, _status, _updatedDate, _createdDate):
        self.description = _description
        self.status = _status
        self.updatedDate = _updatedDate
        self.createdDate = _createdDate

    def as_dict(self):        
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class SubCategoryDb(db.Model):
    __tablename__ = 'subCategory'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    updatedDate = db.Column(db.String(20), nullable=False)
    createdDate = db.Column(db.String(20), nullable=False)
    idCategory = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    product = db.relationship('ProductDb', backref='subCategory')


    def __init__(self, _description, _status, _updatedDate, _createdDate,_idCategory):
        self.description = _description
        self.status = _status
        self.updatedDate = _updatedDate
        self.createdDate = _createdDate
        self.idCategory = _idCategory

    def as_dict(self):        
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}








