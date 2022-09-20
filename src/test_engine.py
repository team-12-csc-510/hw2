import importlib.machinery
import os
import sys
import traceback
import types
from inspect import getmembers, isfunction

from src.utils import the


class TestEngine:
    def __init__(self, path):
        self.path = path
        self.test_list = []
        self.fails = 0
        sys.path.append(path)

    def get_tests(self):
        module = importlib.import_module(self.path)
        return [func for func in getmembers(module) if isfunction(func[1])]

    def create_test_list(self):
        file_list = [
            os.path.join(self.path, file)
            for file in os.listdir(self.path)
            if os.path.isfile(os.path.join(self.path, file))
        ]
        for file in file_list:
            mod_loader = importlib.machinery.SourceFileLoader("tests", file)
            mod = types.ModuleType("tests")
            mod_loader.exec_module(mod)
            self.test_list.extend(
                [
                    func
                    for func in getmembers(mod)
                    if (isfunction(func[1]) and func[0].startswith("test"))
                ]
            )

    def run_all_tests(self):
        self.create_test_list()
        for test_name, test_func in self.test_list:
            if the["dump"]:
                if not test_func():
                    self.fails += 1
            else:
                try:
                    if not test_func():
                        self.fails += 1
                except Exception:
                    print(traceback.print_exc())
                    self.fails += 1

        tests = len(self.test_list)
        print(f"Executed {tests} test cases ; failed {self.fails} test cases")

    def list_tests(self):
        print("Test names:")
        for test in self.test_list:
            print(test[0])

    def sort_tests(self):
        self.test_list.sort(key=lambda tup: tup[0])


if __name__ == "__main__":
    test_path = os.path.join(os.path.abspath(os.curdir), "../tests/unit")
    test_eng = TestEngine(test_path)
    test_eng.run_all_tests()
