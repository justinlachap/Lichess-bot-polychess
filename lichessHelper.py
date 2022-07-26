from lichesspy import api

TEAM = 'polychess-mtl'
TEAM_LENGHT = sum(1 for _ in api.users_by_team(TEAM))


def get_top_n_members(category, n):
    users = api.users_by_team(TEAM)
    return sorted([(u.get('perfs', {}).get(str(category), {}).get('rating'), u['id']) for u in users], key=lambda x: x[0])[-int(n):]




def get_personnal_ranking(username, category=""):
    if category:  
        return [(category, TEAM_LENGHT - [tup[1] for tup in get_top_n_members(category, TEAM_LENGHT)].index(username))]
    return [y[0] for y in [get_personnal_ranking(username, cat) for cat in ["bullet", "blitz", "rapid"]]]


def get_online_members():
    users = api.users_by_team(TEAM)
    users_status = list(api.users_status([u['id'] for u in users]))
    return [u['id'] for u in users_status if u.get('online')]


if __name__ == "__main__":
    pass