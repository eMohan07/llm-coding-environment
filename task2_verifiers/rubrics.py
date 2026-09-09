def syntax_rubric(code):

    try:
        compile(code, "<generated_code>", "exec")
        return 1.0

    except SyntaxError:
        return 0.0


def function_rubric(code, function_name):

    namespace = {}

    try:
        exec(code, namespace)

        if function_name in namespace:
            return 1.0

        return 0.0

    except Exception:
        return 0.0


def correctness_rubric(code, function_name, tests):

    namespace = {}

    try:
        exec(code, namespace)

        function = namespace[function_name]

    except Exception:
        return 0.0

    passed = 0

    for inputs, expected in tests:

        try:

            actual = function(*inputs)

            if actual == expected:
                passed += 1

        except Exception:
            pass

    return passed / len(tests)