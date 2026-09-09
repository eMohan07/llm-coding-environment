PROBLEMS = [

    {
        "name": "Palindrome",

        "function_name": "is_palindrome",

        "prompt": """
Write a Python function called is_palindrome(text).

Requirements:
- Return True if the text is a palindrome.
- Return False otherwise.
- Ignore uppercase/lowercase differences.
- Ignore spaces and punctuation.

Return only Python code.
""",

        "tests": [
            (("madam",), True),
            (("racecar",), True),
            (("hello",), False),
            (("Madam",), True),
            (("A man, a plan, a canal: Panama",), True)
        ]
    },


    {
        "name": "Factorial",

        "function_name": "factorial",

        "prompt": """
Write a Python function called factorial(n).

Requirements:
- Return the factorial of n.
- factorial(0) should return 1.

Return only Python code.
""",

        "tests": [
            ((0,), 1),
            ((1,), 1),
            ((5,), 120),
            ((7,), 5040)
        ]
    },


    {
        "name": "Prime Number",

        "function_name": "is_prime",

        "prompt": """
Write a Python function called is_prime(n).

Requirements:
- Return True if n is a prime number.
- Return False otherwise.
- Numbers less than 2 are not prime.

Return only Python code.
""",

        "tests": [
            ((2,), True),
            ((3,), True),
            ((4,), False),
            ((17,), True),
            ((1,), False),
            ((0,), False)
        ]
    },


    {
        "name": "Remove Duplicates",

        "function_name": "remove_duplicates",

        "prompt": """
Write a Python function called remove_duplicates(items).

Requirements:
- Remove duplicate items from a list.
- Preserve the original order.

Example:
remove_duplicates([1, 2, 2, 3, 1])

should return:

[1, 2, 3]

Return only Python code.
""",

        "tests": [
            (([1, 2, 2, 3, 1],), [1, 2, 3]),
            ((["a", "b", "a"],), ["a", "b"]),
            (([],), []),
            (([1, 1, 1],), [1])
        ]
    },


    {
        "name": "Fibonacci",

        "function_name": "fibonacci",

        "prompt": """
Write a Python function called fibonacci(n).

Requirements:
- Return the nth Fibonacci number.
- fibonacci(0) should return 0.
- fibonacci(1) should return 1.

Return only Python code.
""",

        "tests": [
            ((0,), 0),
            ((1,), 1),
            ((5,), 5),
            ((10,), 55)
        ]
    }

]