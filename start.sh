#!/bin/bash
# Suggy AI Text Model All-in-One Start Script

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running initialization first..."
    bash init.sh
fi

source venv/bin/activate

echo "------------------------------------------------"
echo "🚀 Starting Suggy AI Text Model API"
echo "📡 Location: http://localhost:8001"
echo "📝 Documentation: examples.md"
echo "🔄 Auto-Reload: ACTIVE"
echo "------------------------------------------------"

# Start the modular API
uvicorn api.main:app --host 0.0.0.0 --port 8001 --reload
