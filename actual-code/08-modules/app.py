"""
This is my application file ... 
"""
import utils as ut
# import pandas as pd
# import numpy as np
from utils import insecure_printer, Shape as S

triangle = "I am a triangle"
print(ut.triangle)
print(triangle)

square = ut.Shape("square")

ut.insecure_printer(square)

insecure_printer("I'm free!")
circle = S("circle")

print(__file__)
print(__doc__)
print(dir(ut))

print(ut.__file__)
print(f"In the app.py file my name is {__name__}")
print(f"In the app.py file my name is {ut.__name__}")