import jwl
import time

# 1. Configuração inicial
# Chave secreta usada para assinar os tokens
secret_key = 'sua_chave_secreta'
# Tempo padrão de validade dos tokens em minutos
default_expiration_minutes = 30

# 2. Módulo de Geração de Tokens
def generate_jwt(user_id, secret_key, expiration_minutes=default_expiration_minutes):
    # Calcula o tempo de expiração do token
    expiration_time = int(time.time()) + (expiration_minutes * 60)
    # Cria o payload com user_id e exp
    payload = {
        'user_id': user_id,
        'exp': expiration_time
    }
    # Assina e codifica o payload em um token JWT
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

# 3. Módulo de Validação de Tokens
def validate_jwt(received_token, secret_key):
    try:
        # Decodifica o token usando a chave secreta
        payload = jwt.decode(received_token, secret_key, algorithms=['HS256'])
        user_id = payload['user_id']
        # Se tudo estiver correto, retorna que o token é válido e o user_id
        return True, user_id
    except jwt.ExpiredSignatureError:
        return False, "Token expirado."
    except jwt.InvalidTokenError:
        return False, "Token inválido."

# 4. Testes
if __name__ == "__main__":
    # Teste de geração de token
    user_id = '12345'
    token = generate_jwt(user_id, secret_key)
    print(f'Token gerado: {token}')

    # Teste de validação de token
    is_valid, result = validate_jwt(token, secret_key)
    print(f'Token válido: {is_valid}, Resultado: {result}')

    # Teste de validação com token expirado
    # Aguarda um tempo para simular expiração, se necessário
    time.sleep(2)  # Ajuste se necessário
    expired_token = generate_jwt(user_id, secret_key, expiration_minutes=0)  # Token que expira imediatamente
    is_valid, result = validate_jwt(expired_token, secret_key)
    print(f'Token expirado: {is_valid}, Resultado: {result}')
