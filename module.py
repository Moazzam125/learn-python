# Module


# Import entire module

import function

from function import *


# Import single class

from classes import car


# Import entire classes

import classes


# Using short name of module's file

import function as fun


# Using function from module

function.build_person('moazzam', 'muhammad')


print("\n====================")


# Impport Specfic functions from module
                                        # (from) must
                                        # import (function_1, function_2)
                                        # Don't use dot notation (module.function)

from function import greet_user, greet

greet()

print("\n====================")


# Using short name of module's function

from function import my_pets as mp

mp('Tom', 'cat')

print("\n====================")