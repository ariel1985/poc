
# script_a.py

def function_a():
    print("Function A from script_a")

# Import function_b from script_b
from B.script_b import function_b

if __name__ == "__main__":
    function_b()
