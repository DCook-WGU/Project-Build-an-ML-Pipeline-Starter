# Hint 1 for data cleaning issues 
[link](https://knowledge.udacity.com/questions/1059727)

## Trouble with basic cleaning
    
Having trouble with basic cleaning after several updates, push commits

> (‌base) root@DESKTOP-8MJM1NE:~/Project-Build-an-ML-Pipeline-Starter# mlflow run . -P steps=basic_cleaning
> 2025/01/05 18:22:15 INFO mlflow.utils.conda: Conda environment mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17 already exists.
> 2025/01/05 18:22:15 INFO mlflow.projects.utils: === Created directory /tmp/tmprda0ivoo for downloading remote URIs passed to arguments of type 'path' ===
> 2025/01/05 18:22:15 INFO mlflow.projects.backend.local: === Running command 'source /root/miniconda3/bin/../etc/profile.d/conda.sh && conda activate mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17 1>&2 && python main.py main.steps=\'basic_cleaning\' $(echo '')' in run with ID '5162724dbf22453690b538815935f1d3' === 
> /root/Project-Build-an-ML-Pipeline-Starter/main.py:23: UserWarning: 
> The version_base parameter is not specified.
> Please specify a compatability version level, or None.
> Will assume defaults for version 1.1
>   @hydra.main(config_name='config')
> /root/Project-Build-an-ML-Pipeline-Starter/main.py:23: UserWarning: 
> config_path is not specified in @hydra.main().
> See https://hydra.cc/docs/1.2/upgrades/1.0_to_1.1/changes_to_hydra_main_config_path for more information.
>   @hydra.main(config_name='config')
> /root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/hydra/_internal/hydra.py:119: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
> See https://hydra.cc/docs/1.2/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
>   ret = run_job(
> 2025/01/05 18:22:21 INFO mlflow.projects.utils: === Fetching project from src/basic_cleaning into /tmp/tmp7qspd6ag ===
> Error executing job with overrides: ["main.steps='basic_cleaning'"]
> Traceback (most recent call last):
>   File "/root/Project-Build-an-ML-Pipeline-Starter/main.py", line 54, in go
>     mlflow.run(
>   File "/root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/mlflow/projects/__init__.py", line 337, in run
>     submitted_run_obj = _run(
>   File "/root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/mlflow/projects/__init__.py", line 106, in _run
>     submitted_run = backend.run(
>   File "/root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/mlflow/projects/backend/local.py", line 80, in run
>     work_dir = fetch_and_validate_project(project_uri, version, entry_point, params)
>   File "/root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/mlflow/projects/utils.py", line 138, in fetch_and_validate_project
>     work_dir = _fetch_project(uri=uri, version=version)
>   File "/root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/mlflow/projects/utils.py", line 172, in _fetch_project
>     _fetch_git_repo(parsed_uri, version, dst_dir)
>   File "/root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/mlflow/projects/utils.py", line 222, in _fetch_git_repo
>     output = g.execute(cmd)
>   File "/root/miniconda3/envs/mlflow-8daaa939c70c525a14ed7896f7dc54ec79b6ca17/lib/python3.10/site-packages/git/cmd.py", line 1388, in execute
>     raise GitCommandError(redacted_command, status, stderr_value, stdout_value)
> git.exc.GitCommandError: Cmd('git') failed due to: exit code(128)
>   cmdline: git remote show origin
>   stderr: 'fatal: 'src/basic_cleaning' does not appear to be a git repository
> fatal: Could not read from remote repository.
> Please make sure you have the correct access rights
> and the repository exists.'
> Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
> 2025/01/05 18:22:22 ERROR mlflow.cli: === Run (ID '5162724dbf22453690b538815935f1d3') failed ===

[Github or Project Link](https://github.com/etrev17/Project-Build-an-ML-Pipeline-Starter)


The path to the basic cleaning module is incorrect: [Line55](https://github.com/etrev17/Project-Build-an-ML-Pipeline-Starter/blob/main/main.py#L55)


Please change it to

> os.path.join(hydra.utils.get_original_cwd(), "src", "basic_cleaning")

You'll need to do the same for the other modules. Notice that the first step, the download step does this in a similar way. Repeat the same pattern for the other modules.