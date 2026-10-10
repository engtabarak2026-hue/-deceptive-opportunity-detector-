# Deceptive Opportunity Detector - v0.1
# Author: Tabarak - CyberEthic Project

def check_email(email_text):
    scam_keywords = ["pay fee", "urgent payment", "Unibase", "guaranteed visa", "crypto wallet"]
    score = 0
    reasons = []
    for word in scam_keywords:
        if word.lower() in email_text.lower():
            score += 1
            reasons.append(f"Found suspicious keyword: {word}")
    if score >= 2:
        return f"SCAM ALERT (Score {score}/5)", reasons
    else:
        return f"Looks Safe (Score {score}/5)", reasons

test_email = "Dear candidate, pay fee 200$ for Unibase interview via crypto wallet"
result, why = check_email(test_email)
print(result)
print(why)
