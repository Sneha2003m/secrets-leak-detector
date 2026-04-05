import os

# GOOD: Always load secrets from environment variables
API_KEY = os.environ.get("API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST", "localhost")

def connect_to_database():
    if not DB_PASSWORD:
        raise ValueError("DB_PASSWORD environment variable is not set!")
    print(f"Connecting to database at {DB_HOST}")

if __name__ == "__main__":
    print("App started - secrets loaded from environment variables")
    print(f"API_KEY present: {'Yes' if API_KEY else 'No - set it in .env!'}")
