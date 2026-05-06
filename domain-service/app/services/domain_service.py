from app.adapters.website_adapter import WebsiteAdapter
from app.adapters.hiring_adapter import HiringAdapter
from app.adapters.local_adapter import LocalAdapter

class DomainService:
    def __init__(self):
        self.adapters = {
            "website": WebsiteAdapter(),
            "hiring": HiringAdapter(),
            "local": LocalAdapter()
        }

    def search(self, domain: str, keyword: str):
        adapter = self.adapters.get(domain)
        if not adapter:
            raise ValueError(f"Domain adapter '{domain}' not supported")
        return adapter.search(keyword)
