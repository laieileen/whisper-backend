# Whisper - AI Usage and Prompts

## Overview
The Whisper backend was created with assistance from Claude (Anthropic). Below are the key prompts and decisions.

## Model Used
- **Google Gemini Pro** (ai.google.dev)
- Used for the `/narrative` endpoint to weave memories into narratives
- Free tier: no payment information required

## Key Prompts and Design Decisions

### 1. Backend Architecture
**Prompt**: "Create a Flask backend with two endpoints: one to accept anonymous memory submissions and store them in a database, one to fetch the recent memories and weave them together using Claude API into a cohesive narrative."

**Implementation**:
- Chose SQLite for simplicity (no external database setup needed)
- `/submit` endpoint validates input (1-500 character limit)
- `/narrative` endpoint fetches last 20 memories, calls Claude with a prompt that asks for a poetic weave
- Added error handling and CORS

### 2. Gemini Integration for Narrative Generation
**Prompt**: "Write a Gemini API call that takes a list of anonymous memories and generates a short, beautiful, cohesive narrative that finds common themes."

**Implementation**:
- Uses `gemini-pro` model
- Prompt asks Gemini to be "poetic" and find "universal truths" in disparate voices
- Uses Gemini's `generate_content()` method for streaming responses
- Error handling for API failures

### 3. Environment Variables and Security
**Prompt**: "How should I handle the Gemini API key securely in a Flask app that will be deployed to Render?"

**Implementation**:
- Read API key from environment variables using `os.getenv('GEMINI_API_KEY')`
- `.gitignore` prevents `.env` from being committed
- Render dashboard used to set production environment variables
- No secrets hardcoded in source code

## Testing and Debugging
- Created `/health` endpoint for simple testing
- Included `curl` examples in README for testing each endpoint
- Documented local testing workflow before deployment

## Future Improvements (for Project 2)
- Add user accounts (optional: track what submissions a user made)
- Implement moderation/admin panel to flag/remove inappropriate submissions
- Add daily rotation (new narrative every day based on that day's submissions)
- Persist narratives so you can see past weavings
- Add frontend for better UX/design (this assignment focuses on functionality)