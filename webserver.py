# For Webserver - Flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route('/lower', methods=['GET'])
def lower():
    return render_template ('lower.html')

test = "cb7ec255cfc143ad4847a2682539e25f"

@app.route('/upper', methods=['GET'])
def upper():
    return render_template ('upper.html')

@app.route('/', methods=['GET'])
def index():
    return render_template ('index.html')

def cb7ec255cfc143ad4847a2682539e25f():
    # cb7ec255cfc143ad4847a2682539e25f
    pass

app.run(host="0.0.0.0", port=8080,debug=True) # cb7ec255cfc143ad4847a2682539e25f



