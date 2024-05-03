import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s : %(levelname)-s] : %(message)s"
)

while True:
    project_name = input("Enter the project name: ")

    if project_name != '':
        break

logging.info(f"Creating directory for {project_name}")

list_of_files = [
    # GitHub directory where action files can be stored
    ".github/workflows/.gitkeep",
    # Your other files
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",  # Fixed typo here
    "init_setup.sh",
    "requirements.txt",  # Corrected typo here
    # Requirements dev file only used for testing (pytest)
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")

    if (not  os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filename, 'w' ) as f:
            pass
            logging.info(f"Created an NEW file : {filename} at path : {filepath}")

    else:
        logging.info(f"File {filepath} already exists")

    

