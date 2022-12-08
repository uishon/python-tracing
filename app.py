from flask import Flask
import logging
import requests

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    logger.info("serving /")
    return 'Hello World from Python'

@app.route('/nodejs')
def hello():
    logger.info("serving /nedejs")
    response = requests.get("http://localhost:8080")
    logger.info(f"{response.text=}")
    return response.text

logging.basicConfig(level=logging.INFO)
logger.info("app started")
app.run(host='0.0.0.0', port=8000)
