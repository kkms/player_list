""" Main Implementation to Call the Class """

import requests


def get_league_list( url, limit=10 , active="true"):
    """ Get League List with url, limit and active parameter"""

    params={"limit":limit, "active":active}
    response = requests.get(url, params, timeout=2000)
    if response.status_code == 200:
        return response.json()
    return None


def get_player_details(url):
    """Get the Player Details """
    print(f"Get the Player details from the site :{url}")
    response = requests.get(url, timeout=2000)
    if response.status_code == 200:
        return response.json()
    return None


if __name__ == '__main__':
    URI = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes"

    league_data = get_league_list(URI)
    players = [get_player_details(item["$ref"]) for item in league_data['items'] if league_data]
    # Print the first player name and modify it
    print(f"Change the player first name :{ players[0]["firstName"] }")
    players[0]["firstName"] = "Santhosh"
    print(f"Changed the player first name :{ players[0]["firstName"] }")
