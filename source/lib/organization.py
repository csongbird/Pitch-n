class Organization(object):
    """
    This is the class used for organizations
    """
    def __init__(self, name, password, **kwargs):
        self.name = name;
        self.password = password;
        self.location = "";

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_location(self):
        return self.location

    def set_location(self, newLocation):
        self.location = newLocation
    
    def __eq(self, other):
        if type(self) != type(other):
            return False
        elif self.location != other.location:
            return False
        return True

    def __str__(self):
        return self.name

    