from unittest.mock import MagicMock, create_autospec
from uuid import uuid4
import pytest
from domain.user.user_repository_interface import UserRepositoryInterface
from application.user.find_user import FindUserRequest, FindUserResponse, FindUser
from domain.user.user_entity import User


class TestFindUser:
    def test_when_user_exists_then_return_response_dto(self):
        mock_user = User(id=uuid4(), name="João")
        mock_repository = create_autospec(UserRepositoryInterface)
        mock_repository.get_by_id.return_value = mock_user

        use_case = FindUser(repository=mock_repository)
        request = FindUserRequest(id=mock_user.id)

        response = use_case.execute(request)

        assert response == FindUserResponse(id=mock_user.id, name="João")

    def test_when_user_not_found_then_raise_exception(self):
        mock_repository = create_autospec(UserRepositoryInterface)
        mock_repository.get_by_id.return_value = None

        use_case = FindUser(repository=mock_repository)
        request = FindUserRequest(id=uuid4())

        with pytest.raises(Exception):
            use_case.execute(request)
