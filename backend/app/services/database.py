from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Database file path (backend folder ke andar banegi)
DB_PATH = os.path.join(os.path.dirname(__file__), "../codeguard.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Scan history ka table
class ScanHistory(Base):
    __tablename__ = "scan_history"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    language = Column(String)
    total_findings = Column(Integer)
    result_json = Column(Text)  # Poora JSON result store karne ke liye
    created_at = Column(String)  # Date/Time

# Table create karein (agar pehle se nahi hai)
def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()