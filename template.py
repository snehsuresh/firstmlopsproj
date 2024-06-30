import os
from pathlib import Path #Will correct your path according to os

list_of_files = [
    ".github/workflows/.gitkeep",  # Config for CI/CD pipeline
    "src/__init__.py",  # Indicates 'src' as a Python package
    "src/components/__init__.py",  # Indicates 'components' as a Python package
    "src/components/data_ingestion.py",  # Script for data ingestion processes
    "src/components/data_transformation.py",  # Script for data transformation processes
    "src/components/model_trainer.py",  # Script for model training processes
    "src/components/model_evaluation.py",  # Script for model evaluation processes
    "src/pipeline/__init__.py",  # Indicates 'pipeline' as a Python package
    "src/pipeline/training_pipeline.py",  # Script for the training pipeline
    "src/pipeline/prediction_pipeline.py",  # Script for the prediction pipeline
    "src/utils/__init__.py",  # Indicates 'utils' as a Python package
    "src/utils/utils.py",  # Utility functions used across the project
    "src/logger/logging.py",  # Logging configuration and functions
    "src/exception/exception.py",  # Custom exception handling classes
    "tests/unit/__init__.py",  # Indicates 'unit' as a Python package for unit tests
    "tests/integration/__init__.py",  # Indicates 'integration' as a Python package for integration tests
    "init_setup.sh",  # Shell script to initialize the project setup
    "requirements.txt",  # List of main dependencies for the project
    "requirements_dev.txt",  # List of development dependencies
    "setup.py",  # Script for installing the package
    "setup.cfg",  # Configuration for the setup script
    "pyproject.toml",  # Configuration for the build system
    "tox.ini",  # Configuration for Tox testing tool
    "experiment/experiments.ipynb"  # Jupyter notebook for experiments
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

