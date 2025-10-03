from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/frage', methods=['POST'])
def frage_empfangen():
    frage = request.form.get('frage') or request.json.get('frage')
    print("Frage empfangen:", frage)
    return jsonify({"antwort": f"Du hast gefragt: {frage}. Die KI-Antwort kommt später hier rein."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
