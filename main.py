import lichess.api

TEAM = 'polychess-mtl'
TEAM_LENGHT = sum(1 for _ in lichess.api.users_by_team(TEAM))


def get_top_n_members(category, n):
    users = lichess.api.users_by_team(TEAM)
    return sorted([(u.get('perfs', {}).get(category, {}).get('rating'), u['id']) for u in users], key=lambda x: x[0])[-n:]


def get_personnal_ranking(username, category=""):
    if category:
        return TEAM_LENGHT - [tup[1] for tup in get_top_n_members(category, TEAM_LENGHT)].index(username)

    ranks = [["bullet"], ["blitz"], ["rapid"]]
    for i, cat in enumerate(ranks):
        ranks[i].append(get_personnal_ranking(username, cat[0]))
    return ranks


def get_online_members():
    users = lichess.api.users_by_team(TEAM)
    users_status = list(lichess.api.users_status([u['id'] for u in users]))
    return [u['id'] for u in users_status if u.get('online')]


# print(get_top_n_members("rapid", 2))
# print(get_online_members())
# print(get_personnal_ranking("justinlachap"))
# print(get_top_n_members("blitz", 6))
# print(get_top_n_members("rapid", 6))
# print(get_top_n_members("bullet", 6))
