class OptimizationService:
    def optimize_campaign(self, metrics: dict):
        """
        Analyze metrics and generate optimization recommendations.
        """
        recommendations = []
        
        reply_rate = metrics.get("reply_rate", 0.0)
        open_rate = metrics.get("open_rate", 0.0)
        
        if reply_rate < 0.05:
            recommendations.append("The reply rate is low. Try more personalized email body content.")
            
        if open_rate < 0.20:
            recommendations.append("Open rate is below benchmark. Experiment with shorter, high-curiosity subject lines.")
            
        return {
            "status": "success",
            "recommendations": recommendations,
            "confidence_score": 0.85
        }
