#!/bin/bash
docker stop mlops-container && docker rm mlops-container
docker build -t mlops-dev .
