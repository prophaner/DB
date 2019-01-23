from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer, Text, Boolean, Date, Sequence
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine

engine = create_engine("sqlite:///id.sqlite")

metadata = MetaData(engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_seq'), primary_key=True)
    uuid = Column(Text, unique=True, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    _password = Column(Text, nullable=False)

    registered = Column(Boolean, nullable=False)
    expiration = Column(Date, nullable=False)
    token = Column(Text)

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


class Name(Base):
    __tablename__ = 'name'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    uuid = Column(Text, nullable=False)
    first_name = Column(Text)
    middle_name = Column(Text)
    last_name = Column(Text)
    current = Column(Boolean)  # Is this name current?
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    email = Column(Text)
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)  # Protected = Hidden and secured
    tags = Column(Text)  # Tags for the Row


class Phone(Base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    phone = Column(Text, unique=True)  # Phone Number stored in Text
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)  # Protected = Hidden and secured
    tags = Column(Text)  # Tags for the Row


class Gender(Base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    gender = Column(Text)
    protection = Column(Boolean)
    tags = Column(Text)


class DOB(Base):
    __tablename__ = 'dob'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    dob = Column(Date)
    protection = Column(Boolean)
    tags = Column(Text)


class Height(Base):
    __tablename__ = 'height'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    height_ft = Column(Integer)
    height_in = Column(Integer)
    height_date = Column(Date)
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


class Weight(Base):
    __tablename__ = 'weight'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    pounds = Column(Text)
    date = Column(Date)
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


class Eyes(Base):
    __tablename__ = 'eyes'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    color = Column(Text)
    date = Column(Date)
    protection = Column(Boolean)
    tags = Column(Text)


class Hair(Base):
    __tablename__ = 'hair'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    color = Column(Text)
    date = Column(Date)
    protection = Column(Boolean)
    tags = Column(Text)


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
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
    residence_type = Column(Text)  # Own, Rent, Sublet, Lodge
    residence_use = Column(Text)  # NONE, primary residence, rental, unused << If residence_type == Own
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


class SSN(Base):
    __tablename__ = 'ssn'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    ssn = Column(Text)  # SSN
    name = Column(Text)  # Points at the Name Table. Create a new one if not there
    image = Column(Text)  # Upload a new picture
    protection = Column(Boolean)
    tags = Column(Text)


class DL(Base):
    __tablename__ = 'dl'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    dln = Column(Text)								# DL number
    ssn = Column(Text)  # Points at the SSN Table. Create a new one if not there
    state = Column(Text)
    dl_class = Column(Text)							# DL class
    name = Column(Text)  # Points at the Name Table. Create a new one if not there
    address = Column(Text)  # Points at the Address Table. Create a new one if not there
    dob = Column(Text)  # Points at the DOB Table. Create a new one if not there
    hair = Column(Text)  # Points at the hair Table. Create a new one if not there
    eyes = Column(Text)  # Points at the eyes Table. Create a new one if not there
    height = Column(Text)  # Points at the height Table. Create a new one if not there
    weight = Column(Text)  # Points at the weight Table. Create a new one if not there
    sex = Column(Text)  # Points at the gender Table. Create a new one if not there
    duplicates = Column(Integer)
    medical = Column(Text)
    organ_donor = Column(Text)
    non_resident = Column(Text)
    issued = Column(Date)
    expires = Column(Date)
    restriction = Column(Text)
    endorse = Column(Text)
    replaced = Column(Date)
    document_discriminator = Column(Text)
    image = Column(Text)
    converted = Column(Boolean)						# Checked if ID has been converted from image to Parse mode
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    registration = Column(Text)  # Points at the registration Table. Create a new one if not there
    title = Column(Text)  # Points at the title Table. Create a new one if not there
    plate = Column(Text)  # Points at the plate Table. Create a new one if not there
    ownership_type = Column(Text)  # Lease, Own, Rent
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


class VehicleTitle(Base):
    __tablename__ = 'vehicle_title'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    title_number = Column(Text)  # Points at the registration Table. Create a new one if not there
    vin_number = Column(Text)
    year = Column(Text)  # Points at the title Table. Create a new one if not there
    make = Column(Text)  # Points at the plate Table. Create a new one if not there
    model = Column(Text)
    body = Column(Text)
    document_number = Column(Text)
    color = Column(Text)
    weight = Column(Text)
    fuel = Column(Text)
    cylinders = Column(Text)
    new = Column(Boolean)
    used = Column(Boolean)
    demo = Column(Boolean)
    title_type = Column(Text)
    issued_date = Column(Date)
    purchase_date = Column(Date)
    liens = Column(Text)
    odometer = Column(Text)
    list_price = Column(Text)
    owner_name = Column(Text)  # Points at the Name Table and the OtherNames Table, stores them in a List
    owner_address = Column(Text)  # Points at the Address Table and the OtherAddress Table, stores them in a List
    image = Column(Text)
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


class VehicleRegistration(Base):
    __tablename__ = 'vehicle_registration'

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False)
    mailing_address = Column(Text)
    plate = Column(Text)
    decal = Column(Text)
    expires = Column(Text)
    year = Column(Text)
    make = Column(Text)
    body = Column(Text)
    color = Column(Text)
    tax_month = Column(Text)
    vin = Column(Text)
    plate_type = Column(Text)
    net_weight = Column(Text)
    dln = Column(Text)
    issued_date = Column(Text)
    issued_plate = Column(Text)
    image = Column(Text)
    priority = Column(Integer, unique=True)
    protection = Column(Boolean)
    tags = Column(Text)


Base.metadata.create_all(engine)
