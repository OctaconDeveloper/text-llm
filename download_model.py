import os
import argparse
from huggingface_hub import hf_hub_download

MODELS = {
    "smol": {
        "name": "SmolLM2-1.7B (Uncensored/Fastest)",
        "repo": "mradermacher/SmolLM2-1.7B-Instruct-abliterated-GGUF",
        "file": "SmolLM2-1.7B-Instruct-abliterated.Q4_K_M.gguf"
    },
    "7b": {
        "name": "Dolphin-2.9.3-7B (Uncensored/Balanced)",
        "repo": "mradermacher/dolphin-2.9.3-mistral-7B-32k-GGUF",
        "file": "dolphin-2.9.3-mistral-7B-32k.Q4_K_M.gguf"
    },
    "nemo": {
        "name": "Dolphin-2.9.3-Nemo-12B (Uncensored/Smart)",
        "repo": "dphn/dolphin-2.9.3-mistral-nemo-12b-gguf",
        "file": "dolphin-2.9.3-mistral-nemo-12b.Q4_K_M.gguf"
    },
    "slimaki": {
        "name": "Slimaki-24B (Uncensored/Largest)",
        "repo": "mradermacher/Slimaki-24B-v1.2-GGUF",
        "file": "Slimaki-24B-v1.2.Q3_K_M.gguf"
    }
}

LOCAL_DIR = "models"

def download(model_alias):
    model = MODELS[model_alias]
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
    parser.add_argument("--alias", help="Model alias to download (smol, 7b, nemo, slimaki)")
    parser.add_argument("--all", action="store_true", help="Download all available models")
    args = parser.parse_args()

    # Filter out models that already exist
    pending_models = {}
    for alias, m in MODELS.items():
        if not os.path.exists(os.path.join(LOCAL_DIR, m["file"])):
            pending_models[alias] = m

    if args.all:
        if not pending_models:
            print("\nAll uncensored models are already downloaded!")
        else:
            for alias in pending_models:
                download(alias)
        return

    if args.alias:
        if args.alias in MODELS:
            download(args.alias)
        else:
            print(f"Invalid alias. Choose from: {', '.join(MODELS.keys())}")
        return

    if not pending_models:
        print("\nAll uncensored models are already downloaded!")
        return

    print("\nAvailable Uncensored Models (Not yet downloaded):")
    for alias, m in pending_models.items():
        print(f"- {alias}: {m['name']}")
    
    choice = input("\nEnter alias to download (or 'all'): ").strip().lower()
    if choice == 'all':
        for alias in pending_models:
            download(alias)
    elif choice in pending_models:
        download(choice)
    else:
        print("Invalid choice or model already exists.")

if __name__ == "__main__":
    main()
