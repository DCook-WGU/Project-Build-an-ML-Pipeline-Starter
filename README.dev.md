
# MLOps Dev Container Setup for Udacity D501

This repository contains a fully containerized development environment for the Udacity D501 Machine Learning DevOps project, using Docker, Conda, and VS Code Remote Containers.

---

## 🚀 Features

- Ubuntu-based Docker container (Ubuntu 22.04)
- Miniconda installed manually
- Conda environment named `mlops` using `environment.yml`
- Integrated with Weights & Biases (W&B)
- Remote development via VS Code
- Git identity and config handled automatically
- Workspace support via `.code-workspace`

---

## 📁 Folder Structure

```bash
Project-Build-an-ML-Pipeline-Starter/
├── .devcontainer/
│   └── devcontainer.json
├── .dockerignore
├── Dockerfile
├── environment.yml
├── mlops.code-workspace
├── start.sh
├── stop.sh
├── rebuild.sh
├── [Project Files]
```

---

## 🛠 Setup Instructions

### 1. 🔁 First-Time Setup

Ensure Docker Desktop, WSL 2, and VS Code are installed.

1. Clone this repo to your desired directory (e.g., D: drive)
2. Open WSL Ubuntu and navigate to the project folder:
   ```bash
   cd /mnt/d/wgu/d501/Project-Build-an-ML-Pipeline-Starter
   ```
3. Give execute permissions to the helper scripts:
   ```bash
   chmod +x start.sh stop.sh rebuild.sh
   ```
4. Launch the container:
   ```bash
   ./start.sh
   ```

### 2. 🧠 W&B API Key Setup

Add the following to your Ubuntu `~/.bashrc` to avoid hardcoding:
```bash
export WANDB_API_KEY=your-api-key-here
```
Then reload:
```bash
source ~/.bashrc
```

---

## 📦 Dev Container Configuration

### `.devcontainer/devcontainer.json`

Handles:
- Image usage
- Volume mounting
- Environment variable injection
- Post-create Git config
- Extensions & interpreter

### `mlops.code-workspace`

Ensures:
- Project folder is recognized
- Python interpreter path is set
- Recommended extensions are preloaded

---

## 🔧 Useful Commands

| Command        | Purpose                         |
|----------------|---------------------------------|
| `./start.sh`   | Start the container + mount app |
| `./stop.sh`    | Stop and remove the container   |
| `./rebuild.sh` | Rebuild the Docker image        |

---

## 🔄 Rebuilding the Container

To rebuild from scratch:
```bash
./stop.sh && ./rebuild.sh && ./start.sh
```

---

## ✅ Verification

Once inside the container (you should see `(mlops)`):
```bash
which python
conda info --envs
wandb --version
```

All should reflect the expected paths and versions.

---

## 🧪 Next Steps

- Run the project pipeline step-by-step
- Integrate experiment tracking with W&B
- Start customizing configs in `config.yaml`
- Explore modular components in `components/`

---

> 🐳 To set up the full development environment using Docker and VS Code, see [README.dev.md](README.dev.md)

---

## 🙌 Credits

Setup based on Udacity D501 Machine Learning DevOps content.

Contributed by: [Danty Cook](https://github.com/DCook-WGU)
