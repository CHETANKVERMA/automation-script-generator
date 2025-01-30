def validate_input(step):
    """Validates if the input step is a non-empty string."""
    return isinstance(step, str) and len(step.strip()) > 0
