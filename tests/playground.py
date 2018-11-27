import src
from pybaseball import batting_stats_bref


def get_players(team):
    p1 = src.Player("Todd", team)
    p2 = src.Player("Macca", team)
    p3 = src.Player("Dan", team)
    p4 = src.Player("Stu", team)
    return [p1, p2, p3, p4]


def get_team():
    team = src.Team("Sox")
    return team


def get_bases():
    b1 = src.Base("Base One", 1)
    b2 = src.Base("Base Two", 2)
    b3 = src.Base("Base Three", 3)
    b4 = src.Base("Home", 4)
    return [b1, b2, b3, b4]


def get_base_manager():
    bm = src.BasesManager()
    return bm


def test_out_pybaseball():
    data = batting_stats_bref()
    print(data)


def test_base_running_with_enums():
    """
    test function to show use of new func with enums
    """
    t: src.Team = get_team()
    players: src.Player = get_players(t)
    p1 = players[0]
    bm: src.BasesManager = get_base_manager()
    src.base_running.BaseResult_Todd(p1, bm)


def test_main():
    """
    Main test function
    """
    team = get_team()
    players = get_players(team)
    bases_manager = get_base_manager()

    for base in bases_manager.Bases:
        print(base.Name)

    test_out_pybaseball()
