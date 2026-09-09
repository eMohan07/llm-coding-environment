class MultiTurnEnvironment:

    def __init__(self):
        self.function_name = "is_palindrome"

        self.tests = [
            (("madam",), True),
            (("racecar",), True),
            (("hello",), False),
            (("Madam",), True),
            (("A man, a plan, a canal: Panama",), True)
        ]


    def evaluate(self, code):

        namespace = {}

        try:
            exec(code, namespace)

        except Exception as error:
            return {
                "success": False,
                "score": 0.0,
                "feedback": f"Code error: {error}"
            }

        if self.function_name not in namespace:
            return {
                "success": False,
                "score": 0.0,
                "feedback": (
                    f"Function '{self.function_name}' "
                    "was not found."
                )
            }

        function = namespace[self.function_name]

        passed = 0
        failed_tests = []

        for inputs, expected in self.tests:

            try:
                actual = function(*inputs)

                if actual == expected:
                    passed += 1

                else:
                    failed_tests.append(
                        f"Input {inputs}: "
                        f"expected {expected}, "
                        f"got {actual}"
                    )

            except Exception as error:
                failed_tests.append(
                    f"Input {inputs}: error {error}"
                )

        score = passed / len(self.tests)

        if score == 1.0:
            return {
                "success": True,
                "score": score,
                "feedback": "All tests passed!"
            }

        feedback = "Some tests failed:\n"
        feedback += "\n".join(failed_tests)
        feedback += "\n\nFix your code based on these failures."

        return {
            "success": False,
            "score": score,
            "feedback": feedback
        }