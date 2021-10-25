import repositories.player_repository as repository
from domain.models import Player, Parameter
from flask import Flask, request

player = repository.PlayerRepository
parameter = repository.ParameterRepository

def get_users():
    return player.users

def get_user(player_id):
    playerFound = [player for player in player.users if player["id"] == player_id]
    if (len(playerFound) > 0):
        return playerFound
    return "Player not found"

def post_user():
    newUser = {
        "id" : len(player.users) + 1,
        "name": request.json["name"],
        "score" : request.json["score"]
    }
    player.users.append(newUser)
    return player.users

def put_user(player_id):
    found = [player for player in player.users if player["id"] == player_id]
    newParameter = {
        "attribute" : found[0]["name"],
        "value" : found[0]["score"]
    }
    parameter.parameters.append(newParameter)
    if (len(found) > 0):
        found[0]["name"] = request.json["name"]
        found[0]["score"] = request.json["score"]
        return [{"parameter before": newParameter}, {"Current Parameter": found}]
    return "Player not found"

def del_user(player_id):
    delFound = [player for player in player.users if player["id"] == player_id]
    if (len(delFound) > 0):
       player.users.remove(delFound[0])
    return "deleted product succesfully"