@@ -0,0 +1,13 @@
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():Add commentMore actions
    data = request.json
    print("Received webhook:", data)
    # Process your webhook here (e.g., simulate trades)
    return 'OK', 200

if _name_ == '_main_':
    app.run(port=5000)