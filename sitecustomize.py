import warnings
try:
    from pydantic.warnings import (
        UnsupportedFieldAttributeWarning,
        PydanticDeprecatedSince20,
    )
    warnings.filterwarnings("ignore", category=UnsupportedFieldAttributeWarning)
    warnings.filterwarnings("ignore", category=PydanticDeprecatedSince20)
except Exception:
    pass