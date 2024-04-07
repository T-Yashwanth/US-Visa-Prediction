import os
from pathlib import Path

project_name = "us_visa_prediction"

list_of_folders = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/s3.operations.py", # need to be removed or renamed
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/usvisa_data.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "config/model.yaml",
    "config/schema.yamal"
]

for filepath in list_of_folders:
    filepath = Path(filepath)
    filedirectory, filename = os.path.split(filepath)

    if filedirectory != "":
        os.makedirs(filedirectory, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file already exist {filename} at {filedirectory}")
