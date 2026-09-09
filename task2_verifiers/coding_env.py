import verifiers as vf

from parser import code_parser


FUNCTION_NAME = "add_numbers"

TESTS = [
    ((2, 3), 5),
    ((10, 20), 30),
    ((-5, 5), 0)
]


async def syntax_reward(completion, parser):

    code = parser.parse_answer(completion)

    try:
        compile(code, "<generated_code>", "exec")
        return 1.0

    except Exception:
        return 0.0


async def function_reward(completion, parser):

    code = parser.parse_answer(completion)

    namespace = {}

    try:
        exec(code, namespace)

        return float(FUNCTION_NAME in namespace)

    except Exception:
        return 0.0


async def correctness_reward(completion, parser):

    code = parser.parse_answer(completion)

    namespace = {}

    try:
        exec(code, namespace)

        function = namespace[FUNCTION_NAME]

    except Exception:
        return 0.0

    passed = 0

    for inputs, expected in TESTS:

        try:

            actual = function(*inputs)

            if actual == expected:
                passed += 1

        except Exception:
            pass

    return passed / len(TESTS)


rubric = vf.Rubric(
    funcs=[
        syntax_reward,
        function_reward,
        correctness_reward
    ],

    weights=[
        0.2,
        0.2,
        0.6
    ],

    parser=code_parser
)