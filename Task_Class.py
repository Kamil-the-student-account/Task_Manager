from enum import Enum
from random import *
import json

class Status(Enum):
    To_Do = 0
    Completed = 1

class Task:
    def __init__(self):
        self.name = ''
        self.priority = 1
        self.status = 0
        self.id = int(random() * 10000000000000000) # there can be collission of id of two tasks

    def show(self):
        print(f"Task --- {self.name} --- \n"
              f"Status: {self.status} \n"
              f"Priority: {self.priority}\n")
        # if self.status == 0:
            # print(f"Deadline time: {self.deadline_time}\n")
    def finish(self):
        if self.status == 0:
            self.status = 1
            print(f"Task --- {self.name} --- has been finished.\n")
        else:
            print(f"ERROR: Task --- {self.name} --- has been done already.\n")
    def set_priority(self):
        if self.status:
            print(f"ERROR: Task --- {self.name} --- has been done already.\n")
        else:
            print(f"-> What is new priority of {self.name}?\n")
            new_priority = int(input(":: "))
            if new_priority < 0 or new_priority > 5:
                print("ERROR: Priority must be between 0 and 5\n")
                while new_priority < 0 or new_priority > 5:
                    print(f"-> What is new priority of {self.name}?\n")
                    new_priority = int(input("Priority:: "))
            self.priority = new_priority
            print(f"Priority of the task has been set to {self.priority}\n")
    def set_name(self):
        print("-> What is the new name: \n")
        new_name = input("Name:: ").strip()
        if not new_name:
            print("ERROR: Name cannot be empty \n")
            while new_name.strip() == "":
                print("-> What is the new name: \n")
                new_name = input("Name:: ").strip()
        self.name = new_name
        print(f"Name of the task has been set to {self.name}\n")

def open_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data

class Task_Manager:
    def __init__(self):
        self.tasks = []
    def write_data(self, task_name, task_priority, task_status, task_id):
        task = {
            "task_name": task_name,
            "priority": task_priority,
            "status": task_status,
            "id": task_id
        }
        with open("data.json", "a", encoding = 'utf-8') as file:
            json.dump(task, file, indent = 4, ensure_ascii = False)
        print("->Task has been written to data.json\n")

    def add_task_to_list(self):
        new_task = Task()
        new_task.set_name()
        new_task.set_priority()

        def append_task(file_name, new_item):
            try:
                with open(file_name, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {"List": []}

            if "List" not in data:
                data["List"] = []
            data["List"].append(new_item)

            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)

        new_item = {
            "task_name" : new_task.name,
            "priority" : new_task.priority,
            "status" : 0,
            "id" : new_task.id
        }

        append_task("data.json", new_item)

    def show_tasks_id_list(self):
        for task in self.tasks:
            print(f"Task --- {task.name} --- ID: {task.id}")

    def show_tasks(self):
        data = open_file("data.json")
        for task in data["List"]:
            print("-" * 20)
            print(f"Name: {task["task_name"]} + \n"
                  f"Priority: {task["priority"]}\n"
                  f"Status: {task["status"]}\n"
                  f"ID: {task["id"]}")

    def delate_task(self, task):
        self.tasks.remove(task)
        print(f"Task --- {task.name} --- ID: {task.id} --- has been deleted.\n")