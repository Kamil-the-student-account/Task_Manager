from logging import Manager

from Imports import *

if __name__ == '__main__':
    dashboard = Dashboard()
    dashboard.manager = TaskManager()
    while True:
        dashboard.run()