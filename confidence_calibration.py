# Measures confidence stability

def confidence_score(confidences):
    return sum(confidences) / max(len(confidences), 1)
