from Task_Class import *

class Dashboard:
    def __init__(self):
        self.manager = Task_Manager()
    def show_all_options(self):
        print(f"---OPTIONS---: \n"
              f"1. Add new task \n" 
              f"2. Delate task \n"
              f"3. Finish task \n"
              f"4. Show all tasks")

    def chose_option(self):
        while True:
            self.show_all_options()
            option = input(f":: ")

            try:
                opt = int(option)
            except ValueError:
                os.system("cls")
                continue

            if opt not in range(1, 5):
                os.system("cls")
                continue

            match opt:
                case 1:
                    os.system("cls")
                    self.manager.add_task_to_list()
                    con = input()
                    os.system("cls")

                case 2:
                    os.system("cls")
                    self.manager.delete_task()
                    con = input()
                    os.system("cls")

                case 3:
                    os.system("cls")
                    self.manager.show_tasks()
                    self.manager.finish_task()
                    con = input()
                    os.system("cls")

                case 4:
                    os.system("cls")
                    self.manager.show_tasks()
                    con = input()
                    os.system("cls")

                case _:
                    os.system("cls")

    def run(self):
        self.chose_option()