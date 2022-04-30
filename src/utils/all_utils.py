import yaml
import os

def read_yaml(path : str) -> dict:
    with open(path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    
    return content

def create_directory(dirs : list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory {dir_path}")
