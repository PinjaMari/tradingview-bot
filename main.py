from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

balance = 50
open_position = None
entry_price = 0.0
log = []

@app.route('/webhook', methods=['POST'])
def webhook():
    global balance, open_position, entry_price, log

    data = request.get_json()
    signal = data.get("signal")
    price = float(data.get("price", 0))
    pnl_from_tv = float(data.get("pnl", 0))  # PnL from TradingView (optional)

    if signal == "LONG" and open_position is None:
        entry_price = price
        open_position = "LONG"
        log.append(f"{datetime.now()} - Opened LONG at {entry_price:.4f}")
    elif signal == "SHORT" and open_position is None:
        entry_price = price
        open_position = "SHORT"
        log.append(f"{datetime.now()} - Opened SHORT at {entry_price:.4f}")
    elif signal == "CLOSE" and open_position:
        pnl = price - entry_price if open_position == "LONG" else entry_price - price
        balance += pnl
        log.append(f"{datetime.now()} - Closed {open_position} at {price:.4f}, PnL: {pnl:.4f} (TV: {pnl_from_tv:.4f}), Balance: {balance:.2f}")
        open_position = None

    return jsonify({"status": "ok"})

@app.route('/log', methods=['GET'])
def get_log():
    return jsonify({
        "balance": round(balance, 2),
        "open_position": open_position,
        "entry_price": round(entry_price, 4) if open_position else None,
        "trades": log
    })

@app.route('/')
def home():
    return jsonify({"message": "Trading Webhook Server Running", "balance": balance, "position": open_position})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)