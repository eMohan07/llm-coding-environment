import verifiers as vf


def extract_code(text):
    """Extract Python code from a markdown response."""

    if "```python" in text:
        return text.split("```python")[1].split("```")[0].strip()

    if "```" in text:
        return text.split("```")[1].split("```")[0].strip()

    return text.strip()


code_parser = vf.Parser(extract_fn=extract_code)