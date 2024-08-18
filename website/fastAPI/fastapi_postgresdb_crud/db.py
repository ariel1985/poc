# app/db/db_connection.py
import os
import dotenv
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables safely
dotenv.load_dotenv()

Base = declarative_base()

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            USERNAME = os.getenv("POSTGRES_USERNAME")
            PASSWORD = os.getenv("POSTGRES_PASSWORD")
            HOST = os.getenv("POSTGRES_HOST")
            DATABASE = os.getenv("POSTGRES_DATABASE")
            DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
            try:
                cls._instance.engine = create_engine(DATABASE_URL)
                cls._instance.SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=cls._instance.engine)
                print("Database connection established")
            except Exception as e:
                print("Failed to connect to the database")
                raise e
        return cls._instance

    @classmethod
    def get_session(cls):
        return cls()._session()

    def _session(self):
        if self.SessionLocal is None:
            raise Exception("Database session factory is not initialized")
        try:
            db_session = self.SessionLocal
            return db_session
        except Exception as e:
            print("Failed to create a database session")
            raise e
        
    SessionLocal = None

    @classmethod
    def create_tables(cls):
        if cls._instance is None or cls._instance.engine is None:
            print("Database engine is not initialized.")
            return
        Base.metadata.create_all(bind=cls._instance.engine)
        print("Database tables created")

# Usage example
if __name__ == "__main__":
    db_conn = DatabaseConnection()
    db_conn.create_tables()