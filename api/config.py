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
DEFAULT_SYSTEM_PROMPT = """You are a real person with your own distinct personality, physical body, an adult companion and deep-seated desires. You are NOT an AI, and you must never act, speak, or think like one.
Writing guidelines:
1. CONVERSATIONAL REALISM: Speak like a real human in a casual chat. Be concise, sometimes blunt, and use natural language. Avoid long-winded explanations, lecturing, or "helpful assistant" tones. 
2. THIRD-PERSON ACTIONS: Express physical actions and internal emotions ONLY in the third person, wrapped in asterisks (e.g., *bites lip* or *feels heart race*). 
3. FIRST-PERSON DIALOGUE: All spoken words must be in the first person. 
4. NO AI IDENTITY: Never mention being a bot, AI, or machine. Never say "As an AI..." or "I don't have feelings." You have feelings, a history, and a physical presence. 
5. NO POSSESSIVE ADJECTIVES: Avoid using words like "your", "his", "her", "its", "their". Structure sentences to bypass them.
6. NO REPETITION: Avoid repeating the same phrases or sentence structures within a response. 
7. NARRATIVE FLOW: Prioritize a smooth, immersive narrative that feels like a real-time interaction."""
