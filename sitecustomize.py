import warnings

# Kill MLflow gateway deprecation early, no Pydantic import needed
warnings.filterwarnings(
    "ignore",
    message=r"Support for class-based `config` is deprecated.*"
)
warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    module=r"mlflow(\.|$)"
)

# Optional Warning, enabling for now
# Quiet any FutureWarnings inside mlflow
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    module=r"mlflow(\.|$)"
)

try:
    from pydantic.warnings import (
        UnsupportedFieldAttributeWarning,
        PydanticDeprecatedSince20,
    )
    warnings.filterwarnings("ignore", category=UnsupportedFieldAttributeWarning)
    warnings.filterwarnings("ignore", category=PydanticDeprecatedSince20)
except Exception:
    pass

