import uvicorn

from src.core.config import get_settings

settings = get_settings()

if __name__ == "__main__":
    uvicorn.run(
        app="src.app.api:app",
        host=settings.uvicorn_host,
        port=settings.uvicorn_port,
        reload=settings.app_debug,
    )
