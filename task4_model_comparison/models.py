import os
from openai import OpenAI


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


MODELS = [
    "openai/gpt-4o-mini",
    "openrouter/free",
    "openrouter/free"
]


def generate_code(model, prompt):

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "code": response.choices[0].message.content,
        "actual_model": response.model
    }