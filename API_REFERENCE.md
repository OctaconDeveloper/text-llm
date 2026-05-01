# 📖 Suggy AI API Reference

This document provides a comprehensive technical reference for all Suggy AI Text Model API endpoints.

---

## 🔐 Security & Authentication
All `POST` endpoints require an API key passed via the `m-api-key` header.
- **Header Name**: `m-api-key`
- **Example**: `m-api-key: sk-suggy-f9a1b2c3`

---

## 📡 Endpoints Summary

### 1. Chat Completion
`POST /api/chat`
The primary endpoint for generating text with context and persona support.

**Request Body (`application/json`):**
| Field | Type | Description |
| :--- | :--- | :--- |
| `message` | `string` | **Required**. The user input text. |
| `sessionId` | `string` | Optional. Persistent session ID for conversation history. |
| `profileId` | `string` | Optional. Database-backed profile ID to load traits from. |
| `profileName` | `string` | Optional. Name of a `.txt` profile file in `profiles/`. |
| `modelName` | `string` | Optional. Model alias (e.g., `smol`, `nemo`) to use. |
| `ignoreLimit` | `boolean` | Optional. Set `true` to bypass the 20-message history limit. |
| `temperature` | `float` | Optional. Controls randomness (Default: `0.8`). |
| `max_tokens` | `int` | Optional. Max response length (Default: `512`). |

**Response Body:**
```json
{
  "sessionId": "UUID-string",
  "response": "AI generated text",
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 45,
    "total_tokens": 168
  }
}
```

---

### 2. Create Profile
`POST /api/profiles`
Save a character persona to the database.

**Request Body (`application/json`):**
| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | **Required**. Character name. |
| `style` | `string` | Interaction/speaking style. |
| `ethnicity` | `string` | Character ethnicity. |
| `ageRange` | `string` | Age description (e.g., "20-34"). |
| `sex` | `string` | Gender/Sex. |
| `personality`| `string` | Core personality traits. |
| `background` | `string` | Life history and context. |
| `hairStyle` | `string` | Physical hair description. |
| `hairColor` | `string` | Physical hair color. |
| `eyeColor` | `string` | Physical eye color. |
| `bodyType` | `string` | Physical body description. |
| `breastStyle`| `string` | Physical description. |

**Response Body:**
```json
{
  "status": "success",
  "profileId": "UUID-string",
  "traits": { ... }
}
```

---

### 3. System Health
`GET /api/health`
Check API status and model availability. No API key required.

**Response Body:**
```json
{
  "status": "ready",
  "current_model": "filename.gguf",
  "alias": "smol",
  "available_models": ["model1.gguf", "model2.gguf"],
  "available_profiles": ["mistress_elena", "luna"],
  "n_ctx": 4096
}
```

---

### 4. List Models
`GET /api/models`
Returns a simple list of all models currently present in the `models/` directory.

---

### 5. List Profile Files
`GET /api/profiles`
Returns a list of all `.txt` profile names found in the `profiles/` directory.

---

## 🚦 Rate Limiting
- **Global Limit**: 100 requests per minute.
- **Chat Limit**: 20 requests per minute.
*Exceeding these limits will result in a `429 Too Many Requests` response.*

---

## 🎭 Persona Attribute Mapping
When creating or using profiles, the following mapping is applied to build the system prompt:

- **[IDENTITY]**: `name`, `type`, `ethnicity`, `ageRange`, `sex`
- **[PERSONALITY]**: `style`, `personality`, `background`
- **[PHYSICAL]**: `bodyType`, `breastStyle`, `hairStyle`, `hairColor`, `eyeColor`, `complexion`
