class Player():
    def __init__(self, name, team):
        self.Name = name
        self.Team = team


class Team():
    def __init__(self, name):
        self.Name = name
        self.Players = None


class Base():
    def __init__(self, name="", id=0):
        self.Name = name
        self.PlayerHere = None
        self.ID = id

    def IsOccupied(self):
        """
        Returns bool representing if PlayerHere != None
        """
        return self.PlayerHere != None

    def IsFree(self):
        """
        Returns bool representing if PlayerHere == None
        """
        return self.PlayerHere == None


class BasesManager():
    """
    Responsible to managing bases 
    and their statuses
    """

    def __init__(self, bases=[]):
        self.Bases = bases
        self.CurrentBaseStatus = BasesStatus.BasesEmpty

    def get_base_status(self):
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
