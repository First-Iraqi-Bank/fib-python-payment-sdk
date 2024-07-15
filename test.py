import sys
import unittest

# ANSI escape sequences for colors
CYAN = '\033[96m'  # Cyan color
GREEN = '\033[92m'  # Green color
RED = '\033[91m'  # Red color
RESET = '\033[0m'  # Reset to default color


class CustomTextTestResult(unittest.TextTestResult):
    def startTest(self, test):
        super().startTest(test)
        test_name = test._testMethodName  # Get the test method name
        print(f"Running test: {CYAN}{test_name}{RESET}............ ", end="")

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"{GREEN}\u2713{RESET}")  # Unicode check mark symbol in green

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"{RED}\u2717{RESET}")  # Unicode cross mark symbol in red

    def addError(self, test, err):
        super().addError(test, err)
        print(f"{RED}\u2717{RESET}")  # Unicode cross mark symbol in red


class CustomTextTestRunner(unittest.TextTestRunner):
    resultclass = CustomTextTestResult


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific test method if specified as command-line argument
        test_to_run = sys.argv[1]
        suite = unittest.TestSuite()
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_to_run))
    else:
        # Otherwise, discover tests from the 'tests' folder
        loader = unittest.TestLoader()
        start_dir = 'tests'  # Adjust this to your tests folder path
        suite = loader.discover(start_dir=start_dir, pattern='test_*.py')

    runner = CustomTextTestRunner(verbosity=1)  # Set verbosity as needed
    result = runner.run(suite)

    # Optionally print the number of failures and errors
    print(f"\n\nFailures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
