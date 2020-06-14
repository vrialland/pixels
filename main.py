import uvicorn

if __name__ == "__main__":
    # Serve application
    import uvicorn

    uvicorn.run("pixels.app:app", host="0.0.0.0", reload=True)
