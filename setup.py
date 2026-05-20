from cx_Freeze import setup, Executable
import random

# Open main.py and append random variable
file = open("main.py", "a", encoding="utf-8")

# Generate random number
r1 = random.randint(-100000, 100000)

# Convert integer to string before concatenation
file.write("\nvar = " + str(r1))

file.write("\nprint(var)\n")
file.close()

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna"]

options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="Wifi",
    options=options,
    version="1.0.0",
    description='Wifi Password',
    executables=executables
)
