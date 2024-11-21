from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface
from domain.user.user_entity import User
from typing import Optional


class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self, users: list[User] = None):
        self.users: list[User] = users or []

    def save(self, user: User) -> None:
        self.users.append(user)

    def get_by_id(self, user_id: UUID) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def delete(self, user_id: UUID) -> None:
        user = self.get_by_id(user_id)
        if user:
            self.users.remove(user)

    def list(self) -> list[User]:
        return [user for user in self.users]

    def update(self, user: User) -> None:
        to_update_user = self.get_by_id(user.id)
        if to_update_user:
            self.users.remove(to_update_user)
            self.users.append(user)
