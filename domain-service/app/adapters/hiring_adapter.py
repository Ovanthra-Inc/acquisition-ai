class HiringAdapter:
    def search(self, keyword: str):
        return [
            {
                "company_name": f"{keyword.capitalize()} Labs",
                "industry": "Tech",
                "signals": ["hiring_engineer"]
            }
        ]
