from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:pass@db:5432/email_sec"
    es_url: str = "http://es:9200"
    rabbitmq_url: str = "amqp://guest:guest@rabbitmq/"
    redis_url: str = "redis://redis:6379/0"
    vt_api_key: str = ""  # Set in .env
    abuseipdb_key: str = ""
    # Add for uniques: ipfs_node_url, etc.

settings = Settings()