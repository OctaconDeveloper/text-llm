# 📖 API Usage Examples

This guide provides sample `curl` commands for interacting with the Suggy AI Text Model API.

---

## 1. Basic Chat
Start a conversation using the default model (Nemo).

```bash
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
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

## 3. Persistent Sessions (Memory)
Use a `session_id` to make the model remember previous parts of the conversation.

```bash
# First message
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -d '{
           "session_id": "session_001",
           "message": "My favorite food is sushi."
         }'

# Follow-up (Model will remember your preference)
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -d '{
           "session_id": "session_001",
           "message": "What should we have for dinner?"
         }'
```

---

## 4. Switching Models & Profiles
You can switch models or persona profiles on the fly.

```bash
# Switch to the 7B model (Balanced & Fast)
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -d '{
           "model_name": "7b",
           "message": "Testing the 7B model."
         }'

# Use a saved profile (e.g., companion)
curl -X POST http://localhost:8001/api/chat \
     -H "Content-Type: application/json" \
     -d '{
           "profile_name": "companion",
           "message": "Let's talk."
         }'
```

---

## 5. System Management

### Check Health & Model Qualities
```bash
curl http://localhost:8001/api/health
```

### List Available Persona Profiles
```bash
curl http://localhost:8001/api/profiles
```

### List All Models
```bash
curl http://localhost:8001/api/models
```
