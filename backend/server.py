from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Brute Force Allocation
def brute_force_allocate(demand, capacity):
    allocation = {}
    branches = list(capacity.keys())

    for book, quantity in demand.items():
        remaining = quantity
        allocation[book] = {}

        for branch in branches:
            if remaining == 0:
                break
            can_take = min(remaining, capacity.get(branch, 0))
            if can_take > 0:
                allocation[book][branch] = can_take
                capacity[branch] -= can_take
                remaining -= can_take
    return allocation

# Balanced Allocation
def balanced_allocate(demand, capacity):
    allocation = {}
    sorted_branches = sorted(capacity.items(), key=lambda x: x[1])

    for book, quantity in demand.items():
        allocation[book] = {}
        remaining = quantity
        i = 0

        while remaining > 0 and i < len(sorted_branches):
            branch, space = sorted_branches[i]
            can_take = min(remaining, space)
            if can_take > 0:
                allocation[book][branch] = can_take
                sorted_branches[i] = (branch, space - can_take)
                remaining -= can_take
            i += 1
    return allocation

@app.route("/api/allocate", methods=["POST"])
def allocate():
    data = request.json
    demand = data.get("demand", {})
    capacity = data.get("capacity", {})

    if not demand or not capacity:
        return jsonify({"error": "Missing demand or capacity"}), 400

    brute_plan = brute_force_allocate(demand.copy(), capacity.copy())
    balanced_plan = balanced_allocate(demand.copy(), capacity.copy())

    return jsonify({"bruteForce": brute_plan, "balanced": balanced_plan})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
