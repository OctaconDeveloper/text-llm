import os
import argparse
from huggingface_hub import hf_hub_download

MODELS = {
    "1": {
        "name": "SmolLM2-1.7B (Uncensored/Fastest)",
        "repo": "mradermacher/SmolLM2-1.7B-Instruct-abliterated-GGUF",
        "file": "SmolLM2-1.7B-Instruct-abliterated.Q4_K_M.gguf"
    },
    "2": {
        "name": "Dolphin-2.9.3-7B (Uncensored/Balanced)",
        "repo": "mradermacher/dolphin-2.9.3-mistral-7B-32k-GGUF",
        "file": "dolphin-2.9.3-mistral-7B-32k.Q4_K_M.gguf"
    },
    "3": {
        "name": "Dolphin-2.9.3-Nemo-12B (Uncensored/Smart)",
        "repo": "dphn/dolphin-2.9.3-mistral-nemo-12b-gguf",
        "file": "dolphin-2.9.3-mistral-nemo-12b.Q4_K_M.gguf"
    },
    "4": {
        "name": "Slimaki-24B (Uncensored/Largest)",
        "repo": "mradermacher/Slimaki-24B-v1.2-GGUF",
        "file": "Slimaki-24B-v1.2.Q3_K_M.gguf"
    }
}

LOCAL_DIR = "models"

def download(model_id):
    model = MODELS[model_id]
    print(f"\n--- Downloading {model['name']} ---")
    os.makedirs(LOCAL_DIR, exist_ok=True)
    try:
        path = hf_hub_download(
            repo_id=model["repo"],
            filename=model["file"],
            local_dir=LOCAL_DIR
        )
        print(f"Done! Model saved to: {path}")
        return path
    except Exception as e:
        print(f"ERROR: Could not download {model['name']}.")
        print(f"Check URL: https://huggingface.co/{model['repo']}")
        print(f"Details: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="Model ID to download (1-4)")
    args = parser.parse_args()

    if args.id:
        if args.id in MODELS:
            download(args.id)
        else:
            print("Invalid ID.")
    else:
        print("\nAvailable Uncensored Models:")
        for key, m in MODELS.items():
            print(f"{key}: {m['name']}")
        
        choice = input("\nEnter ID to download (or 'all'): ").strip().lower()
        if choice == 'all':
            for key in MODELS:
                download(key)
        elif choice in MODELS:
            download(choice)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
