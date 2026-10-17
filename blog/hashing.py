from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes = ['bcrypt'], deprecated = "auto")

class Hash():
    def bcrypt(password : str):
         hass_pass = pwd_cxt.hash(password)
         return hass_pass
    
    def verify(plain_password,hashed_password):
         return pwd_cxt.verify(plain_password, hashed_password)