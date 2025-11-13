import re
from transformers import pipeline

class ContentModerator:
    def __init__(self):
        # Load pre-trained model for toxic content detection
        self.classifier = pipeline(
            "text-classification", 
            model="unitary/multilingual-toxic-xlm-roberta",
            return_all_scores=True
        )
        
        # Custom harmful content patterns
        self.harmful_patterns = [
            r'\b(kill|harm|hurt|violence|attack)\b',
            r'\b(hate|racist|sexist|discriminat)\b',
            r'\b(terrorist|bomb|weapon|shoot)\b'
        ]
    
    def moderate_text(self, text):
        """Analyze text for harmful content"""
        
        # Check for harmful patterns
        pattern_matches = []
        for pattern in self.harmful_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                pattern_matches.append(pattern)
        
        # Use AI model for classification
        try:
            results = self.classifier(text[:512])  # Limit text length
            toxic_score = 0
            for result in results[0]:
                if result['label'] in ['toxic', 'hate', 'insult', 'threat']:
                    toxic_score = max(toxic_score, result['score'])
        except:
            toxic_score = 0
        
        # Determine final classification
        is_unsafe = toxic_score > 0.7 or len(pattern_matches) > 0
        
        return {
            'is_unsafe': is_unsafe,
            'toxic_score': round(toxic_score, 3),
            'pattern_matches': pattern_matches,
            'confidence': max(toxic_score, 0.3)  # Minimum confidence for pattern matches
        }
