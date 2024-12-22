import os
from dotenv import load_dotenv
load_dotenv()

class Config:
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False
	API_URL = os.getenv("API_URL")
	SECRET_KEY = os.getenv("SECRET_KEY")
	ADMIN_ENDPOINT = f"{API_URL}/admin"
	VACANCY_ENDPOINT = f"{API_URL}/vacancy"
	VACANCY_REQUEST_ENDPOINT = f"{API_URL}/vacancy-request"

	BABEL_TRANSLATION_DIRECTORIES = "C:/Users/admin/Desktop/Projects/CLIENTS/czech_job_applications/translations"
	BABEL_DEFAULT_LOCALE = "uk"
	BABEL_SUPPORTED_LOCALES = ["uk", "ru"]

	IMAGES_SAVE = "images"
	VIDEOS_SAVE = "videos"
	UPLOADS_FOLDER_ABSOLUTE = "frontend/app/uploads"
	UPLOADS_FOLDER_RELATIVE = "uploads"

class ProductionConfig(Config):
	...

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True