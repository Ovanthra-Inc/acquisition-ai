import os

services = [
    'experimentation-service', 'learning-service', 'rbac-service', 
    'organization-service', 'platform-api-service', 'policy-service', 
    'recommendation-service', 'observability-service', 'billing-service', 
    'proxy-service'
]

content = '''from fastapi import APIRouter

api_router = APIRouter()
'''

for svc in services:
    directory = os.path.join(svc, 'app', 'api', 'v1')
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, 'router.py')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Created {file_path}")
