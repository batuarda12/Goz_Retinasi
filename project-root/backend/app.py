from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Next.js'in erişebilmesi için CORS ekledik

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Flask API calisiyor!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
