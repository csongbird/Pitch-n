class User(object):
    """
    This is the user class used for individuals
    """
    def __init__(self, name, password, **kwargs):
        self.username = name;
        self.password = password;
        self.favorites = []

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_fav(self):
        return self.favorites

    def add_to_fav(self, org):
        self.favorites.append(org)

    def remove_from_fav(self, org):
        self.favorites.remove(org)
    
    def __eq(self, other):
        if type(self) != type(other):
            return False
        elif self.username != other.username:
            return False
        return True

    def __str__(self):
        return self.username

    