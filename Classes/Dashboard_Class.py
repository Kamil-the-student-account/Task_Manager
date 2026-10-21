from Imports import *
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Dashboard:
    def __init__(self):
        self.manager = TaskManager()
    def show_all_options(self):
        print(f"---OPTIONS---:"
              f"1. Add new task"
              f"2. Delate task"
              f"3. Finish task"
              f"4. Show all tasks"
              )
    def chose_option(self):
        option = int(input(f":: "))
        if option not in range(1, 6):
            print("ERROR: Option must be between 1 and 5")
            while option not in range(1, 6):
                clear_screen()
                option = int(input(f":: "))
        clear_screen()
        match option:
            case 1:
                self.manager.add_task()
            case 2:
                task = self.manager.chose_task()
                self.manager.delate_task(task)
            case 3:
                task = self.manager.chose_task()
                task.finish()
            case 4:
                self.manager.show_tasks()
                task = self.manager.chose_task()
                task.finish()

    def run(self):
        self.show_all_options()
        self.chose_option()
        clear_screen()