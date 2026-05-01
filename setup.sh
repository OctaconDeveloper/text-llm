#!/bin/bash

echo "🚀 Starting Suggy AI Production Setup..."

# 1. Environment Setup
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "📥 Installing dependencies..."
./venv/bin/pip install -r requirements.txt

# 2. Database Initialization
echo "🗄️ Initializing database..."
PYTHONPATH=. ./venv/bin/python3 scratch/fix_db.py

# 3. Model Downloads
echo "🤖 Downloading all uncensored models (this may take a while)..."
./venv/bin/python3 download_model.py --all

# 4. Success Message
echo ""
echo "✅ Setup Complete!"
echo "------------------------------------------------"
echo "To start locally:"
echo "  bash start.sh"
echo "------------------------------------------------"
