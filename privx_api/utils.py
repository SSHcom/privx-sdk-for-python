from typing import Any


def get_value(obj: Any, default_value: Any) -> Any:
    return obj if obj is not None else default_value
