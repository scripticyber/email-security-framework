from fastapi import FastAPI
from app.routers import ingestion, analysis, enrichment, scoring, orchestration, dashboard
from app.config import settings  # Stub
from app.tasks import make_celery  # For Celery integration

app = FastAPI(title="Email Security Framework")

app.include_router(ingestion.router, prefix="/ingest")
app.include_router(analysis.router, prefix="/analysis")
app.include_router(enrichment.router, prefix="/enrich")
app.include_router(scoring.router, prefix="/scoring")
app.include_router(orchestration.router, prefix="/orchestrate")
app.include_router(dashboard.router, prefix="/dashboard")

celery = make_celery(app)  # Init Celery

@app.get("/")
def root():
    return {"status": "Building v0.1 - Core ready, uniques integrating..."}