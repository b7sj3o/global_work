import subprocess

def start_backend():
    print("Starting FastAPI backend...")
    subprocess.Popen(["uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"])

def start_frontend():
    print("Starting Flask frontend...")
    subprocess.Popen(["python", "frontend/app/app.py"], shell=True)

if __name__ == "__main__":
    start_backend()
    start_frontend()
    print("Both backend and frontend are running!")
