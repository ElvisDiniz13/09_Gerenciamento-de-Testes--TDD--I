import pytest
from uuid import uuid4
from domain.task.task_entity import Task
from domain.user.user_entity import User


class TestUser:

    # Teste para inicialização do usuário
    def test_user_initialization(self):
        user_id = uuid4()
        user_name = "Test User"
        user = User(id=user_id, name=user_name)

        assert user.id == user_id
        assert user.name == user_name
        assert user.tasks == []

    # Teste para validação do ID do usuário
    def test_user_id_validation(self):
        with pytest.raises(Exception, match="id must be an UUID"):
            User(id="invalid_id", name="Test User")

    # Teste para validação do nome do usuário
    def test_user_name_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="name is required"):
            User(id=user_id, name="")
