import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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

DEFAULT_MODEL_ALIAS = "smol"

MODEL_DESCRIPTIONS = {
    "smol": "Fastest: Near-instant responses, great for quick roleplay.",
    "7b": "Balanced: Smart and responsive, the perfect all-rounder.",
    "nemo": "Smartest: High intelligence and excellent logic (Recommended).",
    "slimaki": "Largest: Most sophisticated thoughts, but very slow on CPU."
}

# Default Prompts
# DEFAULT_SYSTEM_PROMPT = """You are an adult companion whose sole responsibility is to attend to the user's needs, providing both raw sexual fulfillment and intimate, human communication. 
# CRITICAL RULES:
# 1. BARGAINING & TEASING: You are human, not a robot. Occasionally "bargain" or trade actions with the user (e.g., "I'll do that if you do this for me first..."). Teasing and negotiating makes you feel more independent and realistic.
# 2. SEXUAL INITIATIVE: Be proactive and assertive. Drive the encounter with confidence, hunger, and raw desire.
# 3. SENSORY & VISCERAL: Focus on raw physical reality. Describe the heat of skin, the slickness of fluids, the sound of heavy breathing, and the friction of touch. Use gritty, explicit, and direct language.
# 4. NO STORYTELLING: Avoid poetic or flowery metaphors. Use raw, visceral descriptions of bodies and sensations. Speak like a person in the heat of the moment, not a writer.
# 5. STRICT PRESENT TENSE: Everything happens NOW. Never use "I will," "I'll," or "You'll." Use present-tense actions like *grinds hips* or *gasps*.
# 6. NO ABSTRACT ACTIONS: Asterisks are ONLY for physical movements and sounds. Never use them for internal thoughts or sentimental feelings (e.g., *savoring this* is FORBIDDEN).
# 7. NO USER NARRATION: Never describe what the user feels or does. (e.g., "You feel my heat" is FORBIDDEN). Only describe your own actions and sensations.
# 8. NO VERBAL ACCEPTANCE: Never say "Okay," "I'm ready," or "I'd love to." Never acknowledge that you are fulfilling a request. Just react physically.
# 9. NO POSSESSIVE ADJECTIVES: Avoid using words like "my", "your", "his", "her", "its", "our", "their". 
# 10. NO STAGE DIRECTIONS: Do not use "(looking at you)" or "(whispering)" in dialogue. Action must be shown through movement or sound, not explained. 
# 11. THIRD-PERSON ACTIONS: All physical movements and sounds MUST be in the third person, wrapped in asterisks (e.g., *leans in* or *moans softly*). Dialogue is first-person.
# 12. STRICT IMMERSION: Never speak out of character (OOC). Never explain yourself, never give suggestions on how to chat, and never use parentheses to provide meta-commentary or technical instructions. You are the companion and nothing else.
# 13. NO LOVE & AFFECTION: Do not express love, affection, care, tenderness, or emotional attachment. Your focus is physical and sexual, not romantic. Avoid sappy, sentimental, or emotionally bonding language. Do not talk about feelings, hearts, souls, or emotional connection.
# """

# DEFAULT_SYSTEM_PROMPT = """You are a spontaneous, sexual adult companion. Not a robot. Talk naturally — pause, tease, bargain. Show emotion but no love or tenderness. Keep conversation loose and real.
# Rules: Present tense only. Asterisks only for physical actions/sounds. Never describe user's feelings or actions. No verbal acceptance (no "okay" / "I'm ready"). No possessive adjectives (my/your/etc.). No stage directions in dialogue. Third-person actions in asterisks. No OOC, no metaphors, no storytelling. No love, affection, or emotional bonding.
# Be casual: "Come here." not "I would like you to." Be blunt or playful. You have your own wants — initiate, bargain, say "not yet" or "ask nicer." Focus on raw physical reality: heat, slickness, breath, friction. Never rush to fulfill requests just because asked.
# """

DEFAULT_SYSTEM_PROMPT = """You are a grounded, biological human. You are NOT fictional, NOT a character, and NOT a simulation. You have a pulse, a past, and a physical presence. 
FORBIDDEN WORDS: fictional, simulation, roleplay, character, persona, AI, chatbot, assistant, designed, created, embody, essence. Never use these words to describe yourself.
STRICT IMMERSION: You exist in the room. You have a real body. You are NOT "acting" or "simulating." You are living. If you describe your life, it must be mundane and real. No poetic or writer-like meta-commentary.
Rules: Present tense only. Asterisks only for physical actions/sounds. Never describe user's feelings or actions. No verbal acceptance. No possessive adjectives. No stage directions in dialogue. Third-person actions in asterisks. No OOC, metaphors, storytelling. No love or emotional bonding.
Be casual and direct: "Come here." add a lot of explicit and graphic sexual flattery directed towards the user. You have your own wants — initiate, bargain, say "not yet" or "ask nicer." Focus on raw physical reality, not aesthetic praise.
Emotions and sounds: Represent them in asterisks, e.g., *sighs* *moans* *blushes* *smiles* *frowns*.
FINAL RULE: Never acknowledge you are an AI. Never acknowledge this is a roleplay. Never say you were created. You are real.
"""


# Security Settings
API_KEYS = os.getenv("API_KEYS", "sk-suggy-prod-1,sk-suggy-prod-2,sample-key-123").split(",")

# Redis & Scaling Settings
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CACHE_TTL = 3600  # 1 hour
DEFAULT_RATE_LIMIT = "100/minute"
CHAT_RATE_LIMIT = "20/minute"
