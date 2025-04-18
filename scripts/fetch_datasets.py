import yaml
import os
import subprocess
import sys

config_file = sys.argv[1]
output_dir = sys.argv[2]

with open(config_file) as f:
    config = yaml.safe_load(f)

for dataset in config['datasets']:
    source = dataset['source']
    for filename in dataset['files']:
        full_path = f"{source}/{filename}"
        print(f"Downloading {full_path}...")
        subprocess.run(["gsutil", "cp", full_path, output_dir], check=True)
