from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

sqlite_db = {'drivername': 'sqlite', 'database': 'id.sqlite'}
print(URL(**sqlite_db))

db_uri = "sqlite:///id.sqlite"
engine = create_engine(db_uri)

metadata = MetaData(engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, onupdate=uuid.uuid1())
    email = Column(Text, unique=True)
    _password = Column(Text)

    def __init__(self, password=None, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if password:
            self.password = password

    @property
    def password(self):
        raise ValueError("password is write only.")

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value, method='pbkdf2:sha256')

    def verify_password(self, password):
        return check_password_hash(self._password, password)

