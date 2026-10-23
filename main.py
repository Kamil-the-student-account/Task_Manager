from Dashboard_Class import *

if __name__ == '__main__':
    dashboard = Dashboard()
    dashboard.manager = Task_Manager()
    while True:
        dashboard.run()