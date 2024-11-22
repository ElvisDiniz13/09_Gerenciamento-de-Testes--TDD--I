from uuid import uuid4
from domain.user.user_entity import User

class TestUser:

    # TESTE PARA CONSTRUIR O USUÁRIO
    def test_user_initialization(self):
        user_id = uuid4()
        user_name = "Alexandre"
        user = User(id=user_id, name=user_name)

        assert user.id == user_id
        assert user.name == user_name