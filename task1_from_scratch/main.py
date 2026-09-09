from problems import PROBLEMS


class CodingEnvironment:

    def __init__(self, problem_name):
        self.problem = PROBLEMS[problem_name]

    def get_task(self):
        return self.problem["description"]

    def evaluate(self, code):

        namespace = {}

        # Run the submitted code
        try:
            exec(code, namespace)

        except Exception as error:
            return {
                "score": 0,
                "error": f"Code Error: {error}"
            }

        # Get the required function
        function_name = self.problem["function_name"]

        if function_name not in namespace:
            return {
                "score": 0,
                "error": f"Function '{function_name}' not found"
            }

        function = namespace[function_name]

        passed = 0
        results = []

        # Run all test cases
        for inputs, expected in self.problem["tests"]:

            try:
                actual = function(*inputs)

                if actual == expected:
                    passed += 1
                    results.append("PASS")
                else:
                    results.append(
                        f"FAIL | Expected {expected}, Got {actual}"
                    )

            except Exception as error:
                results.append(f"ERROR | {error}")

        # Calculate reward / score
        total = len(self.problem["tests"])
        score = passed / total

        return {
            "score": score,
            "passed": passed,
            "total": total,
            "results": results
        }


# -------------------------------
# CREATE ENVIRONMENT
# -------------------------------

environment = CodingEnvironment("add_numbers")

print("TASK:")
print(environment.get_task())


# -------------------------------
# SIMULATED AI RESPONSE
# -------------------------------

model_code = """
def add_numbers(a, b):
    return a + b
"""
# model_code = """
# def add_numbers(a, b):
#     return a - b
# """

# -------------------------------
# EVALUATE CODE
# -------------------------------

result = environment.evaluate(model_code)

print("\nRESULT:")
print(result)