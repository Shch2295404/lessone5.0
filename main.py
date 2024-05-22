class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = 'не выполнено'

    def mark_as_done(self):
        self.status = 'выполнено'

    def __str__(self):
        return f"{self.description} (Срок: {self.due_date}) — {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
        else:
            print("Неверный индекс задачи")

    def get_pending_tasks(self):
        return [task for task in self.tasks if task.status == 'не выполнено']

    def __str__(self):
        result = "Список задач:\n"
        for i, task in enumerate(self.tasks):
            result += f"{i + 1}. {task}\n"
        return result


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("запись к зубному", "2024-06-01")
    manager.add_task("регистрация на рейс", "2024-06-02")
    manager.add_task("подтверждение участия в форуме", "2024-06-03")

    print(manager)  # Вывод всех задач

    # Отметить первую задачу как выполненную
    manager.mark_task_as_done(0)
    print(manager)  # Вывод всех задач после отметки

    # Отметить вторую задачу как выполненную
    manager.mark_task_as_done(1)
    print(manager)

    # Отметить третью задачу как выполненную
    # manager.mark_task_as_done(2)
    # print(manager)

    # Вывод невыполненных задач
    pending_tasks = manager.get_pending_tasks()
    print("Невыполненные задачи:")
    for task in pending_tasks:
        print(task)

    # Отметить все задачи как выполненные
    for task in manager.tasks:
        task.mark_as_done()
    print(manager)
