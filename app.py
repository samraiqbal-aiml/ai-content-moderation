
from flask import Flask, render_template, request, jsonify
from content_moderator import ContentModerator

app = Flask(__name__)
moderator = ContentModerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/moderate', methods=['POST'])
def moderate():
    text = request.json.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'Please enter some text'})
    
    # Analyze the text
    result = moderator.moderate_text(text)
    
    return jsonify({
        'text': text,
        'is_unsafe': result['is_unsafe'],
        'confidence': result['confidence'],
        'toxic_score': result['toxic_score'],
        'pattern_matches': result['pattern_matches']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
