from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    data = request.json
    print("Received webhook:", data)
    # You can simulate trades here, calculate PnL, etc.
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)