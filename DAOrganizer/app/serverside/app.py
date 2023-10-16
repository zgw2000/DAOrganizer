from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize Web3 and connect to the Ethereum network
# Replace 'your_ethereum_rpc_url' with the actual Ethereum RPC URL
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('your_ethereum_rpc_url'))

# Example Ethereum account for contract interactions
account_address = '0xYourAccountAddress'
private_key = 'YourPrivateKey'

# Load your DAOrganizer contract ABI and address here
# contract_abi = ...
# contract_address = ...

# Initialize the contract instance
# dao_contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Sample data to simulate proposals and fund allocation
proposals = [
    {"id": 1, "title": "Proposal 1", "description": "Description for Proposal 1", "votes": 0},
    {"id": 2, "title": "Proposal 2", "description": "Description for Proposal 2", "votes": 0},
]
total_funds = 10000

@app.route('/proposals', methods=['GET'])
def get_proposals():
    return jsonify(proposals)

@app.route('/proposals/<int:proposal_id>', methods=['GET'])
def get_proposal(proposal_id):
    proposal = next((p for p in proposals if p['id'] == proposal_id), None)
    if proposal is None:
        return jsonify({"error": "Proposal not found"}), 404
    return jsonify(proposal)

@app.route('/proposals', methods=['POST'])
def create_proposal():
    data = request.json
    if 'title' not in data or 'description' not in data:
        return jsonify({"error": "Title and description are required"}), 400
    
    # Create a new proposal and add it to the list (simulated)
    new_proposal = {"id": len(proposals) + 1, "title": data['title'], "description": data['description'], "votes": 0}
    proposals.append(new_proposal)
    return jsonify(new_proposal), 201

@app.route('/proposals/<int:proposal_id>/vote', methods=['POST'])
def vote_for_proposal(proposal_id):
    proposal = next((p for p in proposals if p['id'] == proposal_id), None)
    if proposal is None:
        return jsonify({"error": "Proposal not found"}), 404
    
    # Simulated vote counting
    proposal['votes'] += 1
    return jsonify({"message": "Vote counted successfully"})

@app.route('/fund_allocation', methods=['GET'])
def get_fund_allocation():
    return jsonify({"total_funds": total_funds, "proposals": proposals})

@app.route('/fund_allocation', methods=['POST'])
def allocate_funds():
    data = request.json
    if 'proposal_id' not in data or 'allocation' not in data:
        return jsonify({"error": "Proposal ID and allocation amount are required"}), 400
    
    proposal_id = data['proposal_id']
    allocation = data['allocation']
    
    proposal = next((p for p in proposals if p['id'] == proposal_id), None)
    if proposal is None:
        return jsonify({"error": "Proposal not found"}), 404
    
    if allocation > total_funds:
        return jsonify({"error": "Insufficient funds"}), 400
    
    # Simulated fund allocation
    total_funds -= allocation
    proposal['allocation'] = allocation
    
    return jsonify({"message": "Funds allocated successfully"})

if __name__ == "__main__":
    app.run(debug=True)
