from celery import Celery
from app.config import settings

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=settings.redis_url,
        broker=settings.rabbitmq_url
    )
    return celery

@celery.task
def analyze_email(email_data):
    # Stub: Call utils for parsing, auth, ioc, etc.
    from app.utils.email_parser import parse_email
    from app.utils.auth_checks import validate_auth
    from app.utils.ioc_extractor import extract_iocs
    from app.utils.ml_features import extract_features, detect_ai_phishing  # Unique
    # ... integrate all steps
    parsed = parse_email(email_data)
    auth_results = validate_auth(parsed)
    iocs = extract_iocs(parsed)
    features = extract_features(iocs, auth_results)
    ai_prob = detect_ai_phishing(parsed['body'])  # Unique
    # Enrich, sandbox, score, etc.
    return {"risk": 50.0, "ai_prob": ai_prob}  # Placeholder

# Add tasks for uniques: e.g., @celery.task def share_to_ipfs(iocs): ...