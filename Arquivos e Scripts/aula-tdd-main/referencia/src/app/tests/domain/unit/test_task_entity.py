import pytest
from uuid import uuid4
from domain.task.task_entity import Task


class TestTask:

    # Teste para verificar a inicialização de uma tarefa
    def test_task_initialization(self):
        task_id = uuid4()
        user_id = uuid4()
        title = "Test Task"
        description = "This is a test task."
        completed = False

        task = Task(
            id=task_id,
            user_id=user_id,
            title=title,
            description=description,
            completed=completed,
        )

        # Verifica se os atributos da tarefa estão corretos
        assert task.id == task_id
        assert task.user_id == user_id
        assert task.title == title
        assert task.description == description
        assert task.completed == completed

    # Teste para verificar a validação do ID da tarefa
    def test_task_id_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="id must be an UUID"):
            Task(
                id=1,
                user_id=user_id,
                title="Task Title",
                description="Description",
                completed=False,
            )

    # Teste para verificar a validação do user_id
    def test_task_user_id_validation(self):
        task_id = uuid4()
        with pytest.raises(Exception, match="user_id must be an UUID"):
            Task(
                id=task_id,
                user_id="invalid_user_id",
                title="Task Title",
                description="Description",
                completed=False,
            )

    # Teste para verificar a validação do título da tarefa
    def test_task_title_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="title is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="",
                description="Description",
                completed=False,
            )

    # Teste para verificar a validação da descrição da tarefa
    def test_task_description_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="description is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="Task Title",
                description="",
                completed=False,
            )

    # Teste para verificar a validação do status 'completed' da tarefa
    def test_task_completed_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(
            Exception, match="invalid completed status: must be a boolean"
        ):
            Task(
                id=task_id,
                user_id=user_id,
                title="Task Title",
                description="Description",
                completed="not_boolean",
            )

    # Teste para verificar se o método mark_as_completed funciona corretamente
    def test_mark_as_completed(self):
        task = Task(
            id=uuid4(),
            user_id=uuid4(),
            title="Test Task",
            description="Description",
            completed=False,
        )

        # Marca a tarefa como concluída
        task.mark_as_completed()

        # Verifica se o atributo 'completed' foi atualizado para True
        assert task.completed is True
