import os
from faker import Faker
from api import db, Customer
from settings import database_name, number_of_records

fake = Faker(locale='NL')


def create_database():
    db.create_all()


def add_records_to_database(n):
    for i in range(n):
        fake_data = {
            **fake.profile(),
            'phone_number': fake.phone_number(),
        }
        fake_data['birthdate'] = str(fake_data['birthdate'])  # Convert datetime to str to jsonify birthdate
        db.session.add(Customer(
            name=fake_data['name'],
            birthdate=fake_data['birthdate'],
            sex=fake_data['sex'],
            ssn=fake_data['ssn'],
            mail=fake_data['mail'],
            phone_number=fake_data['phone_number'],
            address=fake_data['address'],
            residence=fake_data['residence'],
            job=fake_data['job'],
            company=fake_data['company'],
        ))
    db.session.commit()


if __name__ == '__main__':
    if database_name not in os.listdir():
        create_database()
        add_records_to_database(number_of_records)
