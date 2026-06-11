import os
import json
import sys
from dotenv import load_dotenv

load_dotenv()  # reads .env locally; in GitHub Actions, env vars are injected directly

# --- read secrets ---
api_key    = os.getenv("MY_API_KEY")
model_name = os.getenv("MODEL_NAME")

# --- read payload passed from workflow ---
payload_str = os.getenv("EVAL_PAYLOAD", "{}")
payload     = json.loads(payload_str)

dataset_name = payload.get("dataset_name", "default-dataset")
run_name     = payload.get("run_name",     "test-run")

# --- validation ---
if not api_key:
    print("❌ ERROR: MY_API_KEY is not set")
    sys.exit(1)

# --- simulate eval ---
print(f"✅ Secrets loaded")
print(f"   API Key   : {api_key[:4]}****")   # never print full secret
print(f"   Model     : {model_name}")
print(f"\n📦 Payload received")
print(f"   Dataset   : {dataset_name}")
print(f"   Run name  : {run_name}")
print(f"\n🚀 Running eval [{run_name}] on dataset [{dataset_name}] using [{model_name}]...")
print(f"✅ Done.")
