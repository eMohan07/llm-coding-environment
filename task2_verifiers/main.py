from coding_env import VerifierCodingEnvironment


environment = VerifierCodingEnvironment()


model_response = """

Here is my solution:

```python

def add_numbers(a, b):
    return a + b


```"""

result = environment.evaluate(model_response)

print("\nPARSED CODE:")

print(result["code"])

print("\nSCORES:")

print("Syntax Score:", result["syntax_score"])

print("Function Score:", result["function_score"])

print("Correctness Score:", result["correctness_score"])

print("Final Score:", result["final_score"])