from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚕 Welcome to QuickCab</h1>
    <p>Online Cab Booking System</p>
    <p>DevOps CI/CD Project</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
