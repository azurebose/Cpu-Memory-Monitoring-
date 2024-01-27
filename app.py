from flask import Flask, render_template, jsonify
import psutil
import time

app = Flask(__name__)

def get_system_usage():
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)
    memory_percent = psutil.virtual_memory().percent
    return {"cpu_percentages": cpu_percentages, "memory_percent": memory_percent}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/system_data")
def system_data():
    system_usage = get_system_usage()
    return jsonify(system_usage)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
