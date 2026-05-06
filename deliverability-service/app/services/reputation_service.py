class ReputationService:
    def calculate_score(self, domain_metrics: dict) -> float:
        """
        Calculate reputation score based on bounce rate, spam rate, and delivery success.
        Base score is 100.
        """
        score = 100.0
        
        bounce_rate = domain_metrics.get("bounce_rate", 0.0)
        spam_rate = domain_metrics.get("spam_rate", 0.0)
        
        if bounce_rate > 5.0:
            score -= 30.0
        elif bounce_rate > 2.0:
            score -= 10.0
            
        if spam_rate > 2.0:
            score -= 40.0
        elif spam_rate > 0.5:
            score -= 15.0
            
        return max(score, 0.0)

    async def update_domain_reputation(self, db, domain: str, metrics: dict):
        # Implementation to update DB record
        pass
