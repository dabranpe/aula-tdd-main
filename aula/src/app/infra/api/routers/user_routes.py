# Importa dependências necessárias do FastAPI e outras camadas da aplicação
from fastapi import APIRouter, HTTPException
from infra.user.in_memory_user_repository import InMemoryUserRepository
from application.user.create_user_use_case import CreateUserUseCase, CreateUserRequest

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
        usecase = CreateUserUseCase(repository)

        # Executa o caso de uso com os dados da requisição e retorna o resultado
        output = usecase.execute(request)
        return output

    except Exception as e:
        # Em caso de erro, retorna um erro HTTP 404 com a mensagem detalhada da exceção
        raise HTTPException(status_code=404, detail=str(e))



