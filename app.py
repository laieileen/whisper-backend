# Whisper Backend
# Collects anonymous submissions

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Initialize SQLite database
DATABASE = 'memories.db'

def init_db():
    """Create the memories table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def get_recent_memories(limit=20):
    """Fetch the most recent memories from the database."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT text FROM memories ORDER BY timestamp DESC LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]

def get_all_messages(limit=50):
    """Fetch all messages from the database."""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT text, timestamp FROM memories ORDER BY timestamp DESC LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.close()
    return [{"text": row[0], "timestamp": row[1]} for row in rows]

@app.route('/submit', methods=['POST'])
def submit_memory():
    """Accept an anonymous memory submission."""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text = data['text'].strip()
        
        if len(text) < 1:
            return jsonify({'error': 'Memory cannot be empty'}), 400
        
        if len(text) > 500:
            return jsonify({'error': 'Memory too long (max 500 characters)'}), 400
        
        # Store in database
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('INSERT INTO memories (text) VALUES (?)', (text,))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Memory saved'}), 201
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/messages', methods=['GET'])
def get_messages():
    """Fetch all submitted messages."""
    try:
        messages = get_all_messages(limit=50)
        
        if not messages:
            return jsonify({'messages': [], 'count': 0}), 200
        
        return jsonify({
            'messages': messages,
            'count': len(messages)
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)