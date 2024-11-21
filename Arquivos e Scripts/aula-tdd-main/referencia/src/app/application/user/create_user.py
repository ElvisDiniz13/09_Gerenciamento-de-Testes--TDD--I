from dataclasses import dataclass
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface
from domain.user.user_entity import User
from uuid import uuid4


@dataclass
class CreateUserRequest:
    name: str


@dataclass
class CreateUserResponse:
    id: UUID
    name: str


class CreateUser:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        user = User(id=uuid4(), name=request.name)
        self.repository.save(user=user)
        return CreateUserResponse(id=user.id, name=user.name)
