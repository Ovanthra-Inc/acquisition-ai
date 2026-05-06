class WebsiteAdapter:
    def search(self, keyword: str):
        return [
            {
                "company_name": f"{keyword.capitalize()} Corp",
                "website": f"https://{keyword.lower()}.com",
                "industry": "Software",
                "signals": []
            }
        ]
