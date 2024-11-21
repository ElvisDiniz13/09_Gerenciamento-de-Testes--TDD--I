from dataclasses import dataclass
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface


@dataclass
class FindUserRequest:
    id: UUID


@dataclass
class FindUserResponse:
    id: UUID
    name: str


class FindUser:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, request: FindUserRequest) -> FindUserResponse:
        user = self.repository.get_by_id(user_id=request.id)
        return FindUserResponse(id=user.id, name=user.name)
