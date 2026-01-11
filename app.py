from flask import Flask, render_template,request,flash,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set a secret key
app.secret_key = "jatin"   # ANY STRING

db = SQLAlchemy(app)


# create database schema using python classes
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):    # whenever you will print the todo object
                           # information you want to see.
        return f"{self.sno} - {self.title}"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.email}"


@app.route('/')
def about():
    return render_template('/about.html')

@app.route('/index',methods=['GET','POST','DELETE'])
def createAndRead():
    if request.method == 'POST':   # create
        title = request.values['title']
        description = request.values['description']

        if not title and not description:
            flash("Missing Title and Description","warning")
            return redirect('/index')
        elif not title:
            flash("Missing Title","warning")
            return redirect('/index')
        elif not description:
            flash("Missing Description","warning")
            return redirect('/index')


        test = Todo(title=title, description=description)
        db.session.add(test)
        db.session.commit()
        if test:
            flash("Todo Created Successfully!", "success")
            return redirect('/index')

    allTodo = Todo.query.all()   # read
    return render_template("index.html", allTodo = allTodo)

@app.route("/update/<int:sno>",methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title = request.values['title']
        description = request.values['description']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.description = description
        db.session.add(todo)
        db.session.commit()
        if todo:
            flash("Todo Updated Successfully!", "success")
            return redirect('/index')
        return redirect('/index')

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('/update.html',todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    if todo:
        flash("Todo Deleted Successfully!", "danger")
        return redirect('/index')
    return redirect('/index')


@app.route('/users/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and email == user.email and password == user.password:
            session['email'] = email
            flash("Login Successful!", "success")
            return redirect('/index')
        elif not email and  not password:
            flash("Missing Email and Password","warning")
            return redirect('/users/login')
        elif not email:
            flash("Missing Email","warning")
            return redirect('/users/login')
        elif not password:
            flash("Missing Password","warning")
            return redirect('/users/login')
        else:
            flash("The email and password you entered did not match our records. Please double-check and "
                  "try again", "danger")
            return redirect('/users/login')

    return render_template('/login.html')

@app.route('/users/create', methods=[ 'GET', 'POST', 'DELETE'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User(name=name, email=email,password=password)
        db.session.add(user)
        db.session.commit()

        if not name and not email and  not password:
            flash("Missing Name, Email and Password","warning")
            return redirect('/users/create')
        elif not name:
            flash("Missing Name","warning")
            return redirect('/users/create')
        elif not email:
            flash("Missing Email","warning")
            return redirect('/users/create')
        elif not password:
            flash("Missing Password","warning")
            return redirect('/users/create')

        flash("User Created Successfully!","success")
        return redirect('/users/login')
    return render_template('/signup.html')


@app.route('/logout')
def logout():
    if session.pop('email', None):
        flash("Logged out Successfully!", "success")
        redirect('/users/login')
    return redirect('/users/login')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # This block creates the empty todo.db and tables if they don't exist
    app.run(host='0.0.0.0', port=5000)


# To create this database just use below commands in python interpreter.
# from app import db
# app.app_context().push()
# db.create_all()


# https://inloop.github.io/sqlite-viewer/