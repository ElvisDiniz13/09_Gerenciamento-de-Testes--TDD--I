from abc import ABC, abstractmethod
from domain.user.user_entity import User
from typing import List
from uuid import UUID


class UserRepositoryInterface(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[User]:
        raise NotImplementedError
