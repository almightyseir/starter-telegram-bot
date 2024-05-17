import os
import subprocess

# Set the path to the bash script
bash_script_path = "./run.sh"

# Check if the bash script exists
if not os.path.exists(bash_script_path):
    print(f"The bash script '{bash_script_path}' does not exist.")
    exit(1)

# Give permission to execute the bash script
os.chmod(bash_script_path, 0o755)

# Run the bash script
try:
    subprocess.run([bash_script_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    exit(1)
