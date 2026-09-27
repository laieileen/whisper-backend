# Whisper Backend

A Flask backend that collects anonymous submissions and uses Claude AI to weave them into cohesive, poetic narratives.

## What It Does

This backend provides two endpoints:

### `POST /submit`
Accepts anonymous memory submissions.
- **Parameters**: JSON body with `text` field (string, 1-500 characters)
- **Response**: `{ "success": true, "message": "Memory saved" }`
- **Error handling**: Returns 400 if text is missing, empty, or too long

**Example request**:
```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I learned to be brave today"}'
```

### `GET /narrative`
Fetches the most recent memories and uses Claude to weave them into a narrative.
- **Parameters**: None
- **Response**: JSON with `narrative` (string) and `memory_count` (integer)

**Example request**:
```bash
curl http://127.0.0.1:5000/narrative
```

### `GET /health`
Simple health check to verify the backend is running.
- **Response**: `{ "status": "ok" }`

## How the Frontend Communicates

1. User types a memory into a form on the frontend
2. Frontend makes a `POST /submit` request with the text
3. User clicks "See the Narrative" button
4. Frontend makes a `GET /narrative` request
5. Backend queries the last 20 memories from the database
6. Backend calls Claude API to weave them together
7. Frontend displays the narrative to the user

## Setup and Running Locally

### Prerequisites
- Python 3.9+
- A Claude API key from Anthropic

### 1. Clone the repo and set up a virtual environment
```bash
git clone <your-repo-url>
cd whisper-backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the root directory (do NOT commit this):
```
CLAUDE_API_KEY=sk-ant-...your-actual-key-here...
```

Load it in your shell:
```bash
export $(cat .env | xargs)
```

Or use a tool like `python-dotenv` to load it automatically.

### 4. Run the backend
```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
```

The database (`memories.db`) will be created automatically on first run.

### 5. Test it locally
In a separate terminal:
```bash
curl http://127.0.0.1:5000/health
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "This is my memory"}'
curl http://127.0.0.1:5000/narrative
```

## Handling Secrets

### Locally
- Store your Claude API key in a `.env` file
- **Do NOT commit `.env` to git**
- The `.gitignore` file prevents this automatically

### On Render
1. Go to your Render deployment dashboard
2. Click "Environment"
3. Add a new environment variable: `CLAUDE_API_KEY` with your API key
4. Render will inject it into the app when it runs

The app reads `CLAUDE_API_KEY` using `os.getenv('CLAUDE_API_KEY')`.

## Frontend-Backend Connection

The frontend is hosted on GitHub Pages at a URL like `https://username.github.io/whisper`.

The backend is hosted on Render at a URL like `https://whisper-backend.onrender.com`.

CORS is enabled on this backend (via `flask-cors`) so the frontend can make cross-origin requests.

The frontend replaces `http://127.0.0.1:5000` with the Render URL before deploying.

## Deployment to Render

1. Push this repo to GitHub (public repo)
2. Go to [Render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Set the following:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - Add environment variables (including `CLAUDE_API_KEY`)
6. Click "Create Web Service"
7. Render will deploy and give you a public URL

## Troubleshooting

**"ModuleNotFoundError: No module named 'flask'"**
- Make sure you've activated the venv and run `pip install -r requirements.txt`

**"CLAUDE_API_KEY not found"**
- Locally: Make sure `.env` is in the root and you've run `export $(cat .env | xargs)`
- On Render: Check the Environment tab in the dashboard

**Frontend can't reach the backend**
- Make sure you've replaced `http://127.0.0.1:5000` with the Render URL in your frontend
- Check the browser console for CORS errors (shouldn't happen with this setup)
- Test the backend directly: `curl https://your-backend-url.onrender.com/health`

**Database errors**
- `memories.db` is created automatically; you don't need to set it up
- If something goes wrong, delete it and run the app again

## Code Explanation

- **`init_db()`**: Creates the memories table on startup
- **`get_recent_memories()`**: Fetches the last N memories from the database
- **`weave_narrative()`**: Calls Claude API to turn memories into a cohesive narrative
- **`/submit` endpoint**: Validates input, stores memory in DB, returns success/error
- **`/narrative` endpoint**: Pulls memories, calls Claude, returns the narrative
- **CORS**: Allows the frontend (GitHub Pages) to make requests to this backend