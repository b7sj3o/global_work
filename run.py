import subprocess

def start_backend():
    print("Starting FastAPI backend...")
    subprocess.Popen(["python", "backend/app.py"], shell=True)

def start_frontend():
    print("Starting Flask frontend...")
    subprocess.Popen(["python", "frontend/app.py"], shell=True)

if __name__ == "__main__":
    start_backend()
    start_frontend()
    print("Both backend and frontend are running!")
