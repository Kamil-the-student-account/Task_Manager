import json
import os
from _pyrepl.commands import clear_screen
from time import *
from random import *
from enum import Enum
from Classes.Dashboard_Class import *
from Classes.Task_Class import *
from Texting.Errors import *
from Texting.Info import *

class Status(Enum):
    To_Do = 0
    Completed = 1
