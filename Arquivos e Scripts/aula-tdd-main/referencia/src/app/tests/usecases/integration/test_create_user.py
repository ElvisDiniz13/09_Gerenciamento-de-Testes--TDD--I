from uuid import UUID, uuid4
from application.user.create_user import CreateUser, CreateUserRequest
from infra.user.in_memory_user_repository import InMemoryUserRepository


class TestCreateUser:

    def test_create_user_with_valid_data(self):
        # Inicializa um repositório de usuários em memória
        repository = InMemoryUserRepository()
        # Instancia o caso de uso de criação de usuário, passando o repositório como dependência
        use_case = CreateUser(repository=repository)
        # Cria uma requisição com dados válidos para o usuário, usando o nome "João"
        request = CreateUserRequest(name="João")
        # Executa o caso de uso com a requisição e armazena a resposta
        response = use_case.execute(request)

        # Verifica se a resposta não é nula, o que indica que o usuário foi criado
        assert response is not None
        # Verifica se o ID do usuário na resposta é uma instância válida de UUID
        assert isinstance(response.id, UUID)
        # Confirma que o repositório agora contém exatamente um usuário
        assert len(repository.users) == 1

        # Obtém o usuário persistido no repositório
        persisted_user = repository.users[0]

        # Verifica se o ID do usuário persistido coincide com o ID do usuário na resposta
        assert persisted_user.id == response.id
        # Verifica se o nome do usuário persistido é o mesmo que o fornecido na requisição ("João")
        assert persisted_user.name == "João"
