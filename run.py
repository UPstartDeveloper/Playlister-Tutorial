import os
from app import create_app


if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))
