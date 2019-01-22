from sqlalchemy.orm import sessionmaker
from DB.schema import *
from DB.helpers import *
import random, string, datetime
import uuid


Session = sessionmaker(bind=engine)
session = Session()


class Registration(object):
    def __init__(self, email=None):
        self.email = email or self.get_random_email()
        self.uuid = str(uuid.uuid4())

    def get_random_email(self):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(6)) + '@random.com'

    def get_new_uuid(self):
        new_uuid = str(uuid.uuid4())
        self.uuid = new_uuid
        return new_uuid

    def add_user(self):
        session.add(User(uuid=self.uuid, email=self.email, password=self.email))
        session.commit()

    def query_user(self, user_email=None):
        if not user_email:
            user_email = self.email

        return session.query(User).filter(User.email == user_email).first()

    def test_name(self, commit=True, **kwargs):
        if not kwargs:
            kwargs = {'uuid': self.uuid,
                      'first_name': random.choice(names),
                      'middle_name': random.choice(names),
                      'last_name': random.choice(last_names),
                      'current': random.choice([True, False])}

        if commit:
            session.add(Name(**kwargs))
            session.commit()

        return kwargs

    def test_email(self, commit=True, **kwargs):
        if not kwargs:
            kwargs = {'uuid': self.uuid,
                      'email': self.get_random_email()}

        if commit:
            session.add(Email(**kwargs))
            session.commit()

        return kwargs

    def test_phone(self, commit=True, **kwargs):
        if not kwargs:
            kwargs = {'uuid': self.uuid,
                      'phone': int(random.random() * 10**9)}

        if commit:
            session.add(Phone(**kwargs))
            session.commit()

        return kwargs

    def test_gender(self, commit=True, **kwargs):
        if not kwargs:
            kwargs = {'uuid': self.uuid,
                      'gender': random.choice(['M', 'F'])}

        if commit:
            session.add(Gender(**kwargs))
            session.commit()

        return kwargs

    def test_dob(self, commit=True, **kwargs):
        year = 2020 - random.choice([_ for _ in range(20, 50)])
        month = random.choice([_ for _ in range(1, 12)])
        day = random.choice([_ for _ in range(1, 28)])
        dob = datetime.datetime.strptime("{} {} {}".format(month, day, year), '%m %d %Y')

        if not kwargs:
            kwargs = {'uuid': self.uuid,
                      'dob': dob}

        if commit:
            session.add(DOB(**kwargs))
            session.commit()

        return kwargs

    def query_uuid(self, user_uuid=None):
        if not user_uuid:
            user_uuid = self.uuid

        all_tables = engine.table_names()

        for table in all_tables:
            q = session.query(Base.metadata.tables[table]).all()

            for row in q:
                for item in row:
                    if item == user_uuid:
                        print("{}\t\t{}".format(table, row))

    def test1(self):
        # Create a new Random User with a new UUID and a random email address
        self.add_user()

        # Add a few tables
        self.test_name()
        self.test_name()
        self.test_dob()
        self.test_email()
        self.test_email()
        self.test_gender()
        self.test_phone()
        self.test_phone()
        self.test_phone()

        self.query_uuid()


a = Registration()
a.test1()
