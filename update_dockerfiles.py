import os

root_dir = "."
for root, dirs, files in os.walk(root_dir):
    if "Dockerfile" in files:
        filepath = os.path.join(root, "Dockerfile")
        with open(filepath, "r") as f:
            content = f.read()
            
        if "docker-entrypoint.sh" not in content and "uvicorn" in content:
            new_content = content.replace(
                'CMD ["uvicorn"', 
                'COPY docker-entrypoint.sh /usr/local/bin/\nRUN chmod +x /usr/local/bin/docker-entrypoint.sh\nCMD ["/usr/local/bin/docker-entrypoint.sh"]\n# CMD ["uvicorn"'
            )
            with open(filepath, "w", newline="") as f:
                f.write(new_content)
            print(f"Updated {filepath}")
