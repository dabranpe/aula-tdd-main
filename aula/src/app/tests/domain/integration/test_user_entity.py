from domain.user.user_entity import User
from domain.task.task_entity import Task
from uuid import uuid4

class TestUserWithTasks:

    # TESTE PARA ADICIONAR TAREFAS AO USUARIO
    def teste_collect_tasks(self):
        user = User(id=uuid4(), name="Alfredão")
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