from functions import get_files_info as gfi
from functions import get_file_content as gfc
from functions import write_file as wc
from functions import run_python_file as rpf


#TODO: not really unit tests, more of a "print what i need" atm. fix that.

test_cases = [
    {
    "args": ["calculator", "."], 
    "excpected": 
'''- main.py: file_size=719 bytes, is_dir=False
- tests.py: file_size=1331 bytes, is_dir=False
- pkg: file_size=44 bytes, is_dir=True
'''
},
    {
    "args": ["calculator", "pkg"], 
    "excpected":
'''- calculator.py: file_size=1721 bytes, is_dir=False
- render.py: file_size=376 bytes, is_dir=False
'''
},
    {
    "args": ["calculator", "/bin"], 
    "excpected":
'''Error: Cannot list "/bin" as it is outside the permitted working directory
'''},
    {
    "args": ["calculator", "../"], 
    "excpected":
'''Error: Cannot list "../" as it is outside the permitted working directory
'''},
]
def tests():
    # for test_case in test_cases:
    #     print("============================")
    #     result = gfi.get_files_info(*test_case["args"])

        # print(f'Excpeted: {test_case["excpected"]}')
        # print("=======")
        # print(result)

        # if result.inc == test_case["excpected"]:
        #     print("PASS")
        # else:
        #     print("FAIL")

    # print(gfi.get_files_info("calculator", "."))
    # print(gfi.get_files_info("calculator", "pkg"))
    # print(gfi.get_files_info("calculator", "/bin"))
    # print(gfi.get_files_info("calculator", "../"))

    # print(gfc.get_file_contents("calculator", "lorem.txt"))
    # print(gfc.get_file_contents("calculator", "main.py"))
    # print(gfc.get_file_contents("calculator", "pkg/calculator.py"))
    # print(gfc.get_file_contents("calculator", "/bin/cat"))
    # print(gfc.get_file_contents("calculator", "pkg/does_not_exist.py"))

    # print(wc.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(wc.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(wc.write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    
    print(rpf.run_python_file("calculator", "main.py"))
    print(rpf.run_python_file("calculator", "main.py", ["3 + 5"]))
    print(rpf.run_python_file("calculator", "tests.py"))
    print(rpf.run_python_file("calculator", "../main.py"))
    print(rpf.run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    tests()
