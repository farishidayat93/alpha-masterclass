from app import create_app
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv(override=True)
    debug = os.getenv('DEBUG') == 'True'
    app = create_app()
    app.run(debug=debug)
