def extract_code(response):

    if "```python" in response:
        code = response.split("```python")[1]
        code = code.split("```")[0]
        return code.strip()

    if "```" in response:
        code = response.split("```")[1]
        code = code.split("```")[0]
        return code.strip()

    return response.strip()