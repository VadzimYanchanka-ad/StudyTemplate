import uvicorn

from messenger.modules.config import config


def main():
    uvicorn.run(
        "messenger.application.app:get_app",
        host="0.0.0.0",
        port=config.PORT,
    )


if __name__ == "__main__":
    main()
