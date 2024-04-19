from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/run_script", methods=["POST"])
def run_script():
  # Call your Python script here (e.g., using subprocess)
  import subprocess
  result = subprocess.run(["python", "run.py"])
  # Handle the script output (optional)
  # You can return a message based on the script's success/failure
  return "Script execution triggered!"

if __name__ == "__main__":
  app.run(debug=True)
