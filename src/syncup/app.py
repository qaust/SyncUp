"""
Main server for SyncUp web app
"""

from    flask import Flask
import  dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.config.from_prefixed_env()

@app.route('/')
def index():
    return {"message": "Hello!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)