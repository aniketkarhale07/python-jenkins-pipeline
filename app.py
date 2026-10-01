from flask import Flask

app = Flask(__name__)

# Disable Flask request logs
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def home():
    return "<h1>PHP</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# nohup python3 app.py >/dev/null 2>&1 &
