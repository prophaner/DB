class MissingEmailAddress(Exception):
    """Raised when Registration class is missing email address"""
    pass


class MissingPassword(Exception):
    """Raised when Registration class is missing password"""
    pass


class InvalidEmailAddress(Exception):
    """Email address is not RFC standard"""
    pass


class InvalidPassword(Exception):
    """Incorrect password format"""
    pass


class EmailExists(Exception):
    """Email already exists in the DB"""
    pass
