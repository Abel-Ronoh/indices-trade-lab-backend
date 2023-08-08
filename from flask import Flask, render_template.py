from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class InvestmentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hourly_profit = db.Column(db.Float, nullable=False)
    min_deposit = db.Column(db.Float, nullable=False)
    max_deposit = db.Column(db.Float, nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('investment_plan.id'), nullable=False)
    deposit_amount = db.Column(db.Float, nullable=False)
    withdrawal_amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=db.func.now())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return 'User registered successfully'

    return render_template('register.html')

@app.route('/investments')
def investments():
    plans = InvestmentPlan.query.all()
    return render_template('investments.html', plans=plans)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        user_id = request.form['user_id']
        plan_id = request.form['plan_id']
        deposit_amount = request.form['deposit_amount']

        transaction = Transaction(user_id=user_id, plan_id=plan_id, deposit_amount=deposit_amount)
        db.session.add(transaction)
        db.session.commit()

        return 'Deposit made successfully'

    return render_template('deposit.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)