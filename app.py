from flask import Flask, request, jsonify, render_template
from digital_footprint import DigitalFootprint  # import your class

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    username = data.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    analyzer = DigitalFootprint(username)
    
    domain_info = analyzer.check_domain(username)
    social_info = analyzer.check_social_media(username)
    
    return jsonify({
        "username": username,
        "domains": domain_info,
        "social_profiles": social_info
    })

if __name__ == '__main__':
    app.run(debug=True)