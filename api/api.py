import json
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from settings import database_name


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_name}'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    birthdate = db.Column(db.String(10))
    sex = db.Column(db.String(1))
    ssn = db.Column(db.String(12), unique=True)
    mail = db.Column(db.String(120))
    phone_number = db.Column(db.String(15))
    address = db.Column(db.String(250))
    residence = db.Column(db.String(250))
    job = db.Column(db.String(200))
    company = db.Column(db.String(150))

    def __repr__(self):
        return f'Customer: {self.name, self.birthdate, self.sex, self.phone_number}'


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    output = []
    for customer in customers:
        customer_data = {
            'id': customer.id,
            'name': customer.name,
            'birthdate': customer.birthdate,
            'sex': customer.sex,
            'ssn': customer.ssn,
            'mail': customer.mail,
            'phone_number': customer.phone_number,
            'address': customer.address,
            'residence': customer.residence,
            'job': customer.job,
            'company': customer.company,
        }
        output.append(customer_data)
    return {'data': output}


@app.route('/customers/<cust_id>', methods=['GET'])
def get_customer(cust_id):
    if Customer.query.get(cust_id):
        customer = Customer.query.get(cust_id)
        return {
            'id': customer.id,
            'name': customer.name,
            'birthdate': customer.birthdate,
            'sex': customer.sex,
            'ssn': customer.ssn,
            'mail': customer.mail,
            'phone_number': customer.phone_number,
            'address': customer.address,
            'residence': customer.residence,
            'job': customer.job,
            'company': customer.company,
        }
    else:
        return {'error': f'Customer with id: {cust_id} not present in the database'}


@app.route('/customers', methods=['POST'])
def add_customer():
    data = json.loads(request.get_data())
    if not data.get('name'):
        return {'error': 'Name is a required field'}, 404
    customer = Customer(
        name=data.get('name'),
        birthdate=data.get('birthdate', ''),
        sex=data.get('sex', ''),
        ssn=data.get('ssn', ''),
        mail=data.get('mail'),
        phone_number=data.get('phone_number', ''),
        address=data.get('address', ''),
        residence=data.get('residence', ''),
        job=data.get('job', ''),
        company=data.get('company', ''),
    )
    db.session.add(customer)
    db.session.commit()
    return {'id': customer.id}, 201  # 201 status code -> 'Created'


@app.route('/customers/<cust_id>', methods=['DELETE'])
def delete_customer(cust_id):
    customer = Customer.query.get(cust_id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return {'success': f'Customer with id: {cust_id} is deleted from the database'}
    else:
        return {'error': f'Customer with id: {cust_id} is not present in the database'}, 404


@app.route('/customers/<cust_id>', methods=['PUT', 'PATCH'])
def update_customer(cust_id):
    customer = Customer.query.get(cust_id)
    if customer:
        data = json.loads(request.get_data())
        if 'name' in data.keys() and not data['name']:
            return {'error': 'Name is a required field'}, 404
        customer_columns = Customer.__table__.columns.keys()
        for key, value in data.items():
            if key != 'id' and key in customer_columns:
                Customer.query.filter_by(id=cust_id).update({key: value})
        db.session.commit()
        return {'success': f'Customer with id: {cust_id} has been updated in the database'}
    else:
        return {'error': f' Customer with id: {cust_id} not present in the database'}, 404


if __name__ == '__main__':
    app.run(debug=True)
