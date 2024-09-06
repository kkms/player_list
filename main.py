""" Main Implementation to Call the Class """

import requests
from marshmallow import EXCLUDE
from model.league import League
from model.player import Player


def get_league_list( url, limit=10 , active="true"):
    """ Get League List with url, limit and active parameter"""

    params={"limit":limit, "active":active}
    response = requests.get(url, params, timeout=2000)
    if response.status_code == 200:
        league_model = League.Schema().load(response.json())
        return league_model

def get_player_details(url):
    """Get the Player Details """
    print(f"Player:{url}")
    response = requests.get(url, timeout=2000)
    if response.status_code == 200:
        player_details = Player.Schema().load(response.json(),unknown=EXCLUDE)
        return player_details

if __name__ == '__main__':
    URI = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes"

    league_data = get_league_list(URI)
    players = []
    for ref_data in league_data.items:
        player_model = get_player_details(ref_data.ref)
        #print(player_model)
        players.append(player_model)

    print(f"Change the player first name :{players[0].first_name}")
    players[0].first_name = "Santhosh"
    print(f"Changed the player first name :{players[0].first_name}")
