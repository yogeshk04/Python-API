"""
runserver.py
---

Run this script to start the globoticket app.
"""
import uvicorn

def main():
    uvicorn.run(
        "globoticket.api:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
