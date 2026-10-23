import json
import os
from enum import Enum
from random import *

class Status(Enum):
    To_Do = 0
    Completed = 1

def open_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data

class Task:

    def __init__(self):
        self.name = ''
        self.priority = 1
        self.status = 0
        self.id = int(random() * 10000000000000000) # The chance of collision is similar to the chance of becoming a milioner by accident

    def show(self):

        print(f"Task --- {self.name} --- \n"
              f"Status: {self.status} \n"
              f"Priority: {self.priority}\n")
        # if self.status == 0:
            # print(f"Deadline time: {self.deadline_time}\n")

    def set_priority(self):

        if self.status:
            print(f"!! ERROR: Task --- {self.name} --- has been done already.\n")
        else:
            print(f":: Set priority as an number in a range 1 - 5")
            print(f":: What is new priority of {self.name}??")
            new_priority = int(input("Priority:> "))

            if new_priority < 0 or new_priority > 5:
                os.system("cls")
                print("!! ERROR: Priority must be between 0 and 5")

                while new_priority < 0 or new_priority > 5:
                    os.system("cls")
                    print("!! ERROR: Priority must be between 0 and 5")
                    print(f":: What is new priority of {self.name}??")
                    new_priority = int(input("Priority:> "))

            self.priority = new_priority
            print(f". Priority of the task has been set to {self.priority}\n")

    def set_name(self):
        print(":: What is the new name??")
        new_name = input("Name:> ").strip()

        if not new_name:
            print("!! ERROR: Name cannot be empty")

            while new_name.strip() == "":
                os.system("cls")
                print("!! ERROR: Name cannot be empty")
                print(":: What is the new name??")
                new_name = input("Name:> ").strip()

        self.name = new_name
        print(f". Name of the task has been set to {self.name}\n")

class Task_Manager:
    def __init__(self):
        self.tasks = []

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

    def show_tasks(self):
        data = open_file("data.json")

        for task in data["List"]:
            stat = "Done" if task["status"] else "To do"
            print(f"-< Name: {task["task_name"]} \n"
                  f'-< Priority: {task["priority"]}\n'
                  f"-< Status: " + stat + "\n"
                  f"-< ID: {task["id"]}")
            print("\n")

    def finish_task(self):

        print(f":: What is the ID of the task you would like to finish??")
        try:
            id = int(input("ID:>"))
        except:
            print("!! ERROR: ID must be an integer")
            return

        data = open_file("data.json")
        tasks_list = data.get("List", [])

        found = False

        for task in tasks_list:

            if task.get("id") == id:
                found = True
                status = task.get("status")

                if status == 0:
                    task["status"] = 1
                    print(f". Task --- {task.get('task_name')} --- has been finished.\n")
                else:
                    print(f"!! ERROR: Task --- {task.get('task_name')} --- has been done already.\n")
                break

        if not found:
            print(f"!! ERROR: No task with this ID.\n")
            return

        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def delete_task(self):
        self.show_tasks()

        print(":: What is the ID of the task you would like to delete??")
        try:
            id = int(input("ID:>"))
        except ValueError:
            print("!! ERROR: ID must be an integer")

        data = open_file("data.json")
        task_to_delete = None
        tasks_list = data.get("List", [])

        for task in tasks_list:
            if task.get("id") == id:
                task_to_delete = task

        if task_to_delete:
            tasks_list.remove(task_to_delete)

            with open("data.json", 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            print(". Task has been deleted.\n")