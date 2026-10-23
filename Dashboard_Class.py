
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
        option = int(input(f":: "))
        if option not in range(1, 6):
            print("ERROR: Option must be between 1 and 5\n")
            while option not in range(1, 6):
                # clear_screen()
                option = int(input(f":: "))
        # clear_screen()
        match option:
            case 1:
                self.manager.add_task_to_list()
            case 2:
                task = self.manager.chose_task()
                self.manager.delate_task(task)
            case 3:
                task = self.manager.chose_task()
                task.finish()
            case 4:
                self.manager.show_tasks()

    def run(self):
        self.show_all_options()
        self.chose_option()
        # clear_screen()