# Build an ML Pipeline for Short-Term Rental Prices in NYC

You are working for a property management company renting rooms and properties for short periods of 
time on various rental platforms. You need to estimate the typical price for a given property based 
on the price of similar properties. Your company receives new data in bulk every week. The model needs 
to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

In this project you will build such a pipeline.

## Table of contents

- [Preliminary steps](#preliminary-steps)
  * [Fork the Starter Kit](#fork-the-starter-kit)
  * [Create environment](#create-environment)
  * [Quick Start (First-Time Setup)](#quick-start-first-time-setup)
  * [Get API key for Weights and Biases](#get-api-key-for-weights-and-biases)
  * [The configuration](#the-configuration)
  * [Running the entire pipeline or just a selection of steps](#Running-the-entire-pipeline-or-just-a-selection-of-steps)
  * [Pre-existing components](#pre-existing-components)
  * [Rebuild vs Start — Which Script to Use?](#rebuild-vs-start--which-script-to-use)
  * [Useful Commands Summary](#useful-commands-summary)
  * [Public Links](#public-links)

---

## Preliminary steps

### Supported Operating Systems

This project is compatible with the following operating systems:

- **Ubuntu 22.04** (Jammy Jellyfish) - both Ubuntu installation and WSL (Windows Subsystem for Linux)
- **Ubuntu 24.04** - both Ubuntu installation and WSL (Windows Subsystem for Linux)
- **macOS** - compatible with recent macOS versions

Please ensure you are using one of the supported OS versions to avoid compatibility issues.

### Python Requirement

This project requires **Python 3.10**. Please ensure that you have Python 3.10 installed and set as the default version in your environment to avoid any runtime issues.

---

### Using WSL and Docker (Recommended Setup)

For consistent development across systems, this project supports running inside a **Docker container on WSL2**.

#### Prerequisites (Windows)
1. Enable WSL2 and install Ubuntu 22.04:
   ```bash
   wsl --install
   ```
2. Install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop).
   - Enable “Use the WSL 2 based engine”
   - Enable “Integrate with my default WSL distro (Ubuntu)”
3. Verify Docker works inside WSL:
   ```bash
   docker run hello-world
   ```

#### macOS and Linux
Docker runs natively. Ensure Docker Engine is installed and running before proceeding.

---

### Fork the Starter kit
Go to [https://github.com/udacity/Project-Build-an-ML-Pipeline-Starter](https://github.com/udacity/Project-Build-an-ML-Pipeline-Starter)
and click on `Fork` in the upper right corner. This will create a fork in your Github account, i.e., a copy of the
repository that is under your control. Now clone the repository locally so you can start working on it:

```bash
git clone https://github.com/[your github username]/Project-Build-an-ML-Pipeline-Starter.git
```

and go into the repository:

```bash
cd Project-Build-an-ML-Pipeline-Starter
```

Commit and push to the repository often while you make progress towards the solution. Remember 
to add meaningful commit messages.

---

### Create Environment (Using Docker)

Instead of manually creating a Conda environment, this project provides a script to build and launch a Docker container with the full setup.

From your Ubuntu (WSL) or macOS/Linux terminal:

```bash
# Navigate to the folder where you cloned the repository
cd Project-Build-an-ML-Pipeline-Starter

# Build the Docker image and start the container
./rebuild.sh
```

This script will:
1. Stop and remove any old container (if it exists)
2. Build a new Docker image using the included Dockerfile
3. Start a container in the background
4. Print a command you can use to connect to the container

Once complete, connect to your running container:
```bash
docker exec -it mlops-project bash
```

Then activate the Conda environment inside the container:
```bash
conda activate mlops-dev-project
```

Your environment is now ready for MLflow and W&B usage.

---

### Quick Start (First-Time Setup)

If this is your first time setting up the project, follow these steps:

```bash
# 1. Clone this repository
git clone https://github.com/DCook-WGU/Project-Build-an-ML-Pipeline-Starter.git
cd Project-Build-an-ML-Pipeline-Starter

# 2. Build and start the container
./rebuild.sh

# 3. Enter the running container
docker exec -it mlops-project bash

# 4. Activate the environment (It should auto activate this env for you, but just in case.)
conda activate mlops-dev-project

# 5. Run the pipeline
mlflow run .
```

---

### Get API key for Weights and Biases
Let's make sure we are logged in to Weights & Biases. Get your API key from W&B by going to 
[https://wandb.ai/authorize](https://wandb.ai/authorize) and click on the + icon (copy to clipboard), 
then paste your key into this command:

```bash
wandb login [your API key]
```

You should see a message similar to:
```
wandb: Appending key for api.wandb.ai to your netrc file: /home/[your username]/.netrc
```

> NOTE: If you do not add your W&B API key here, it will not break the system. You will be prompted to on the first to either create a new account or connect to an existing account. When prompted you can input 2 and hit enter. Then you will be prompted to copy and paste your API key. 

---

### The configuration
As usual, the parameters controlling the pipeline are defined in the ``config.yaml`` file defined in
the root of the starter kit. We will use Hydra to manage this configuration file. 
Open this file and get familiar with its content. Remember: this file is only read by the ``main.py`` script 
(i.e., the pipeline) and its content is
available with the ``go`` function in ``main.py`` as the ``config`` dictionary. For example,
the name of the project is contained in the ``project_name`` key under the ``main`` section in
the configuration file. It can be accessed from the ``go`` function as 
``config["main"]["project_name"]``.

NOTE: do NOT hardcode any parameter when writing the pipeline. All the parameters should be 
accessed from the configuration file.

---

### Running the entire pipeline or just a selection of steps
In order to run the pipeline when you are developing, you need to be in the root of the starter kit, 
then you can execute as usual:

```bash
mlflow run .
```
This will run the entire pipeline.

When developing it is useful to be able to run one step at the time. Say you want to run only
the ``download`` step. The `main.py` is written so that the steps are defined at the top of the file, in the 
``_steps`` list, and can be selected by using the `steps` parameter on the command line:

```bash
mlflow run . -P steps=download
```
If you want to run the ``download`` and the ``basic_cleaning`` steps, you can similarly do:
```bash
mlflow run . -P steps=download,basic_cleaning
```
You can override any other parameter in the configuration file using the Hydra syntax, by
providing it as a ``hydra_options`` parameter. For example, say that we want to set the parameter
modeling -> random_forest -> n_estimators to 10 and etl->min_price to 50:

```bash
mlflow run . \
  -P steps=download,basic_cleaning \
  -P hydra_options="modeling.random_forest.n_estimators=10 etl.min_price=50"
```

---

### Pre-existing components
In order to simulate a real-world situation, we are providing you with some pre-implemented
re-usable components. While you have a copy in your fork, you will be using them from the original
repository by accessing them through their GitHub link, like:

```python
_ = mlflow.run(
                f"{config['main']['components_repository']}/get_data",
                "main",
                version='main',
                env_manager="conda",
                parameters={
                    "sample": config["etl"]["sample"],
                    "artifact_name": "sample.csv",
                    "artifact_type": "raw_data",
                    "artifact_description": "Raw file as downloaded"
                },
            )
```

where `config['main']['components_repository']` is set to 
[https://github.com/udacity/Project-Build-an-ML-Pipeline-Starter/tree/main/components](https://github.com/udacity/Project-Build-an-ML-Pipeline-Starter/tree/main/components).

You can see the parameters that they require by looking into their `MLproject` file:

- `get_data`: downloads the data. [MLproject](https://github.com/udacity/Project-Build-an-ML-Pipeline-Starter/blob/main/components/get_data/MLproject)
- `train_val_test_split`: segregate the data (splits the data) [MLproject](https://github.com/udacity/Project-Build-an-ML-Pipeline-Starter/blob/main/components/train_val_test_split/MLproject)

---

## 🧠 Rebuild vs Start — Which Script to Use?

| Script | Builds Image? | Removes Old Container? | Runs Interactively? | Use When |
|--------|----------------|------------------------|---------------------|----------|
| **`./rebuild.sh`** | ✅ Yes | ✅ Yes | 💤 Detached (background) | First-time setup or after Dockerfile/environment changes |
| **`./start.sh`** | ❌ No | ❌ No | ✅ Interactive (`-it`) | Reusing an existing image for daily development |

### Common Workflows

**First-Time Setup**
```bash
./rebuild.sh
docker exec -it mlops-project bash
conda activate mlops-dev-project
```

> Note: It should auto activate the conda env, but if it doesn't then use the command above.

**Daily Use (No rebuild needed)**
```bash
./start.sh
```

---

## 📦 Useful Commands Summary

| Task | Command |
|------|----------|
| Build & start container | `./rebuild.sh` |
| Enter running container | `docker exec -it mlops-project bash` |
| Restart without rebuild | `./start.sh` |
| Run pipeline | `mlflow run .` |
| Check Conda env | `conda env list` |
| View W&B runs | [https://wandb.ai](https://wandb.ai) |

---

## Public Links

- **GitHub Repository:** [https://github.com/DCook-WGU/Project-Build-an-ML-Pipeline-Starter](https://github.com/DCook-WGU/Project-Build-an-ML-Pipeline-Starter)  
- **Latest Release:** [https://github.com/DCook-WGU/Project-Build-an-ML-Pipeline-Starter/releases/latest](https://github.com/DCook-WGU/Project-Build-an-ML-Pipeline-Starter/releases/latest)  
- **Weights & Biases Project: Submission for grading** [https://wandb.ai/dcoo230-western-governors-university/nyc_airbnb?nw=nwuserdcoo230](https://wandb.ai/dcoo230-western-governors-university/nyc_airbnb?nw=nwuserdcoo230)
- **Weights & Biases Project: Testing work** [https://wandb.ai/dcoo230-western-governors-university/nyc_airbnb_original?nw=nwuserdcoo230](https://wandb.ai/dcoo230-western-governors-university/nyc_airbnb_original?nw=nwuserdcoo230)

> Make sure your W&B project is **public** (Settings → Access → Public).  
> Reviewers must be able to open this link without logging in.

> NOTE: I am unable to make my project public, my trial expired prior to being able to complete the class and I had to apply for an academic account extension. This unfortuately made my account attached to a team, "dcoo230-western-governors-university-org", and I am unable to change privacy/visibility to anything other than "Team" or "Restricted". I tried created a new account this time set to "Student" as the organization/institute with "Personal" as the account type, and it still restricted the "Public" access. This feature now appears to be behind a pay-wall. 

> Note: Inside the /docs/WeightsAndBiases-Exports directory, I included screenshots of my runs, the train random forest table view, my artifact linage's graph view with and without expanded history, the project profile page, the edit project panel (Where you can see public is not available), and a csv export of my data. 




---


## License

[License](LICENSE.txt)
