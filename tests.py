from functions import get_files_info as gfi

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
    for test_case in test_cases:
        print("============================")
        result = gfi.get_files_info(*test_case["args"])

        # print(f'Excpeted: {test_case["excpected"]}')
        # print("=======")
        print(result)

        # if result.inc == test_case["excpected"]:
        #     print("PASS")
        # else:
        #     print("FAIL")

    # print(gfi.get_files_info("calculator", "."))
    # print(gfi.get_files_info("calculator", "pkg"))
    # print(gfi.get_files_info("calculator", "/bin"))
    # print(gfi.get_files_info("calculator", "../"))

print(__name__)
if __name__ == "__main__":
    tests()
