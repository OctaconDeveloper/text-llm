# 🚀 Suggy AI Text Model API (Production Grade)

A high-performance, production-ready API wrapper for running uncensored LLMs. Optimized for scalability, persistence, and deep character immersion.

---

## ✨ Features
- **Production Architecture**: Built with FastAPI, Uvicorn, and Gunicorn for high-concurrency handling.
- **Persistent Memory**: SQLite (WAL mode) for long-term conversation history and user profiles.
- **Speed & Efficiency**: Redis-backed caching and rate limiting (using `pyrate-limiter` 4.x).
- **Security**: Mandatory `m-api-key` header verification for all POST requests.
- **Dynamic Personas**: Deep trait injection for realistic roleplay (Identity, Personality, Physicality).
- **Containerized**: Full Docker and Docker Compose support for instant deployment.

---

## 🛠️ Quick Start (Automated)

The unified setup script handles dependency installation, database initialization, and model downloads:

```bash
bash setup.sh
```

---

## 🐳 Docker Deployment (Recommended)

Start the entire stack (API + Redis) in detached mode:

```bash
docker-compose up --build -d
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/chat` | Main generation endpoint with session and persona support. |
| `POST` | `/api/profiles` | Create a persistent persona profile. |
| `GET` | `/api/health` | Simple health check for monitoring/load balancers. |
| `GET` | `/api/status` | Detailed system status, loaded models, and settings. |

**Security Note**: All `POST` requests require the `m-api-key` header defined in your `.env`.

---

## 📂 Project Structure

- **`api/`**: Core modular application logic.
- **`models/`**: Storage for `.gguf` weight files.
- **`profiles/`**: Persistent character definitions.
- **`sessions.db`**: SQLite database for conversation history.
- **`setup.sh`**: One-click environment preparation.
- **`docker-compose.yml`**: Full orchestration for API and Redis.

---

## 🔐 Configuration (`.env`)
Manage your environment variables in the `.env` file:
- `API_KEYS`: Comma-separated list of valid security keys.
- `REDIS_URL`: Connection string for the Redis instance.
- `DEFAULT_MODEL`: The alias to load on startup.

---

## 🎭 Documentation
For detailed `curl` examples and persona attribute guides:
👉 **[examples.md](examples.md)**
