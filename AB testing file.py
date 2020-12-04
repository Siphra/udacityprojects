# AB Testing file
# Initial menu code laid down 3 December 2020
# Project actual start date:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm



def menu_ops():

    """
    This function serves as the main menu for all other function calls,
    it's purpose is to reduce the amount of processing time to the bare minimum
    by not forcing the code to call all available functions inorder to test, or run
    the code.

    """

    print(" This menu is to make the code easier to use")
    print(" Selection menu:")
    menu = ['1: First option', '2: Second Option']
    for i in range(len(menu)):
        print(menu[i])
    print("What option would you like : ")
    x = input()
    if x == int:
        print(menu(x))
    else:
        print(x)
    return print(x)

help(menu_ops)