from environment import CodingEnvironment
from parser import extract_code
from models import MODELS, generate_code
from problems import PROBLEMS


all_results = []


for requested_model in MODELS:

    print("\n" + "=" * 70)
    print("REQUESTED MODEL:")
    print(requested_model)
    print("=" * 70)

    model_scores = []
    actual_models = []

    for problem in PROBLEMS:

        print("\n" + "-" * 70)
        print("PROBLEM:")
        print(problem["name"])
        print("-" * 70)

        try:

            print("\nASKING MODEL...\n")

            model_result = generate_code(
                requested_model,
                problem["prompt"]
            )

            response = model_result["code"]
            actual_model = model_result["actual_model"]

            actual_models.append(actual_model)

            print("ACTUAL MODEL USED:")
            print(actual_model)

            print("\nRAW RESPONSE:\n")
            print(response)

            code = extract_code(response)

            print("\nPARSED CODE:\n")
            print(code)

            environment = CodingEnvironment(
                problem["function_name"],
                problem["tests"]
            )

            evaluation = environment.evaluate(code)

            print("\nRESULT:")
            print(f"Score: {evaluation['score']}")

            print(
                f"Passed: "
                f"{evaluation['passed']}/"
                f"{evaluation['total']}"
            )

            if evaluation["feedback"]:

                print("\nFEEDBACK:")
                print(evaluation["feedback"])

            model_scores.append(
                evaluation["score"]
            )

        except Exception as error:

            print("\nMODEL ERROR:")
            print(error)

            model_scores.append(0.0)


    average_score = sum(model_scores) / len(model_scores)


    all_results.append({
        "requested_model": requested_model,
        "actual_models": actual_models,
        "average_score": average_score,
        "problem_scores": model_scores
    })


print("\n" + "=" * 70)
print("FINAL MODEL RANKING")
print("=" * 70)


all_results.sort(
    key=lambda item: item["average_score"],
    reverse=True
)


for rank, result in enumerate(
    all_results,
    start=1
):

    print(f"\n🏆 RANK #{rank}")

    print(
        f"Requested Model: "
        f"{result['requested_model']}"
    )

    print(
        f"Average Score: "
        f"{result['average_score']:.2f}"
    )

    print(
        f"Percentage: "
        f"{result['average_score'] * 100:.1f}%"
    )

    print("\nProblem Scores:")

    for problem, score in zip(
        PROBLEMS,
        result["problem_scores"]
    ):

        print(
            f"{problem['name']}: "
            f"{score:.2f}"
        )

    print("\nActual Models Used:")

    unique_models = list(
        dict.fromkeys(result["actual_models"])
    )

    for model in unique_models:

        print(f"- {model}")