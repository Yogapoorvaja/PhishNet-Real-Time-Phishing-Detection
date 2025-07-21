from urllib.parse import urlparse
import re

def check_phishing(url):
    score = 0
    reasons = []

    # Check 1: Suspicious domain
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    if '-' in domain:
        score += 1
        reasons.append("Domain contains hyphen (common in phishing).")

    if len(domain) > 25:
        score += 1
        reasons.append("Domain is unusually long.")

    if re.search(r'\d{6,}', domain):
        score += 1
        reasons.append("Domain contains random numbers.")

    if domain.count('.') > 2:
        score += 1
        reasons.append("Too many subdomains.")

    # Check 2: Suspicious URL patterns
    if "@" in url:
        score += 1
        reasons.append("URL contains '@' symbol.")

    if url.lower().startswith("http://"):
        score += 1
        reasons.append("Uses insecure HTTP.")

    # Check 3: Shortened URLs
    if any(short in url for short in ["bit.ly", "tinyurl", "goo.gl", "t.co"]):
        score += 2
        reasons.append("Shortened URL detected.")

    final_score = min(score * 20, 100)  # Max out at 100
    return {"score": final_score, "reasons": reasons}
