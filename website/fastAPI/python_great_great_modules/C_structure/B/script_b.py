
# script_b.py

def function_b():
    print("Function B from script_b")

# Import function_a from script_a
from A.script_a import function_a

if __name__ == "__main__":
    function_a()
