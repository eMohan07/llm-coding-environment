from environment import MultiTurnEnvironment
from llm import generate_code
from parser import extract_code


environment = MultiTurnEnvironment()

MAX_TURNS = 3


problem = """
Write a Python function called is_palindrome(text).

Requirements:
- Return True if the text is a palindrome.
- Return False otherwise.

Return only Python code.
"""


feedback = ""


for turn in range(MAX_TURNS):

    print("\n" + "=" * 50)
    print(f"TURN {turn + 1}")
    print("=" * 50)

    prompt = problem

    if turn == 0:
        prompt += """

For your first attempt, use the simplest implementation
based on direct string reversal.
"""

    if feedback:
        prompt += "\n\nYour previous implementation failed tests."
        prompt += "\n\nENVIRONMENT FEEDBACK:\n"
        prompt += feedback
        prompt += "\n\nFix ALL issues identified."
        prompt += "\nReturn only Python code."

    print("\nASKING MODEL...\n")

    model_response = generate_code(prompt)

    print("RAW MODEL RESPONSE:\n")
    print(model_response)

    code = extract_code(model_response)

    print("\nPARSED CODE:\n")
    print(code)

    result = environment.evaluate(code)

    print("\nSCORE:")
    print(result["score"])

    print("\nFEEDBACK:")
    print(result["feedback"])

    if result["success"]:
        print("\nSUCCESS!")
        print(f"Code solved in {turn + 1} turn(s)")
        break

    feedback = result["feedback"]

else:
    print("\nFAILED!")
    print("Maximum turns reached.")