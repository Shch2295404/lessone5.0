class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return f"{self.description} (Due: {self.due_date}) - {'Выполнено' if self.completed else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
        else:
            raise ValueError('Неверный индекс задачи')

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __str__(self):
        result = "Task List:\n"
        for i, task in enumerate(self.tasks, start=1):
            result += f"{i}. {task}\n"
        return result


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.add_task("Запись к стоматологу", "2024-06-01")
    task_manager.add_task("Регистрация на рейс", "2024-06-02")
    task_manager.add_task("Подтвердить участие в форуме", "2024-06-03")

    print(task_manager) # Печать всех задач

    # Отметьте первую задачу как выполненную
    task_manager.complete_task(0)
    print(task_manager) # Печать всех задач после завершения

    # Пометьте вторую задачу как выполненную
    task_manager.complete_task(1)
    print(task_manager)

    # Отметьте третью задачу как выполненную
    # task_manager.complete_task(2)
    # print(task_manager)

    # Печать ожидающих выполнения заданий
    pending_tasks = task_manager.get_pending_tasks()
    print("Pending Tasks:")
    for task in pending_tasks:
        print(task)

    # Пометить все задачи как выполненные
    for task in task_manager.tasks:
        task.complete()
    print(task_manager)

# Переименовал метод mark_as_done в классе Task в complete для ясности.
# Переименовал атрибут status в классе Task в completed для ясности.
# Переименовал метод mark_task_as_done в классе TaskManager в complete_task для ясности.
# Переименовали метод get_pending_tasks в классе TaskManager в get_pending_tasks для ясности.
# Переименовали переменную manager в основном блоке кода в task_manager для наглядности.
# Удалены отладочные операторы печати.
# Улучшена читаемость методов __str__ за счет использования более описательных строк.
# Изменили сообщение об ошибке в методе complete_task, чтобы вместо оператора печати использовать исключение ValueError.
# Улучшена читаемость основного блока кода за счет использования более описательных имен переменных.
