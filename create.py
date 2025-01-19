import os

def create_structure(base_path):
    directories = [
        "agents",
        "db",
        "streamlit_app",
        "streamlit_app/components",
        "utils"
    ]

    files = {
        "main.py": "",
        "agents/adjust_agent.py": "",
        "agents/detection_agent.py": "",
        "agents/__init__.py": "",
        "db/database.py": "",
        "streamlit_app/app.py": "",
        "streamlit_app/__init__.py": "",
        "streamlit_app/components/charts.py": "",
        "streamlit_app/components/__init__.py": "",
        "utils/market_data.py": ""
    }

    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

    for file, content in files.items():
        file_path = os.path.join(base_path, file)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    base_path = "C:/Users/vaclav/aia3"  # Change this to your desired base path
    create_structure(base_path)