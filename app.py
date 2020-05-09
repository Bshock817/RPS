from flask import Flask, render_template, request, session, flash, json, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RPS.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = 'RPS'


@app.route('/')
def main():
    return render_template('main.html')





if __name__ == "__main__":
    app.run(debug=True)
