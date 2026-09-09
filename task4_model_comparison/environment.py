class CodingEnvironment:

    def __init__(self, function_name, tests):

        self.function_name = function_name
        self.tests = tests


    def evaluate(self, code):

        namespace = {}

        try:

            exec(code, namespace)

        except Exception as error:

            return {
                "score": 0.0,
                "passed": 0,
                "total": len(self.tests),
                "feedback": f"Code error: {error}"
            }


        if self.function_name not in namespace:

            return {
                "score": 0.0,
                "passed": 0,
                "total": len(self.tests),
                "feedback": (
                    f"Function '{self.function_name}' "
                    "was not found."
                )
            }


        function = namespace[self.function_name]

        passed = 0
        failures = []


        for inputs, expected in self.tests:

            try:

                actual = function(*inputs)

                if actual == expected:

                    passed += 1

                else:

                    failures.append(
                        f"Input {inputs}: "
                        f"expected {expected}, "
                        f"got {actual}"
                    )

            except Exception as error:

                failures.append(
                    f"Input {inputs}: "
                    f"error {error}"
                )


        score = passed / len(self.tests)


        return {
            "score": score,
            "passed": passed,
            "total": len(self.tests),
            "feedback": "\n".join(failures)
        }