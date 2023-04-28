
import os

# Define the directories and subdirectories for the project
project_dir = 'Real-time Data Processing with Streamlit and AWS Kinesis'
data_dir = os.path.join(project_dir, 'data')
scripts_dir = os.path.join(project_dir, 'scripts')
streamlit_dir = os.path.join(project_dir, 'streamlit')
db_dir = os.path.join(project_dir, 'db')

# Create the directories for the project
os.makedirs(data_dir, exist_ok=True)
os.makedirs(scripts_dir, exist_ok=True)
os.makedirs(streamlit_dir, exist_ok=True)
os.makedirs(db_dir, exist_ok=True)

# Create empty files for each subdirectory
data_files = ['input_stream.txt', 'processed_stream.txt']
for file in data_files:
    with open(os.path.join(data_dir, file), 'w') as f:
        pass

scripts_files = ['read_stream.py', 'transform_data.py']
for file in scripts_files:
    with open(os.path.join(scripts_dir, file), 'w') as f:
        pass

streamlit_files = ['app.py', 'config.toml']
for file in streamlit_files:
    with open(os.path.join(streamlit_dir, file), 'w') as f:
        pass

db_files = ['database.sqlite']
for file in db_files:
    with open(os.path.join(db_dir, file), 'w') as f:
        pass

print(f'File structure and empty files created for: {project_dir}')
