import lichess.api


def get_top_n_members(category, n):
    users = lichess.api.users_by_team('polychess-mtl')
    return sorted([(u.get('perfs', {}).get(category, {}).get('rating'), u['id']) for u in users], key=lambda x: x[0])[-n:]


def get_personnal_ranking(username, category=""):
    users = lichess.api.users_by_team('polychess-mtl')
    team_lenght = sum(1 for _ in users)
    if category:
        return team_lenght - [tup[1] for tup in get_top_n_members(category, team_lenght)].index(username)

    else:
        ranks = [["bullet"], ["blitz"], ["rapid"]]
        for i, cat in enumerate(ranks):
            ranks[i].append(get_personnal_ranking(username, cat[0]))
        return ranks


def get_online_members():
    users = lichess.api.users_by_team('polychess-mtl')
    users_status = list(lichess.api.users_status([u['id'] for u in users]))
    return [u['id'] for u in users_status if u.get('online')]


# print(get_top_n_members("rapid", 2))
print(get_online_members())
# print(get_personnal_ranking("justinlachap"))
# print(get_top_n_members("blitz", 6))
# print(get_top_n_members("rapid", 6))
# print(get_top_n_members("bullet", 6))
