import os
from pathlib import Path #Will correct your path according to os

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]


for path in list_of_files:
    path = Path(path)  # Remove any leading/trailing whitespace
    filedir, filename = os.path.split(path)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        # logging.info(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(path)) or (os.path.getsize(path)==0):
        with open(path, "w") as f:
            pass #create empty file

