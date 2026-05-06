class LocalAdapter:
    def search(self, keyword: str):
        return [
            {
                "company_name": f"{keyword.capitalize()} Services",
                "industry": "Local Business",
                "signals": [],
                "location": "New York, NY"
            }
        ]
