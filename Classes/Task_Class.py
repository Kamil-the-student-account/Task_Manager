from Imports import *

class Task:
    def __init__(self):
        self.name = ''
        self.add_date = time()
        self.deadline_time = ''
        self.priority = 1 # is a scale 1-5 where 1 is the least important and 5 is crucial
        self.status = 0
        self.id = random() # there can be collission of id of two tasks

    def show(self):
        print(f"Task --- {self.name} --- "
              f"Added date: {self.add_date} "
              f"Status: {self.status} "
              f"Priority: {self.priority}")
        if self.status == 0:
            print(f"Deadline time: {self.deadline_time}")
    def finish(self):
        if self.status == 0:
            self.status = 1
            print(f"Task --- {self.name} --- has been finished.")
        else:
            print(f"ERROR: Task --- {self.name} --- has been done already.")
    def set_priority(self):
        if self.status:
            print(f"ERROR: Task --- {self.name} --- has been done already.")
        else:
            new_priority = int(input(f"What is new priority of {self.name}?"))
            if new_priority < 0 or new_priority > 5:
                print("ERROR: Priority must be between 0 and 5")
                while new_priority < 0 or new_priority > 5:
                    new_priority = int(input(f"What is new priority of {self.name}?"))
            self.priority = new_priority
            print(f"Priority of the task has been set to {self.priority}")
    def set_date(self):
        new_time  = time(input("What is the new deadline: "))
        self.deadline_time = new_time
        print(f"Time of deadline set to {new_time}")
    def set_name(self):
        new_name = input("What is new name?").strip()
        if not new_name:
            print("ERROR: Name cannot be empty")
            while new_name.strip() == "":
                new_name = input("What is new name?").strip()
        self.name = new_name
        print(f"Name of the task has been set to {self.name}")

class TaskManager:
    def __init__(self):
        self.tasks = []
    def write_json(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
    def add_task(self):
        new_task = Task()
        new_task.set_name()
        new_task.set_priority()
        new_task.set_date()
        self.tasks.append(new_task)
    def show_tasks_id_list(self):
        for task in self.tasks:
            print(f"Task --- {task.name} --- ID: {task.id}")
    def show_tasks(self):
        for task in self.tasks:
            task.show()
    def delate_task(self, task):
        self.tasks.remove(task)
        print(f"Task --- {task.name} --- ID: {task.id} --- has been deleted.")
    def chose_task(self):
        self.show_tasks()
        task = input("Task id::  ")
        return task