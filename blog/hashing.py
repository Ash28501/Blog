from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes = ['bcrypt'], deprecated = "auto")

class Hash():
    def bcrypt(password : str):
         hass_pass = pwd_cxt.hash(password)
         return hass_pass