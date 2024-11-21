from domain.user.user_entity import User
from domain.task.task_entity import Task
from uuid import uuid4


# Teste de intergração de usuário com tarefas
class TestUserWithTask:

    # Teste para adicionar tarefas ao usuário
    def test_collect_tasks(self):
        user = User(id=uuid4(), name="Test User")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 1",
            description="Description 1",
            completed=False,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 2",
            description="Description 2",
            completed=True,
        )

        user.collect_tasks([task1, task2])
        assert len(user.tasks) == 2
        assert task1 in user.tasks
        assert task2 in user.tasks

    # Teste para contagem de tarefas pendentes
    def test_count_pending_tasks(self):
        user = User(id=uuid4(), name="Test User")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 1",
            description="Description 1",
            completed=False,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 2",
            description="Description 2",
            completed=False,
        )
        task3 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 3",
            description="Description 3",
            completed=False,
        )

        task1.mark_as_completed()
        user.collect_tasks([task1, task2, task3])
        pending_count = user.count_pending_tasks()
        assert pending_count == 2  # task1 está concluída; task2 e task3 estão pendentes

    # Teste para verificar a contagem de tarefas pendentes em uma lista vazia
    def test_count_pending_tasks_empty(self):
        user = User(id=uuid4(), name="Test User")
        assert user.count_pending_tasks() == 0  # Não há tarefas

    # Teste para tentar coletar uma lista vazia de tarefas
    def test_collect_empty_task_list(self):
        user = User(id=uuid4(), name="Test User")
        user.collect_tasks([])  # Adiciona uma lista vazia de tarefas
        assert len(user.tasks) == 0  # A lista de tarefas deve permanecer vazia

    # Teste para verificar se o método count_pending_tasks lida corretamente quando todas as tarefas estão concluídas
    def test_all_tasks_completed(self):
        user = User(id=uuid4(), name="Test User")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 1",
            description="Description 1",
            completed=True,
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 2",
            description="Description 2",
            completed=True,
        )

        user.collect_tasks([task1, task2])
        assert user.count_pending_tasks() == 0  # Ambas as tarefas estão concluídas

    # Teste para verificar se o método count_pending_tasks lida corretamente quando há apenas uma tarefa
    def test_single_pending_task(self):
        user = User(id=uuid4(), name="Test User")
        task = Task(
            id=uuid4(),
            user_id=user.id,
            title="Task 1",
            description="Description 1",
            completed=False,
        )

        user.collect_tasks([task])
        assert user.count_pending_tasks() == 1  # Apenas uma tarefa pendente
