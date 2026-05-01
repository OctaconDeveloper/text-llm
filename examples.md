# 📖 API Usage Examples (Production Grade)

This guide provides sample `curl` commands for interacting with the Suggy AI Text Model API. For full technical specifications, see the **[API Reference](API_REFERENCE.md)**.

---

## ⚡ Performance & Reliability Note
- **Rate Limiting**: Most endpoints are limited to **100 requests/minute**. The `/chat` endpoint is limited to **20 requests/minute** by default to ensure fair resource allocation.
- **Caching**: Session history and profiles are cached in Redis. Responses for repeat lookups are near-instant.
- **Persistence**: All data is persisted in a high-performance SQLite WAL database.

---

## 📡 API Endpoints

### 1. Chat Completion
**Endpoint**: `POST /api/chat`  
**Header**: `m-api-key: <your_api_key>` (Required for all POST requests)

**Body Parameters**:
- `message` (string, required)
- `sessionId` (string, optional)
- `profileId` (string, optional)
- `modelName` (string, optional)
- `ignoreLimit` (boolean, optional)

---

## 1. Basic Chat
Start a conversation using the default model.

```bash
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -H "m-api-key: sample-key-123" \
     -d '{
           "message": "Hello! How are you today?"
         }'
```

---

## 2. Advanced Persona Customization
You can deeply customize the AI's identity, personality, and appearance in real-time.

```bash
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -H "m-api-key: sample-key-123" \
     -d '{
           "message": "Tell me about yourself.",
           "name": "Luna",
           "ethnicity": "Latina",
           "ageRange": "20-25",
           "personality": "Sarcastic yet loyal",
           "background": "A tech-savvy hacker from Brazil",
           "bodyType": "Slim",
           "hairStyle": "Short bob",
           "hairColor": "Purple",
           "eyeColor": "Hazel"
         }'
```

---

## 3. Persistent Sessions (Redis Cached)
Use a `sessionId` to make the model remember previous parts of the conversation. These are cached in Redis for high-speed retrieval.

```bash
# First message
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -H "m-api-key: sample-key-123" \
     -d '{
           "sessionId": "session_001",
           "message": "My favorite food is sushi."
         }'

# Follow-up (Model will remember your preference)
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -H "m-api-key: sample-key-123" \
     -d '{
           "sessionId": "session_001",
           "message": "What should we have for dinner?"
         }'
```

---

## 4. Profile Management & Creation
Create a persistent model profile with specific traits and a unique ID.

```bash
curl -X POST http://localhost:8001/api/profiles \
     -H "Content-Type: application/json" \
     -H "m-api-key: sample-key-123" \
     -d '{
           "name": "Mistress Elena",
           "style": "Dominant and sophisticated",
           "ethnicity": "Latin",
           "ageRange": "20-34",
           "sex": "Female",
           "type": "human | anime",
           "hairStyle": "Long curly",
           "personality": "Strict but fair, highly intelligent",
           "hairColor": "Black",
           "eyeColor": "Emerald Green",
           "bodyType": "Thick",
           "breastStyle": "large",
           "background": "Born in the slums of argentina, went to a public school, became an adult star earlier in life"
         }'
```
*Returns a `profileId` that can be used in chat requests.*

---

## 5. Combined: Session, Profile, and History Limit
You can pass `sessionId`, `profileId`, and the `ignoreLimit` flag in a single request.

```bash
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -H "m-api-key: sample-key-123" \
     -d '{
           "sessionId": "long_rp_session_01",
           "profileId": "your-profile-id-here",
           "message": "Hello Elena, let us begin our long journey.",
           "ignoreLimit": true
         }'
```

---

## 6. Switching Models
Switch models instantly using aliases. Available: `smol`, `7b`, `nemo`, `slimaki`.

```bash
# Switch to the 7B model (Balanced & Fast)
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -d '{
           "modelName": "7b",
           "message": "Testing the 7B model."
         }'
```

---

## 7. System Management

### Check Health & Performance
Returns system status, active model, and available resources.
```bash
curl http://localhost:8001/api/health
```

### List All Models
```bash
curl http://localhost:8001/api/models
```

### List Available Persona Profiles
```bash
curl http://localhost:8001/api/profiles
```

---

## 8. Production Deployment
To run the API with high-concurrency support:

```bash
gunicorn -c gunicorn_conf.py api.main:app
```
