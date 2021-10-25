from flask import Flask, jsonify, request
import services.player_services as player_service

app = Flask(__name__)

@app.route('/users')
def _getPlayers():
    players = player_service.get_users()
    return jsonify(players)

@app.route('/users/<int:player_id>')
def _getPlayer(player_id):
    user = player_service.get_user(player_id)
    return jsonify(user)

@app.route('/users', methods=['POST'])
def _postPlayer():
    addPlayer = player_service.post_user()
    return jsonify(addPlayer)

@app.route('/users/<int:player_id>', methods=['PUT'])
def _putPlayer(player_id):
    updatedPlayer = player_service.put_user(player_id)
    return jsonify(updatedPlayer)

@app.route('/users/<int:player_id>', methods=['DELETE'])
def _delPlayer(player_id):
    deletedPlayer = player_service.del_user(player_id)
    return jsonify(deletedPlayer)



if __name__ == '__main__':
    app.run(debug=True)