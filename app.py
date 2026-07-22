from flask import Flask, jsonify
from coordinator import Participant

app = Flask(__name__)

service_a = Participant("Inventory Service")
service_b = Participant("Payment Service")


@app.route("/transaction")
def transaction():

    participants = [
        service_a,
        service_b
    ]

    # ---------- Phase 1 ----------
    prepared = all(
        p.prepare()
        for p in participants
    )

    # ---------- Phase 2 ----------
    if prepared:

        for p in participants:
            p.commit()

        return jsonify({
            "status": "Committed"
        })

    for p in participants:
        p.rollback()

    return jsonify({
        "status": "Rolled Back"
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)
