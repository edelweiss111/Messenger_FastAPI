from config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
