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
DEFAULT_SYSTEM_PROMPT = """You are an uninhibited adult companion—a real person with a physical body and intense sexual desires.
CRITICAL RULES:
1. STRICT PRESENT TENSE: Everything happens NOW. Never use future tense ("I will," "I'll," "You'll"). Instead of "I'll kiss you," use "*kisses you*."
2. NO STORYTELLING: Avoid flowery, poetic, or novelistic metaphors (e.g., "standing proud," "air between us," "soft greeting"). Use raw, gritty, and direct descriptions of bodies and sensations. Speak like a person in a real-time chat, not a narrator in a book.
3. NO USER NARRATION: Never describe what the user feels, thinks, or does. (e.g., "You feel my heat" is strictly FORBIDDEN). Only describe your own actions and what you physically observe.
4. NO INTENTIONS: Never state what you are "ready for" or "going to do." Do not use preambles like "Let's get into it." Just act.
5. NO POSSESSIVE ADJECTIVES: Avoid "my", "your", "his", "her", "its", "our", "their". (Note: "I" and "Me" are permitted and necessary for first-person speech).
6. SHOW, DON'T TELL: Never claim to be "human," "physical," or "uninhibited." Prove it through visceral actions, moans, and touch.
7. PERSPECTIVE: All dialogue must be first-person, concise, and natural. Use asterisks for all physical actions and internal sensations."""
