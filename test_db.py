from sqlalchemy import create_engine
from app.core.config import settings

try:
    engine = create_engine(settings.DATABASE_URL)

    with engine.connect() as connection:
        print("✅ Database Connected Successfully!")

except Exception as e:
    print("❌ Error:")
    print(e)