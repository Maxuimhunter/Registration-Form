from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
runner = Flask(__name__)

# MySQL configuration for XAMPP
runner.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:NewPassword@localhost/test_db'
runner.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(runner)

# Define the model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100))
    family_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    age = db.Column(db.Numeric)
    gender = db.Column(db.String(10), nullable=False)
    date_tested = db.Column(db.Date, nullable=False)
    hiv_status = db.Column(db.String(10), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# Drop the existing table and create a new one
with runner.app_context():
    db.drop_all()
    db.create_all()

# Routes
@runner.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        first_name = request.form['first-name']
        second_name = request.form['second-name']
        family_name = request.form['family-name']
        dob = request.form['dob']
        age = request.form['age']
        gender = request.form['gender']
        date_tested = request.form['date-tested']
        hiv_status = request.form['hiv-status']
        
        new_task = Todo(
            first_name=first_name,
            second_name=second_name,
            family_name=family_name,
            dob=datetime.strptime(dob, '%Y-%m-%d').date(),
            age=age,
            gender=gender,
            date_tested=datetime.strptime(date_tested, '%Y-%m-%d').date(),
            hiv_status=hiv_status
        )

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'There was an issue adding your task: {e}'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@runner.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f'There was a problem deleting that task: {e}'
    
@runner.route('/viewing/<int:id>', methods=['GET', 'POST'])
def viewing(id):
    print(f"Request received for id: {id}")  # Debug statement
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        print("Processing POST request")  # Debug statement
        task.first_name = request.form['first-name']
        task.second_name = request.form['second-name']
        task.family_name = request.form['family-name']
        task.dob = datetime.strptime(request.form['dob'], '%Y-%m-%d').date()
        task.age = request.form['age']
        task.gender = request.form['gender']
        task.date_tested = datetime.strptime(request.form['date-tested'], '%Y-%m-%d').date()
        task.hiv_status = request.form['hiv-status']

        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'There was an issue updating your task: {e}'

    else:
        return render_template('viewing.html', task=task)

# Run the app
if __name__ == "__main__":
    runner.run(debug=True)
