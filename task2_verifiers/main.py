import asyncio

from parser import code_parser
from coding_env import (
    syntax_reward,
    function_reward,
    correctness_reward
)

model_response = "def add_numbers(a, b):\n    return a + b"


async def evaluate():
    print("MODEL RESPONSE:")
    print(model_response)

    syntax_score = await syntax_reward(
        model_response,
        code_parser
    )

    function_score = await function_reward(
        model_response,
        code_parser
    )

    correctness_score = await correctness_reward(
        model_response,
        code_parser
    )

    final_score = (
        syntax_score * 0.2
        + function_score * 0.2
        + correctness_score * 0.6
    )

    print("\nPARSED CODE:")
    print(model_response)

    print("\nSCORES:")
    print("Syntax Score:", syntax_score)
    print("Function Score:", function_score)
    print("Correctness Score:", correctness_score)
    print("Final Score:", final_score)


if __name__ == "__main__":
    asyncio.run(evaluate())