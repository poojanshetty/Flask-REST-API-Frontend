import requests
import json
from faker import Faker
from api import Customer

fake = Faker(locale='NL')
customer_columns = Customer.__table__.columns.keys()

# Testing GET Request
requests.get('http://127.0.0.1:5000/customers').json()  # Getting list of all customers
requests.get('http://127.0.0.1:5000/customers/1').json()  # Getting customer with id: 1

# Testing DELETE Request
requests.delete('http://127.0.0.1:5000/customers/1').json()  # Deleting customer with id: 20

# Testing POST Request
fake_data = {**fake.profile(), 'phone_number': fake.phone_number()}
fake_data['birthdate'] = str(fake_data['birthdate'])  # Convert datetime to str to serialize birthdate
post_data = {col: fake_data[col] for col in customer_columns if col != 'id'}
requests.post('http://127.0.0.1:5000/customers', data=json.dumps(post_data))  # Insert new customer record

# Testing PUT/PATCH Request
put_data = {'job': 'Software Engineer'}
requests.put('http://127.0.0.1:5000/customers/1', data=json.dumps(put_data))  # Update customer record with id 1
requests.patch('http://127.0.0.1:5000/customers/1', data=json.dumps(put_data))
