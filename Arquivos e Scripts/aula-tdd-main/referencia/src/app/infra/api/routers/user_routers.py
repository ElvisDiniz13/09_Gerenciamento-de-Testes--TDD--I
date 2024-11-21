# Importa dependências necessárias do FastAPI e outras camadas da aplicação
from fastapi import APIRouter, HTTPException
from infra.user.in_memory_user_repository import InMemoryUserRepository
from application.user.create_user import CreateUser, CreateUserRequest
from application.user.find_user import FindUser, FindUserRequest
from uuid import UUID

# Cria um roteador para gerenciar endpoints de usuários, com prefixo '/users' e tag "Users"
router = APIRouter(prefix="/users", tags=["Users"])

# Instancia um repositório de usuários em memória (simulado), que armazena os dados temporariamente
repository = InMemoryUserRepository()


# Endpoint para criação de um novo usuário
@router.post("/")
def create_user(request: CreateUserRequest):
    try:
        # Inicializa o caso de uso de criação de usuário, passando o repositório
        usecase = CreateUser(repository)

        # Executa o caso de uso com os dados da requisição e retorna o resultado
        output = usecase.execute(request)
        return output

    except Exception as e:
        # Em caso de erro, retorna um erro HTTP 404 com a mensagem detalhada da exceção
        raise HTTPException(status_code=404, detail=str(e))


# Endpoint para busca de um usuário pelo ID
@router.get("/{user_id}")
def find_user(user_id: UUID):
    try:
        # Inicializa o caso de uso de busca de usuário, passando o repositório
        usecase = FindUser(repository)

        # Executa o caso de uso com o ID do usuário e retorna o resultado
        output = usecase.execute(FindUserRequest(id=user_id))
        return output

    except Exception as e:
        # Em caso de erro, retorna um erro HTTP 404 com a mensagem detalhada da exceção
        raise HTTPException(status_code=404, detail=str(e))
