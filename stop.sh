
#!/bin/bash

# Make script strict. Will not fail silently. 
set -euo pipefail

CONTAINER_NAME="${CONTAINER_NAME:-mlops-project}"

echo "Stopping container: $CONTAINER_NAME (if running)"
docker stop "$CONTAINER_NAME" >/dev/null 2>&1 || true

echo "Removing container: $CONTAINER_NAME (if exists)"
docker rm   "$CONTAINER_NAME" >/dev/null 2>&1 || true

echo "Done."

# Deactivate conda env if inside one
if [[ "$CONDA_DEFAULT_ENV" != "" ]]; then
    conda deactivate
fi

# Deactivate conda env if inside one
if [[ "$CONDA_DEFAULT_ENV" != "" ]]; then
    conda deactivate
fi

# Original version
#!/bin/bash
#docker stop mlops-container && docker rm mlops-container
