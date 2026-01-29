import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

print(os.getenv("OPENAI_API_KEY"))
