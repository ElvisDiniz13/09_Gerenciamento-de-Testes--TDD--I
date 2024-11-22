from uuid import UUID

class User:

    id: UUID
    name: str

    def __init__(self,id: UUID, name: str):
        self.id = id
        self.name = name