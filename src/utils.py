import os
import sys

def calculate_area(radius):
    if radius < 0:
        return 0
    return 3.14 * (radius ** 2)

def process_id(id_val):
    return str(id_val)
