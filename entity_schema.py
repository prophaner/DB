from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from DB import helpers

sqlite_db = {'drivername': 'sqlite', 'database': 'id.sqlite'}
print(URL(**sqlite_db))

db_uri = "sqlite:///id.sqlite"
engine = create_engine(db_uri)

metadata = MetaData(engine)
Base = declarative_base()
user_uuid = "Default"


class Name(Base):
    __tablename__ = user_uuid + 'name'

    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    middle_name = Column(Text)
    last_name = Column(Text)
    current = Column(Boolean)  # Is this name current?
    priority = Column(Integer)
    protection = Column(Boolean)
    tags = Column(Text)


class Email(Base):
    __tablename__ = user_uuid + 'email'

    id = Column(Integer, primary_key=True)
    email = Column(Text)
    priority = Column(Integer)  # Priority of the row starting in 0
    protection = Column(Boolean)  # Protected = Hidden and secured
    tags = Column(Text)  # Tags for the Row


class Phone(Base):
    __tablename__ = user_uuid + 'phone'

    id = Column(Integer, primary_key=True)
    phone = Column(Text, unique=True)  # Phone Number stored in Text
    priority = Column(Integer)  # Priority of the row starting in 0
    protection = Column(Boolean)  # Protected = Hidden and secured
    tags = Column(Text)  # Tags for the Row


class Gender(Base):
    __tablename__ = user_uuid + 'gender'

    id = Column(Integer, primary_key=True)
    gender = Column(Text)
    protection = Column(Boolean)
    tags = Column(Text)


class DOB(Base):
    __tablename__ = user_uuid + 'dob'

    id = Column(Integer, primary_key=True)
    dob = Column(Date)
    protection = Column(Boolean)
    tags = Column(Text)


class Height(Base):
    __tablename__ = user_uuid + 'height'

    id = Column(Integer, primary_key=True)
    height_ft = Column(Integer)
    height_in = Column(Integer)
    height_date = Column(Date)
    priority = Column(Integer)
    protection = Column(Boolean)
    tags = Column(Text)


class Weight(Base):
    __tablename__ = user_uuid + 'weight'

    id = Column(Integer, primary_key=True)
    pounds = Column(Text)
    date = Column(Date)
    priority = Column(Integer)
    protection = Column(Boolean)
    tags = Column(Text)


class Eyes(Base):
    __tablename__ = user_uuid + 'eyes'

    id = Column(Integer, primary_key=True)
    color = Column(Text)
    date = Column(Date)
    protection = Column(Boolean)
    tags = Column(Text)


class Hair(Base):
    __tablename__ = user_uuid + 'hair'

    id = Column(Integer, primary_key=True)
    color = Column(Text)
    date = Column(Date)
    protection = Column(Boolean)
    tags = Column(Text)


class Address(Base):
    __tablename__ = user_uuid + 'address'

    id = Column(Integer, primary_key=True)
    address_text = Column(Text)  # Full text for the address
    address_number = Column(Text)
    address_street = Column(Text)
    address_district = Column(Text)
    address_county = Column(Text)
    address_postal = Column(Text)
    address_country = Column(Text)
    address_coordinates_lat = Column(Text)
    address_coordinates_lon = Column(Text)
    checked = Column(Boolean)  # Checked with an address database like Google
    converted = Column(Boolean)  # Checked if address has been converted from Text to Parse mode
    residence_type = helpers.ResidenceTypes  # Own, Rent, Sublet, Lodge
    residence_use = helpers.ResidenceUse  # NONE, primary residence, rental, unused << If residence_type == Own
    priority = Column(Integer)
    protection = Column(Boolean)
    tags = Column(Text)


class SSN(Base):
    __tablename__ = user_uuid + 'ssn'

    id = Column(Integer, primary_key=True)
    ssn = Column(Text)  # SSN
    name = Column(Text)  # Points at the Name Table. Create a new one if not there
    image = Column(Text)  # Upload a new picture
    protection = Column(Boolean)
    tags = Column(Text)


class DL(Base):
    __tablename__ = user_uuid + 'dl'

    id = Column(Integer, primary_key=True)
    dln = Column(Text)								# DL number
    state = helpers.State
    dl_class = Column(Text)							# DL class
    name = Column(Text)  # Points at the Name Table. Create a new one if not there
    address = Column(Text)  # Points at the Address Table. Create a new one if not there
    dob = Column(Text)  # Points at the DOB Table. Create a new one if not there
    hair = Column(Text)  # Points at the hair Table. Create a new one if not there
    eyes = Column(Text)  # Points at the eyes Table. Create a new one if not there
    weight = Column(Text)  # Points at the weight Table. Create a new one if not there
    sex = Column(Text)  # Points at the gender Table. Create a new one if not there
    issued = Column(Date)
    expires = Column(Date)
    rest = Column(Text)
    endorse = Column(Text)
    replaced = Column(Date)
    image = Column(Text)
    converted = Column(Boolean)						# Checked if ID has been converted from image to Parse mode
    priority = Column(Integer)
    protection = Column(Boolean)
    tags = Column(Text)


class Vehicle(Base):
    __tablename__ = user_uuid + 'vehicle'

    id = Column(Integer, primary_key=True)
    registration = Column(Text)  # Points at the registration Table. Create a new one if not there
    title = Column(Text)  # Points at the title Table. Create a new one if not there
    plate = Column(Text)  # Points at the plate Table. Create a new one if not there
    priority = Column(Integer)
    protection = Column(Boolean)
    tags = Column(Text)
