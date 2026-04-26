#!/bin/bash
# Suggy AI Text Model Selection Script

MODELS_DIR="models"

if [ ! -d "$MODELS_DIR" ]; then
    echo "Error: models directory not found."
    exit 1
fi

echo "Available Models:"
models=($(ls $MODELS_DIR/*.gguf | grep -v "active_model.gguf"))

if [ ${#models[@]} -eq 0 ]; then
    echo "No models found in $MODELS_DIR"
    exit 1
fi

for i in "${!models[@]}"; do
    echo "$((i+1)): $(basename "${models[$i]}")"
done

read -p "Enter number to select model: " choice

if [[ "$choice" -gt 0 && "$choice" -le "${#models[@]}" ]]; then
    selected_model="${models[$((choice-1))]}"
    ln -sf "$(basename "$selected_model")" "$MODELS_DIR/active_model.gguf"
    echo "Active model set to: $(basename "$selected_model")"
else
    echo "Invalid choice."
fi
