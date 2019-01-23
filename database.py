from sqlalchemy.orm import sessionmaker, scoped_session
from schema import *
from exceptions import *
from helpers import *
import random, string, datetime, re
import uuid


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


class Registration(object):
    def __init__(self, email=None, password=None):
        """
        :param email: email address from user. Should be unique
        """
        self.email = email
        self.uuid = str(uuid.uuid4())
        self.password = password

    def pre_checks(self):
        if not self.email:
            raise MissingEmailAddress("Include email address")

        if len(self.email) > 7:
            raise InvalidEmailAddress("Incorrect email format")

        if re.match("^.+@([?)[a-zA-Z0-9-.])+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", self.email) is None:
            raise InvalidEmailAddress("Incorrect email format")

        if not self.password:
            raise MissingPassword("Include password")

        if len(self.password) < 8:
            raise InvalidPassword("Make sure your password is at lest 8 letters")

        if re.search('[0-9]', self.password) is None:
            raise InvalidPassword("Make sure your password has a number in it")

        if re.search('[A-Z]', self.password) is None:
            raise InvalidPassword("Make sure your password has a capital letter in it")

        if db_session.query(User).filter(User.email == self.email).first():
            raise EmailExists("Email already exists in the DB")

    def add_user(self):
        self.pre_checks()

        registration_token = str(uuid.uuid4())
        db_session.add(User(uuid=self.uuid,
                            email=self.email,
                            password=self.email,
                            registered=False,
                            expiration=registration_expiration(),
                            token=registration_token))

        db_session.commit()
        # TODO: Add DB hooks to check if data has been committed

        print(send_email(self.email, registration_token))  # Send registration email with token. Print if error
        # TODO: Add an Exeption Handler. If invalid email, if server error.
