from os import getenv
from dotenv import load_dotenv
load_dotenv()


ADMIN_USERNAME = getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = getenv("ADMIN_PASSWORD")