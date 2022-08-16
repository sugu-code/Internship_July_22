import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import pyshorteners

main_url=""
shorter=""

app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'mykey'

db=SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class URL(db.Model):
    __tablename__='url_short'
    id=db.Column(db.Integer, primary_key=True)
    main_url=db.Column(db.String(200))
    shorter=db.Column(db.String(200))
    def __init__(self,main_url,shorter):
        self.main_url=main_url
        self.shorter=shorter

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) 

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = User(email=request.form.get('email'),
                    password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Grab the user from our User Models table
        user = User.query.filter_by(email=request.form.get('email')).first()

        # Check that the user was supplied and the password is right
        # The check_password method comes from the User object
        if user is not None and user.check_password(request.form.get('password')):

            #Log in the user
            login_user(user)

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('index')

            return redirect(next)
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))  

@app.before_first_request
@login_required
def create_tables():
    db.create_all()

@app.route('/add',methods=["GET","POST"])
@login_required
def add():
    global main_url,shorter
    if request.method=="POST":
        main_url=request.form.get("in_1")
        url_short = pyshorteners.Shortener()
        shorter = url_short.tinyurl.short(main_url)
        new_URL=URL(main_url,shorter)
        db.session.add(new_URL)
        db.session.commit()
    return render_template("add.html", shorter=shorter)

@app.route('/display')
@login_required
def display_function():
    url_shorter=db.session.execute("select * from url_short")
    return render_template("display.html",url_shorter=url_shorter)


if __name__=='__main__':
    app.run(debug=True)