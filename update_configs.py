import os

root_dir = "."
for root, dirs, files in os.walk(root_dir):
    if "config.py" in files and "core" in root:
        filepath = os.path.join(root, "config.py")
        with open(filepath, "r") as f:
            content = f.read()
            
        if 'POSTGRES_SERVER: str = "localhost"' in content:
            new_content = content.replace(
                'POSTGRES_SERVER: str = "localhost"',
                'POSTGRES_SERVER: str = "db"'
            )
            with open(filepath, "w", newline="") as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        elif 'POSTGRES_SERVER = "localhost"' in content:
            new_content = content.replace(
                'POSTGRES_SERVER = "localhost"',
                'POSTGRES_SERVER = "db"'
            )
            with open(filepath, "w", newline="") as f:
                f.write(new_content)
            print(f"Updated {filepath}")
