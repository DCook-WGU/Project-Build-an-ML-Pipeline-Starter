#!/bin/bash

# Optional: Export your API key once per shell session
# export WANDB_API_KEY=your-api-key-here

docker run -it \
  --name mlops-container \
  -v $(pwd):/app \
  -e WANDB_API_KEY=$WANDB_API_KEY \
  mlops-dev
