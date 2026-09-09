from parser import extract_code

from rubrics import (
    syntax_rubric,
    function_rubric,
    correctness_rubric
)


class VerifierCodingEnvironment:

    def __init__(self):

        self.function_name = "add_numbers"

        self.tests = [

            ((2, 3), 5),

            ((10, 20), 30),

            ((-5, 5), 0)

        ]

    def evaluate(self, model_response):

        # Parse AI response
        code = extract_code(model_response)

        # Run rubrics
        syntax_score = syntax_rubric(code)

        function_score = function_rubric(
            code,
            self.function_name
        )

        correctness_score = correctness_rubric(
            code,
            self.function_name,
            self.tests
        )

        # Combine rubric scores
        final_score = (

            syntax_score * 0.2

            +

            function_score * 0.2

            +

            correctness_score * 0.6

        )

        return {

            "code": code,

            "syntax_score": syntax_score,

            "function_score": function_score,

            "correctness_score": correctness_score,

            "final_score": final_score

        }