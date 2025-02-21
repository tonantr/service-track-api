import os
from app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":

    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5001))
    debug = os.getenv("FLASK_DEBUG", "False") == "True"

    if debug:
        print(f"Running in debug mode on http://{host}:{port}")
        app.run(host=host, port=port, debug=True)
    else:
        print(f"Starting production server at http://{host}:{port}")
        serve(app, host=host, port=port)
