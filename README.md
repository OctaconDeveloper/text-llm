# 🚀 Suggy AI Text Model

A modular, high-performance setup for running uncensored LLMs on your Mac. Features persistent SQLite sessions, advanced persona customization, and an auto-reloading modular API.

---

## ⚡ Quick Start

The easiest way to start is using the unified start script:

```bash
bash start.sh
```
*This will automatically set up the environment (if needed) and launch the API server on port 8001.*

---

## 🎭 Advanced Persona Customization

Suggy AI allows you to build deep, realistic characters by passing specific attributes in your API requests. The model will automatically embody the traits you define.

**Available Attributes:**
- **Identity**: `name`, `ethnicity`, `ageRange`
- **Personality**: `personality`, `background`, `style`
- **Physical Traits**: `bodyType`, `breastStyle`, `hairStyle`, `hairColor`, `eyeColor`

---

## 📂 Project Structure

- **`api/`**: Core modular application logic (FastAPI).
- **`profiles/`**: Text files defining different persona profiles.
- **`models/`**: Folder where `.gguf` model files are stored.
- **`sessions.db`**: SQLite database for persistent conversation memory.
- **`start.sh`**: The one-click startup script.
- **`download_model.py`**: Script to download new model variants.

---

## 🔓 Uncensored Model Lineup

| Alias | Model Name | Description |
| :--- | :--- | :--- |
| `smol` | SmolLM2-1.7B-Abliterated | **Fastest**: Near-instant on CPU. |
| `7b` | Dolphin-2.9.3-Mistral-7B | **Balanced**: Great logic and speed. |
| `nemo` | Dolphin-2.9.3-Nemo-12B | **Smartest (Default)**: Best for complex chats. |
| `slimaki` | Slimaki-24B-v1.2 | **Largest**: Most complex thoughts (Slow). |

---

## 📡 API Usage

The API runs on port **8001**. For detailed `curl` samples, including persistent sessions and the new persona attributes, see:

👉 **[examples.md](examples.md)**

---


## ⚠️ Performance Note (16GB RAM)
To ensure stability on 16GB systems, the context window is set to **4096 tokens**. For the best experience on Intel Macs, the `nemo` or `7b` models are recommended.
