def execute_code(code):

    namespace = {}

    try:

        exec(code, namespace)

        return {
            "success": True,
            "namespace": namespace
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }