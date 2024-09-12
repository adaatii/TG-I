# TG-I flask-react-app 

In every application there is a control of employees and categories involved in the process.

In this project an API was developed that allows querying, creating and editing this information, about employee and category.

## Libraries and Tools

### Backend

* 🐍 [Python](https://www.python.org/)
* 🧪 [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* 🧪 [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/)
* ⚗️ [SQLAlchemy (Object Relational Mapper - ORM)](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
* 🚧 [Pytest (for testing)](https://docs.pytest.org/en/7.3.x/)

### Frontend

* ⚛️ [React](https://react.dev/)
* 🛣️ [React Router](https://reactrouter.com/en/main)
* 💅 [Material UI](https://mui.com/)
* 🛜 [Axios](https://axios-http.com/)
* ⚡️ [Vite](https://vitejs.dev/)
* ⚒️ [ESLint](https://eslint.org/)
* ✨ [Prettier](https://prettier.io/)

## Project Organization

### Backend

The API was designed using the Model-View-Controller (MVC) pattern:

#### View (Directory that contains the classes for the project activities)

* They have the entity name and the suffix 'View'
* [CategoryView](Backend/Src/View/CategoryView.py) and [EmployeeView](Backend/Src/View/EmployeeView.py)

#### Controller (Action methods)

* They have no prefixes or suffixes
* [Category](Backend/Src/Controller/Category.py) and [Employee](Backend/Src/Controller/Employee.py)

#### Model (The logical structure of a database)

* There is only one database file that is responsible for managing the database of both entities
* [DataBase](Backend/Src/Model/DataBase.py)

### Frontend

#### Routes

To list, the pattern used was the name of the category with the first capital letter and the suffix "List", [CategoryList](Frontend/src/routes/CategoryList.tsx).

To create and update, the pattern used was the name of the category with the first capital letter and the suffix "Form", [CategoryForm](Frontend/src/routes/CategoryForm.tsx).

The Home screen has a path to the functionalities of the Category and Employee entities, in the [Home](Frontend/src/routes/Home.tsx) component.

#### Types

* There is only one type file that that contains the types of the entities.
* [types](Frontend/src/types/types.ts)

## Project Setup

### Backend

First, create a virtual env to host the project dependencies.
Install the necessary dependencies with the following commands:

Linux:

```bash
cd Backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
cd Backend
python3 -m venv .venv
env\Scripts\activate.bat
pip install -r requirements.txt
```

Then, initialize the API server:

```bash
python main.py
```

To run the tests:

```bash
pytest -v
```

> [!NOTE]
> You must first create the database. The database information is at the end of the file.

### Frontend

Previously, nodejs has to be installed.
Then, install the necessary dependencies with the following commands:

```bash
cd Frontend
npm install
```

Then, initialize the dev server:

```bash
npm run dev
```

## MariaDB Configuration with Docker Compose

Start the container with:

bash

MARIADB_ROOT_PASSWORD="your_password" docker compose up

> [!NOTE]
> You can start and daemonize it immediately by passing the -d flag. In this case, you will need to stop the container using Docker Desktop or docker stop {container}.

To create the database, you need to execute an SQL script. You can use tools like DBeaver or any other SQL IDE for this purpose. Simply connect to your MariaDB instance and run the provided SQL script to set up the database schema. You can find the Script in [SQLScript](https://github.com/adaatii/flask-react-app/blob/main/Database/panteao.sql).
## Navigate the project

* [Backend](https://github.com/adaatii/flask-react-app/tree/main/Backend/Src)
* [Frontend](https://github.com/adaatii/flask-react-app/tree/main/Frontend)
* [Tests](https://github.com/adaatii/flask-react-app/tree/main/Backend/tests)
* [DataBase](https://github.com/adaatii/flask-react-app/tree/main/Database/)
