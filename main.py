import uvicorn
from pixels.app import app

if __name__ == "__main__":
    # Serve application
    import uvicorn

    uvicorn.run(app, host="0.0.0.0")
