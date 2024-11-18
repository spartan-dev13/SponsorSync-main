# /NoctiWave/run.py

from app import database_creator
from app import app_creator

if __name__ == "__main__":
    database_creator()
    app_creator()
    
from app.database_creator import database_creator
from app.app_creator import app_creator

# Initialize database and create the app
database_creator()
app = app_creator()

# Entry point for Vercel
def handler(environ, start_response):
    return app(environ, start_response)

