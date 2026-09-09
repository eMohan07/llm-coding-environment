from problems import PROBLEMS
from parser import extract_code
from evaluator import evaluate_function


class CodingEnvironment:

    def __init__(self, problem_name):

        self.problem = PROBLEMS[problem_name]

    def get_task(self):

        return self.problem["description"]

    def evaluate(self, model_response):

        code = extract_code(model_response)

        result = evaluate_function(

            code=code,

            function_name="is_prime",

            tests=self.problem["tests"]

        )

        return result