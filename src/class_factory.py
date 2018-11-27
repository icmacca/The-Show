# import used for static typing
from typing import List, Dict


class Team():
    def __init__(self, name: str):
        self.Name: str = name
        self.Players: List[Player] = None
        self.Score = 0
        self.Outs = 0


class Player():
    def __init__(self, name: str, team: Team):
        self.Name: str = name
        self.Team: Team = team


class Base():
    def __init__(self, name: str, id: int):
        self.Name: str = name
        self.PlayerHere: Player = None
        self.ID: int = id

    def IsOccupied(self) -> bool:
        """
        Returns bool representing if PlayerHere != None
        """
        return self.PlayerHere != None

    def IsFree(self) -> bool:
        """
        Returns bool representing if PlayerHere == None
        """
        return self.PlayerHere == None


class BasesStatus():
    """
     Enum to represent the status of a the Bases member 
    of a BaseManager object
    """
    BasesEmpty = 0
    # single occupation
    FirstOnly = 1
    SecondOnly = 2
    ThirdOnly = 3
    # double occupation
    FirstAndSecond = 12
    SecondAndThird = 23
    FirstAndThird = 13
    # all
    Loaded = 123


class SwingPower():
    """
    Enum to represent the result of a successful hit
    """
    NoBases = 0
    OneBase = 1
    TwoBase = 2
    ThreeBase = 3
    HomeRun = 4


class BasesManager():
    """
    Responsible for creating 
    and managing bases 
    and their statuses
    """

    def __init__(self):
        self.Bases: List[Base] = self.generate_bases()
        self.CurrentBaseStatus: BasesStatus = BasesStatus.BasesEmpty

    def generate_bases(self) -> List[Base]:
        b1: Base = Base("Base One", 1)
        b2: Base = Base("Base Two", 2)
        b3: Base = Base("Base Three", 3)
        b4: Base = Base("Home", 4)
        return [b1, b2, b3, b4]

    def get_base_status(self) -> BasesStatus:
        """
        Returns a BasesStatus enum representing the
        current status of all bases
        """
        if(self.Bases[0].IsFree() and
                self.Bases[1].IsFree() and
                self.Bases[2].IsFree()):

            return BasesStatus.BasesEmpty

        elif(self.Bases[0].IsOccupied() and
                self.Bases[1].IsFree() and
                self.Bases[2].IsFree()):

            return BasesStatus.FirstOnly

        elif(self.Bases[0].IsFree() and
                self.Bases[1].IsOccupied() and
                self.Bases[2].IsFree()):

            return BasesStatus.SecondOnly

        elif(self.Bases[0].IsFree() and
                self.Bases[1].IsFree() and
                self.Bases[2].IsOccupied()):

            return BasesStatus.ThirdOnly

        elif(self.Bases[0].IsOccupied() and
                self.Bases[1].IsOccupied() and
                self.Bases[2].IsFree()):

            return BasesStatus.FirstAndSecond

        elif(self.Bases[0].IsFree() and
                self.Bases[1].IsOccupied() and
                self.Bases[2].IsOccupied()):

            return BasesStatus.SecondAndThird

        elif(self.Bases[0].IsOccupied() and
                self.Bases[1].IsFree() and
                self.Bases[2].IsOccupied()):

            return BasesStatus.FirstAndThird

        else:

            return BasesStatus.Loaded
