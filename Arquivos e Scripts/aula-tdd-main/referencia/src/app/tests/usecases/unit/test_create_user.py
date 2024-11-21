from unittest.mock import MagicMock
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface
from application.user.create_user import (
    CreateUserRequest,
    CreateUserResponse,
    CreateUser,
)
import pytest


class TestCreateUser:
    def test_create_user_with_valid_data(self):
        mock_repository = MagicMock(UserRepositoryInterface)
        use_case = CreateUser(repository=mock_repository)
        request = CreateUserRequest(name="João")
        response = use_case.execute(request)
        assert response.id is not None
        assert isinstance(response, CreateUserResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True

    def test_create_user_with_invalid_data(self):
        mock_repository = MagicMock(UserRepositoryInterface)
        use_case = CreateUser(repository=mock_repository)
        request = CreateUserRequest(name=1)
        with pytest.raises(Exception, match="name is required"):
            use_case.execute(request)
        assert mock_repository.save.called is False
