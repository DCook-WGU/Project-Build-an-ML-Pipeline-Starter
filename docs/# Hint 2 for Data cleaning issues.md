# Hint 2 for Data cleaning issues
[Link] (https://knowledge.udacity.com/questions/1063620)

# Cleaned dataset not showing in wandb

I have tried to run mlflow . run -P steps=basic_cleaning multiple times in multiple ways, and I have gotten the same error. It is not uploading the cleaned file to wandb.

CODE:

> (nyc_airbnb_dev) @mcol887 ➜ /workspaces/Project-Build-an-ML-Pipeline-Starter (main) $ mlflow run . -P steps=basic_cleaning
> 
> /opt/conda/envs/nyc_airbnb_dev/lib/python3.10/site-packages/pydantic/_internal/_config.py:345: UserWarning: Valid config keys have changed in V2:
> 
> 'schema_extra' has been renamed to 'json_schema_extra'
> warnings.warn(message, UserWarning)
> 
> 2025/02/18 02:48:15 INFO mlflow.utils.conda: Conda environment mlflow-b0a0fa781f1d340bd66fdc33bb10c5da7db436d9 already exists.
> 
> 2025/02/18 02:48:15 INFO mlflow.projects.utils: === Created directory /tmp/tmptqi4038w for downloading remote URIs passed to arguments of type 'path' ===
> 
> 2025/02/18 02:48:15 INFO mlflow.projects.backend.local: === Running command 'source /opt/conda/bin/../etc/profile.d/conda.sh && conda activate mlflow-b0a0fa781f1d340bd66fdc33bb10c5da7db436d9 1>&2 && python main.py main.steps=\'basic_cleaning\' $(echo '')' in run with ID '8a8c1fa6ffd44c429be97634eb1d71ed' ===
> 
> /workspaces/Project-Build-an-ML-Pipeline-Starter/main.py:24: UserWarning:
> 
> The version_base parameter is not specified.
> 
> Please specify a compatability version level, or None.
> 
> Will assume defaults for version 1.1
> 
> @hydra.main(config_name='config')
> 
> /workspaces/Project-Build-an-ML-Pipeline-Starter/main.py:24: UserWarning:
> 
> config_path is not specified in @hydra.main().
> 
> See https://hydra.cc/docs/1.2/upgrades/1.0_to_1.1/changes_to_hydra_main_config_path for more information.
> 
> @hydra.main(config_name='config')
> 
> /opt/conda/envs/mlflow-b0a0fa781f1d340bd66fdc33bb10c5da7db436d9/lib/python3.10/site-packages/hydra/_internal/hydra.py:119: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
> 
> See https://hydra.cc/docs/1.2/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
> 
> ret = run_job(
> 
> 2025/02/18 02:48:19 INFO mlflow.projects: === Run (ID '8a8c1fa6ffd44c429be97634eb1d71ed') succeeded ===


As per our discussion in the comments thread, the main.py file needs to be edited to ensure the basic cleaning step is run. Just in case, it should look something like the following:

>   if "basic_cleaning" in active_steps:
>            mlflow.run(
>            os.path.join(hydra.utils.get_original_cwd(), "src", "basic_cleaning"),
>            entry_point="main",
>            parameters={
>                "input_artifact": "sample.csv:latest",  
>                "output_artifact": "clean_sample.csv",
>                "output_type": "cleaned_data",
>                "output_description": "Cleaned dataset after basic preprocessing",
>                "min_price": config["etl"]["min_price"],
>                "max_price": config["etl"]["max_price"],
>            },
>        )

Take special care to access the config dictionary that reads in the config.yaml file that's in the main directory. It is parsed by the hydra framework.