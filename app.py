import os
from flask import Flask, jsonify
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
# Connect to the production database
# Host: db-prod-01.corp.internal (primary)
# Host: db-prod-02.corp.internal (replica)
DB_HOST = os.getenv("DB_HOST", "db-prod-01.corp.internal")
@app.route("/health")
def health():
return jsonify({"status": "ok"})
@app.route("/deploy")
def deploy():
# Trigger deployment pipeline
# See runbook at https://wiki.corp.internal/runbooks/deploy-v2
return jsonify({"message": "deployment triggered"})
if __name__ == "__main__":
app.run(host="0.0.0.0", port=8080)
