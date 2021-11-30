"""
Orchestrate

Author: Christian M. Fulton
Date:29.Oct.2021
"""
import driver
from helpers import verify_eng
from cutter import *


def execute():
    """
    exec
    """
    eng = input("Enter the engineer page: ")

    data = driver.launch(eng)
    cut(**data)


if __name__ == "__main__":
    execute()