import re

class ContentModerator:
    def __init__(self):
        # Custom harmful content patterns - this is the CORE AI logic
        self.harmful_patterns = [
            r'\b(kill|harm|hurt|violence|attack|murder)\b',
            r'\b(hate|racist|sexist|discriminat)\b',
            r'\b(terrorist|bomb|weapon|shoot|gun)\b',
            r'\b(stupid|idiot|dumb|ugly|fat)\b',
            r'\b(die|death|suicide)\b'
        ]
        
        self.high_risk_patterns = [
            r'\b(kill|murder|terrorist|bomb|suicide)\b',
            r'\b(rape|assault|abuse)\b'
        ]
    
    def moderate_text(self, text):
        """Analyze text for harmful content using pattern matching"""
        
        text_lower = text.lower()
        
        # Check for harmful patterns
        pattern_matches = []
        high_risk_matches = []
        
        for pattern in self.harmful_patterns:
            if re.search(pattern, text_lower):
                pattern_matches.append(pattern)
        
        for pattern in self.high_risk_patterns:
            if re.search(pattern, text_lower):
                high_risk_matches.append(pattern)
        
        # Calculate risk score
        base_score = len(pattern_matches) * 0.2
        high_risk_score = len(high_risk_matches) * 0.5
        total_score = min(base_score + high_risk_score, 1.0)
        
        # Determine if unsafe
        is_unsafe = total_score > 0.3 or len(high_risk_matches) > 0
        
        return {
            'is_unsafe': is_unsafe,
            'toxic_score': round(total_score, 3),
            'confidence': max(total_score, 0.1),
            'pattern_matches': pattern_matches,
            'high_risk_matches': high_risk_matches,
            'risk_level': 'HIGH' if len(high_risk_matches) > 0 else 'MEDIUM' if is_unsafe else 'LOW'
        }
