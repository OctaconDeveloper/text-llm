#!/bin/bash
set -e

echo "=== Suggy AI Text Model Initializer ==="

# 1. Environment Setup
if [ ! -d "venv" ]; then
    echo "[1/4] Creating virtual environment..."
    python3 -m venv venv
else
    echo "[1/4] Virtual environment already exists."
fi

source venv/bin/activate

echo "[2/4] Installing/Updating dependencies..."
# pip install --upgrade pip
pip install -r requirements.txt
pip install "llama-cpp-python[server]" huggingface-hub fastapi uvicorn

# 2. Model Management
echo "[3/4] Model Management..."
# download_model.py is in root
python3 download_model.py

# select_model.sh is in scripts/
if [ -f "scripts/select_model.sh" ]; then
    bash scripts/select_model.sh
fi

