import requests
import random

ENDPOINT = "http://127.0.0.1:5000"

# region Category
def test_can_call_the_endpoint_categories():
    response = requests.get(f"{ENDPOINT}/categories/")
    first_category = response.json()['categories'][0]
    expected_result = {
        "id": 1,
        "description": 'COMIDA',
        "status": 1,
        "updatedDate": '04/07/2023 07:48:13',
        "createdDate": '27/06/2023 13:39:33'
    }
    assert response.status_code == 200
    assert first_category == expected_result



def test_can_create_category():
    payload = {
        "description": f"Teste {random.randint(1,10000)}",
        "status": True,
    }
    response = requests.post(f"{ENDPOINT}/categories/", json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_create_category_conflict():
    payload = {
        "description": "SALGADO",
        "status": True,
    }
    response = requests.post(f"{ENDPOINT}/categories/", json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'Category already exists'}


def test_can_create_category_badRquest():
    payload = {
        "description": "",
        "status": True,
    }
    response = requests.post(f"{ENDPOINT}/categories/", json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}


def test_can_update_category():
    payload = {
        "description": "TESTE DE UPDATE",
        "status": False,
    }
    response = requests.put(f"{ENDPOINT}/categories/3", json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_update_category_conflict():
    payload = {
        "description": "SALGADO",
        "status": True,
    }
    response = requests.put(f"{ENDPOINT}/categories/1", json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'Category already exists'}


def test_can_update_category_badRquest():
    payload = {
        "description": "",
        "status": True,
    }
    response = requests.put(f"{ENDPOINT}/categories/19", json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}

# endregion

# region SubCategory

def test_can_call_the_endpoint_subCategories():
    response = requests.get(f"{ENDPOINT}/subCategories/")
    first_subCategory = response.json()['subCategories'][0]
    expected_result = {
        "id": 1,
        "description": 'DRINKS',
        "status": 1,
        "updatedDate": '24/10/2023 21:46:48',
        "createdDate": '24/10/2023 21:46:48',
        "idCategory": 1
    }
    assert response.status_code == 200
    assert first_subCategory == expected_result

def test_can_create_subCategory():
    payload = {
        "description": f"Teste {random.randint(1,10000)}",
        "status": True,
        "idCategory": 1
    }
    response = requests.post(f"{ENDPOINT}/subCategories/", json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_create_subCategory_conflict():
    payload = {
        "description": "CAFÉ",
        "status": True,
        "idCategory": 1
    }
    response = requests.post(f"{ENDPOINT}/subCategories/", json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'Category already exists'}


def test_can_create_subCategory_badRquest():
    payload = {
        "description": "",
        "status": True,
        "idCategory": 2
    }
    response = requests.post(f"{ENDPOINT}/subCategories/", json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}


def test_can_update_subCategory():
    payload = {
        "description": "TESTE DE UPDATE",
        "status": False,
        "idCategory": 1
    }
    response = requests.put(f"{ENDPOINT}/subCategories/5", json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_update_subCategory_conflict():
    payload = {
        "description": "CAFÉ",
        "status": True,
        "idCategory": 1
    }
    response = requests.put(f"{ENDPOINT}/subCategories/9", json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'SubCategory already exists'}


def test_can_update_subCategory_badRquest():
    payload = {
        "description": "",
        "status": True,
        "idCategory": 1
    }
    response = requests.put(f"{ENDPOINT}/subCategories/1", json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}


# endregion

# region Employee
def test_can_call_the_endpoint_employee():
    response = requests.get(f"{ENDPOINT}/employees/")
    first_employee = response.json()['employees'][0]
    expected_result = {
        "id": 1,
        "name": 'ESTRELA',
        "cpf": '65743244432',
        "email": "ESTRELA@GMAIL.COM",
        "passwd": "123",
        "status": 0,
        "updatedDate": '24/10/2023 16:50:19',
        "createdDate": '28/06/2023 08:31:46'
    }
    assert response.status_code == 200
    assert first_employee == expected_result

def test_can_create_employee():
    rand = random.randint(1, 10000)
    payload = {
        "name": f"Nome {rand}",
        "cpf":f"{rand}",
        "email": f"nome{rand}@gmail.com",
        "passwd": f"{rand}",
        "status": True
    }
    response = requests.post(f"{ENDPOINT}/employees/", json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_create_employee_conflict():
    payload = {
        "name": "Estrela",
        "cpf": "65743244432",
        "passwd": "123",
        "email": "estrela@gmail.com",
        "status": True
    }
    response = requests.post(f"{ENDPOINT}/employees/", json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'Employee already exists'}


def test_can_create_employee_badRquest():
    payload = {
        "name": "",
        "cpf": "65743244432",
        "passwd": "123",
        "email": "estrela@gmail.com",
        "status": True
    }
    response = requests.post(f"{ENDPOINT}/employees/", json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}


def test_can_update_employee():
    payload = {
        "name": "New Name",
        "cpf": "1111111",
        "passwd": "123",
        "email": "newemail@gmail.com",
        "status": False
    }
    response = requests.put(f"{ENDPOINT}/employees/2",json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_update_employee_conflict():
    payload = {
        "name": "Estrela",
        "cpf": "65743244432",
        "passwd": "123",
        "email": "estrela@gmail.com",
        "status": True
    }
    response = requests.put(f"{ENDPOINT}/employees/3",json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'Category already exists'}


def test_can_update_employee_badRquest():
    payload = {
        "name": "",
        "cpf": "65743244432",
        "passwd": "123",
        "email": "estrela@gmail.com",
        "status": True
    }
    response = requests.put(f"{ENDPOINT}/employees/2",json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}

# endregion

# region Product
def test_can_call_the_endpoint_product():
    response = requests.get(f"{ENDPOINT}/products/")
    first_product = response.json()['products'][0]
    expected_result = {
        "id": 1,
        "description": 'PRODUCT 6404',
        "price": 640,
        "updatedDate": '25/10/2023 20:52:29',
        "createdDate": '25/10/2023 20:52:29',
        "idSubCategory":1,
        "status": 1,

    }
    assert response.status_code == 200
    assert first_product == expected_result

def test_can_create_product():
    rand = random.randint(1, 10000)
    payload = {
        "description": f"Product {rand}",
        "price":f"{rand}",
        "idSubCategory": 1,
        "status": True
    }
    response = requests.post(f"{ENDPOINT}/products/", json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_create_product_conflict():
    payload = {
        "description": f"PRODUCT 907",
        "price": 907,
        "idSubCategory": 1,
        "status": True
    }
    response = requests.post(f"{ENDPOINT}/products/", json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'Product already exists'}


def test_can_create_product_badRquest():
    payload = {
        "description": "",
        "price": 907,
        "idSubCategory": 1,
        "status": True    
    }
    response = requests.post(f"{ENDPOINT}/products/", json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}


def test_can_update_product():
    payload = {
        "description": f"PRODUCT 907",
        "price": 907,
        "idSubCategory": 2,
        "status": False   
    }
    response = requests.put(f"{ENDPOINT}/products/2",json=payload)
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_can_update_product_conflict():
    payload = {
        "description": f"PRODUCT 907",
        "price": 907,
        "idSubCategory": 2,
        "status": False 
    }
    response = requests.put(f"{ENDPOINT}/products/3",json=payload)
    assert response.status_code == 409
    assert response.json() == {'status': 'error',
                               'message': 'Category already exists'}


def test_can_update_product_badRquest():
    payload = {
        "description": "",
        "price": 907,
        "idSubCategory": 2,
        "status": False 
    }
    response = requests.put(f"{ENDPOINT}/products/2",json=payload)
    assert response.status_code == 400
    assert response.json() == {'status': 'error',
                               'message': 'Fill all of the fields'}

# endregion
