from app.db import engine
from app.models import Base,PaymentEvent

def initialize_database():
    print("Creating missing database tables...")

    Base.metadata.create_all(bind=engine)

    print("Database initialization completed.")


if __name__=="__main__":
    initialize_database()

