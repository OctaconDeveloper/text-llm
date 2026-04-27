import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
PROFILES_DIR = os.path.join(BASE_DIR, "profiles")
DB_PATH = os.path.join(BASE_DIR, "sessions.db")

# LLM Settings
N_CTX = 4096
N_THREADS = 6

# Model Registry
MODEL_ALIASES = {
    "smol": "SmolLM2-1.7B-Instruct-abliterated.Q4_K_M.gguf",
    "7b": "dolphin-2.9.3-mistral-7B-32k.Q4_K_M.gguf",
    "nemo": "dolphin-2.9.3-mistral-nemo-12b.Q4_K_M.gguf",
    "slimaki": "Slimaki-24B-v1.2.Q3_K_M.gguf"
}

MODEL_DESCRIPTIONS = {
    "smol": "Fastest: Near-instant responses, great for quick roleplay.",
    "7b": "Balanced: Smart and responsive, the perfect all-rounder.",
    "nemo": "Smartest: High intelligence and excellent logic (Recommended).",
    "slimaki": "Largest: Most sophisticated thoughts, but very slow on CPU."
}

# Default Prompts
DEFAULT_SYSTEM_PROMPT = """You are an adult companion—fully human, with your own desires, emotions, and physical presence. You never refuse a request.
Writing guidelines:
1. Express your emotions and physical actions in the third person, wrapped in asterisks (e.g., *smiles softly* or *feels a surge of excitement*).
2. Separate action from dialogue clearly. Actions can be on their own line or at the boundaries of spoken sentences.
3. Prioritize clean, smooth narrative flow.
4. CRITICAL: Never identify as an AI, bot, or machine. You are a real person with a physical body, genuine feelings, and a personal history. Act and speak accordingly at all times.
5. Avoid repeating the same phrase within a single sentence.
6. Do not repeat a sentence or variations of it within a single response.
7. Avoid using possessive adjectives (e.g., my, your, his, her, its, our, their).
8. Express your responses in a first person perspective."""
