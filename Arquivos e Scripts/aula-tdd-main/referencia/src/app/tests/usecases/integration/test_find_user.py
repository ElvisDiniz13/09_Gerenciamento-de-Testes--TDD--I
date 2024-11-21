from uuid import UUID, uuid4
from application.user.find_user import FindUser, FindUserRequest
from infra.user.in_memory_user_repository import InMemoryUserRepository
from domain.user.user_entity import User


class TestFindUser:

    def test_find_user_by_id(self):
        # Cria um repositório de usuários em memória
        repository = InMemoryUserRepository()

        # Cria e adiciona um usuário ao repositório
        user_id = uuid4()
        user = User(id=user_id, name="João")
        repository.save(user)

        # Instancia o caso de uso de busca de usuário, passando o repositório como dependência
        use_case = FindUser(repository=repository)

        # Cria uma requisição de busca de usuário pelo ID
        request = FindUserRequest(id=user_id)

        # Executa o caso de uso com a requisição e armazena a resposta
        response = use_case.execute(request)

        # Verifica se a resposta não é nula, indicando que o usuário foi encontrado
        assert response is not None
        # Verifica se o ID do usuário encontrado é uma instância válida de UUID
        assert isinstance(response.id, UUID)
        # Verifica se o ID do usuário encontrado corresponde ao ID buscado
        assert response.id == user_id
        # Verifica se o nome do usuário encontrado é o mesmo que o nome do usuário salvo
        assert response.name == "João"
