from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Projekt-ID aus deinem Schlüssel extrahiert
PROJECT_ID = "proj_9ugnmB5wuj_MhKZJpDlEOG1_Am9_UjCuhTQB7qHmo4wHkTbXPYMDwZ63A-GNK6zb"

@app.route('/api/frage', methods=['POST'])
def frage_empfangen():
    frage = request.form.get('frage') or request.json.get('frage')
    print("Frage empfangen:", frage)
    antwort = frage_an_gpt(frage)
    return jsonify({"antwort": antwort})

def frage_an_gpt(frage):
    url = f"https://api.openai.com/v1/projects/{PROJECT_ID}/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": frage}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return data["choices"][0]["message"]["content"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
