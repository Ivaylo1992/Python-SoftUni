import re


class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15 :
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        pattern = r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(pattern, value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return (f'You have a profile with username: "{self.username}" '
                f'and password: {"*" * len(self.password)}')


profile_with_invalid_username = Profile('Too_long_username', 'Any')