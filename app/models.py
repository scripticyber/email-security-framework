from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class EmailAnalysis(Base):
    __tablename__ = "email_analyses"
    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(String, unique=True)
    risk_score = Column(Float)
    risk_level = Column(String)
    headers = Column(JSON)
    iocs = Column(JSON)
    sandbox_results = Column(JSON)
    ai_phishing_prob = Column(Float)  # Unique: AI detection
    forecast_trend = Column(JSON)  # Unique: Predictive
    # Add more for uniques: deepfake_flags, etc.

Base.metadata.create_all(bind=engine)