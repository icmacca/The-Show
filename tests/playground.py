from src.class_factory import *


def get_players(team):
    p1 = Player("Todd", team)
    p2 = Player("Macca", team)
    p3 = Player("Dan", team)
    p4 = Player("Stu", team)
    return [p1, p2, p3, p4]


def get_team():
    team = Team("Sox")
    return team


def get_bases():
    b1 = Base("Base One", 1)
    b2 = Base("Base Two", 2)
    b3 = Base("Base Three", 3)
    b4 = Base("Home", 4)
    return [b1, b2, b3, b4]


def get_base_manager(bases):
    bm = BasesManager(bases)
    return bm


def test_main():
    """
    Main test function
    """
    team = get_team()
    players = get_players(team)
    bases = get_bases()
    bases_manager = get_base_manager(bases)

    for base in bases_manager.Bases:
        print(base.Name)
