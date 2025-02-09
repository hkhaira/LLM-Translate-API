from dotenv import load_dotenv
import os

load_dotenv() # load environment variables from .env file

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

