import re

filepath = "agent-service/app/utils/tools.py"
with open(filepath, "r") as f:
    content = f.read()

# Replace the manual headers setup and httpx block
# e.g.:
# headers = get_internal_headers(state)
# async with httpx.AsyncClient() as client:
# with:
# async with get_agent_client(state) as client:

content = content.replace("from app.utils.auth import get_internal_headers", "from app.utils.auth import get_internal_headers, get_agent_client")

pattern = re.compile(r'    headers = get_internal_headers\(state\)\n    async with httpx.AsyncClient\([^)]*\) as client:')
content = pattern.sub('    async with get_agent_client(state) as client:', content)

pattern2 = re.compile(r'    headers = get_internal_headers\(state\)\n    async with httpx.AsyncClient\(\) as client:')
content = pattern2.sub('    async with get_agent_client(state) as client:', content)

# Remove the headers=headers from all post/get requests because get_agent_client already injects them!
# wait, httpx client instances remember headers, but we were passing them per request. 
# It's fine to pass them again, or just remove them.
# Let's remove `, headers=headers` and `, headers=headers`
content = content.replace(", headers=headers", "")

with open(filepath, "w") as f:
    f.write(content)
print("Updated tools.py")
