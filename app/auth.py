
from passlib.context import CryptContext

# Contexto para o hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para verificar se a senha corresponde ao hash
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para gerar um hash para a senha
def get_password_hash(password):
    return pwd_context.hash(password)
