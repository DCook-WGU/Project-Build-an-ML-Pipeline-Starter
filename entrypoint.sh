#!/bin/bash

# Load Conda
source /opt/miniconda/etc/profile.d/conda.sh

# Add auto-activation to .bashrc if it's not already there
grep -qxF 'conda activate mlops' ~/.bashrc || echo 'conda activate mlops' >> ~/.bashrc

# Activate it now (for current session)
conda activate mlops

# Log in to Weights & Biases
if [ -n "$WANDB_API_KEY" ]; then
    wandb login "$WANDB_API_KEY"
fi

# Launch interactive shell or passed command
exec "$@"
