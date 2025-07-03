# DOES DOWNLOAD STEP GIVE UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf8 in position 0: invalid start byte wandb: ERROR Internal wandb error: file data was not synced wandb: ERROR transport failed.

If you are encountering this error message when trying to run the download step, please

1) Make sure you have WSL installed and you are using an Ubuntu instance when trying to run the code if you are a Windows User

2) If you have a GPU, download the latest Nvidia driver

3) update wandb to version 0.17.2 in all conda.yml files

4) change the github links to point to your project repitory instead of udacity repository in config yaml and conda yml files

5) push your changes to github

Then try again!