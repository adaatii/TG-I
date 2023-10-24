from setting import app
from Src.Router import Router

app.register_blueprint(Router)

if __name__ == '__main__':
    app.run(debug=True)
