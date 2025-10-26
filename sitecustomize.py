import warnings


# TODO(issue #12): Investigate remaining MLflow PydanticDeprecatedSince20 warning.
#  This warning appears once during MLflow startup (mlflow.gateway.config)
#  and may require deeper upstream patching or waiting for MLflow to update
#  its internal Pydantic model definitions.

# Catch by exact message (robust even if category changes)
warnings.filterwarnings(
    "ignore",
    message=r"Support for class-based [`']config[`'] is deprecated.*"
)

# Catch anything Pydantic emits in its internals (emitter module)
warnings.filterwarnings(
    "ignore",
    category=Warning,
    module=r"pydantic(\.|$)"
)
warnings.filterwarnings(
    "ignore",
    category=Warning,
    module=r"pydantic\._internal\._generate_schema"
)

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

