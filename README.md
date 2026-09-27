# Whisper Backend

This is a Flask backend that collects anonymous messages and stores them in a database.

## Endpoints

### `POST /submit`
Submit an anonymous message.
- **Body**: `{ "text": "your message here" }`
- **Response**: `{ "success": true, "message": "Memory saved" }` (201)
- **Errors**: Returns 400 if text is empty or over 500 characters

### `GET /messages`
Fetch all stored messages.
- **Response**: `{ "messages": [...], "count": N }` (200)
- Each message has `text` and `timestamp`

### `GET /health`
Check if the backend is running.
- **Response**: `{ "status": "ok" }` (200)

## How Frontend Uses It

1. User fills form and clicks "Leave a message"
2. Frontend `POST` to `/submit` with the message text
3. Backend stores it in SQLite database
4. User clicks "Peek inside"
5. Frontend `GET` from `/messages`
6. Backend returns all stored messages
7. Frontend displays them

## Local Setup

### Prerequisites
- Python 3.9+

### Steps
```bash
git clone <repo-url>
cd whisper-backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Server runs on `http://127.0.0.1:5000`

### Test Locally
```bash
# Health check
curl http://127.0.0.1:5000/health

# Submit message
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'

# Get messages
curl http://127.0.0.1:5000/messages
```

## Deployment (Render)

1. Push to GitHub (public repo)
2. Go to Render.com → New Web Service
3. Connect this repo
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Deploy

Your backend URL: `https://whisper-backend-jrie.onrender.com`

## Authentication and Secrets

This backend doesn't use any private APIs.

Database (`memories.db`) is created automatically and stored locally on Render.

## Troubleshooting

**"ModuleNotFoundError"** → Run `pip install -r requirements.txt`

**Backend slow to wake up** → Render free tier sleeps after inactivity. First request takes 10-30 seconds.