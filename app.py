from flask import Flask, request

app = Flask(_name_)

@app.route('/', methods=['POST'])
def handle_webhook():
    data = request.json
    print("Received webhook:", data)
    # Process your webhook here (e.g., simulate trades)
    return 'OK', 200

if _name_ == '_main_':
    app.run(port=5000)