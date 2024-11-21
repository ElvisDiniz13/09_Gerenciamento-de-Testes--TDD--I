from uuid import uuid4
from infra.user.in_memory_user_repository import InMemoryUserRepository
from domain.user.user_entity import User


# Classe para testar o método de salvar usuários
class TestSaveUser:

    # Testa se é possível salvar usuários no repositório
    def test_can_save_user(self):
        repository = (
            InMemoryUserRepository()
        )  # Cria uma instância do repositório em memória
        user1 = User(
            id=uuid4(), name="João"
        )  # Cria o primeiro usuário com um UUID único
        user2 = User(
            id=uuid4(), name="Maria"
        )  # Cria o segundo usuário com um UUID único
        repository.save(user1)  # Salva o primeiro usuário
        repository.save(user2)  # Salva o segundo usuário

        # Verifica se ambos os usuários foram salvos corretamente
        assert len(repository.users) == 2
        assert repository.users[0] == user1
        assert repository.users[1] == user2


# Classe para testar o método de busca de usuários por ID
class TestGetUserById:

    # Testa se é possível buscar um usuário pelo ID
    def test_can_get_user_by_id(self):
        repository = (
            InMemoryUserRepository()
        )  # Cria uma instância do repositório em memória
        user1 = User(id=uuid4(), name="João")  # Cria o primeiro usuário
        user2 = User(id=uuid4(), name="Maria")  # Cria o segundo usuário
        repository.save(user1)  # Salva o primeiro usuário
        repository.save(user2)  # Salva o segundo usuário

        user = repository.get_by_id(user2.id)  # Busca o segundo usuário pelo ID

        assert user == user2  # Verifica se o usuário retornado é o mesmo buscado

    # Testa se o método retorna None quando o usuário não existe
    def test_when_user_does_not_exist_should_return_none(self):
        repository = (
            InMemoryUserRepository()
        )  # Cria uma instância do repositório em memória
        user1 = User(id=uuid4(), name="João")  # Cria o primeiro usuário
        user2 = User(id=uuid4(), name="Maria")  # Cria o segundo usuário
        repository.save(user1)  # Salva o primeiro usuário
        repository.save(user2)  # Salva o segundo usuário

        user = repository.get_by_id(
            uuid4()
        )  # Tenta buscar um usuário com um ID que não existe

        assert user is None  # Verifica se o retorno é None


# Classe para testar o método de exclusão de usuários
class TestDeleteUser:

    # Testa se é possível deletar um usuário pelo ID
    def test_delete_user(self):
        repository = (
            InMemoryUserRepository()
        )  # Cria uma instância do repositório em memória
        user1 = User(id=uuid4(), name="João")  # Cria o primeiro usuário
        user2 = User(id=uuid4(), name="Maria")  # Cria o segundo usuário
        repository.save(user1)  # Salva o primeiro usuário
        repository.save(user2)  # Salva o segundo usuário

        repository.delete(user1.id)  # Deleta o primeiro usuário

        # Verifica se apenas o segundo usuário permanece no repositório
        assert len(repository.users) == 1
        assert repository.users[0] == user2


# Classe para testar o método de atualização de usuários
class TestUpdateUser:

    # Testa se é possível atualizar um usuário existente
    def test_update_user(self):
        repository = (
            InMemoryUserRepository()
        )  # Cria uma instância do repositório em memória
        user1 = User(id=uuid4(), name="João")  # Cria o primeiro usuário
        user2 = User(id=uuid4(), name="Maria")  # Cria o segundo usuário
        repository.save(user1)  # Salva o primeiro usuário
        repository.save(user2)  # Salva o segundo usuário

        user1.name = "Alexandre"  # Atualiza o nome do primeiro usuário
        repository.update(user1)  # Aplica a atualização no repositório

        assert len(repository.users) == 2  # Verifica que ainda há dois usuários
        updated_user = repository.get_by_id(user1.id)  # Busca o usuário atualizado
        assert updated_user.name == "Alexandre"  # Verifica se o nome foi atualizado

    # Testa se tentar atualizar um usuário inexistente não gera erro
    def test_update_non_existent_user_does_not_raise_exception(self):
        repository = (
            InMemoryUserRepository()
        )  # Cria uma instância do repositório em memória
        user1 = User(id=uuid4(), name="João")  # Cria um usuário que não será salvo

        repository.update(
            user1
        )  # Tenta atualizar um usuário que não existe no repositório

        # Verifica que o repositório permanece vazio
        assert len(repository.users) == 0
