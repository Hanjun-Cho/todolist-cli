from flask import Flask, request
from flask_mysqldb import MySQL
from database import initialize_database
import secret

# creates flask application and sets up database configurations
def create_app(testing):
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = secret.MYSQL_HOST
    app.config['MYSQL_USER'] = secret.MYSQL_USER
    app.config['MYSQL_PASSWORD'] = secret.MYSQL_PASSWORD
    app.config['MYSQL_DB'] = secret.MYSQL_DB
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.config['TESTING'] = testing
    app.config['TASK_TABLE'] = "tasks" if not testing else "test_tasks"
    db = MySQL(app)
    app.db = db
    with app.app_context():
        initialize_database()
        from views.api import api
        app.register_blueprint(api)
    return app

if __name__ in "__main__":
    create_app(testing=False)
