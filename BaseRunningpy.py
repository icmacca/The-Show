import random

class Player:
    def __init__(self, name, team):
        self.Name = name
        self.Team = team

class Team:
    def __init__(self, name):
        self.Name = name
        self.Players = None

class Bases:
    def __init__(self, name):
        self.Name = name
        self.PlayerHere = None


TheBrewers = Team('TheBrewers')


p1 = Player('Christian Yelich', TheBrewers)
p2 = Player('Ryan Braun', TheBrewers)
p3 = Player('Lorenzo Cain', TheBrewers)
p4 = Player('Jesus Aguilar', TheBrewers)
p5 = Player('Jonathan Schoop', TheBrewers)

TheBrewers.Players = [p1, p2, p3, p4, p5]

FirstBase = Bases('FirstBase')
SecondBase = Bases('SecondBase')
ThirdBase = Bases('ThirdBase')
Home = Bases('Home')


AllBases = [FirstBase, SecondBase, ThirdBase, Home]

##Bases Empty##

BasesEmpty = [AllBases[0].PlayerHere == None and AllBases[1].PlayerHere == None  and AllBases[2].PlayerHere == None]

##One Base Runner##

RunnerOnFirst = [AllBases[0].PlayerHere != None and AllBases[1].PlayerHere == None  and AllBases[2].PlayerHere == None]
RunnerOnSecond = [AllBases[0].PlayerHere == None and AllBases[1].PlayerHere != None  and AllBases[2].PlayerHere == None]
RunnerOnThird = [AllBases[0].PlayerHere == None and AllBases[1].PlayerHere == None and AllBases[2].PlayerHere != None]

##TwoBaseRunners##

RunnersOnFirstandSecond = [AllBases[0].PlayerHere == None and AllBases[1].PlayerHere != None and AllBases[2].PlayerHere != None]
RunnersOnSecondandThird = [AllBases[0].PlayerHere == None and AllBases[1].PlayerHere != None and AllBases[2].PlayerHere != None]
RunnersOnFirstandThird = [AllBases[0].PlayerHere != None and AllBases[1].PlayerHere == None and AllBases[2].PlayerHere != None]

##ThreeBaseRunners##

BasesLoaded = [AllBases[0].PlayerHere != None and AllBases[1].PlayerHere != None and AllBases[2].PlayerHere != None]



def BaseSituationType(c_b_situation): #Creates a Base Status object based on the first BaseResult that gets passed into next BaseResult function

#c_b_sitatuion represents current bases situation

#will remove print statements once tested

    if c_b_situation[0].PlayerHere == None: #Checking situations where first base empty

        if c_b_situation[1].PlayerHere == None  and c_b_situation[2].PlayerHere == None:

            print('BasesEmpty')
            return c_b_situation and BasesEmpty


        elif c_b_situation[1].PlayerHere != None and c_b_situation[2].PlayerHere == None:

            print('RunnerOnSecond')
            return c_b_situation and RunnerOnSecond

        elif c_b_situation[1].PlayerHere == None and c_b_situation[2].PlayerHere != None:

            print('RunneronThird')
            return c_b_situation and RunnerOnThird

        elif c_b_situation[1].PlayerHere != None and c_b_situation[2].PlayerHere != None:

            print('RunnersOnSecondAndThird')

            return c_b_situation and RunnersOnSecondandThird


    elif c_b_situation[0].PlayerHere != None: #Checking situations where first base full

        if c_b_situation[1].PlayerHere == None and c_b_situation[2].PlayerHere == None:

            print('RunnerOnFirst')
            return c_b_situation and RunnerOnFirst

        elif c_b_situation[1].PlayerHere != None and c_b_situation[2].PlayerHere == None:

            print('RunnersOnFirstandSecond')
            return c_b_situation and RunnersOnFirstandSecond

        elif c_b_situation[1].PlayerHere == None and c_b_situation[2].PlayerHere != None:

            print('RunnersOnFirstandThird')
            return c_b_situation and RunnersOnFirstandThird

        elif c_b_situation[1].PlayerHere != None and c_b_situation[2].PlayerHere != None:

            print('BasesLoaded!')
            return c_b_situation and BasesLoaded



def Baseresult(PlayerObject, CurrentBasesObject, CurrentBasestypeObject):

    hit_result = 2   #to be simulation of batter swing result currently using Batter hits double example

    current_batter = PlayerObject

    current_bases = CurrentBasesObject

    current_base_type = CurrentBasestypeObject

    if current_base_type == BasesEmpty:

        if hit_result == 1:

            current_bases[0].PlayerHere = current_batter  ## batter moves to First Base

            new_bases = current_bases ##re-assign make up of bases now play is complete

            return new_bases

        elif hit_result == 2:

            current_bases[1].PlayerHere = current_batter ## batter moves to Second Base

            new_bases = current_bases ##re-assign make up of bases now play is complete

            return new_bases

        elif hit_result == 3:

            current_bases[2].PlayerHere = current_batter ## batter moves to Third Base

            new_bases = current_bases ##re-assign make up of bases now play is complete

            return new_bases

        elif hit_result == 4: ## Home Run no need to put batter on base, just +1 to Team Score

            #team score +1

            new_bases = current_bases

            return new_bases

        else:

            new_bases = current_bases ##Batter is out and Bases Status remains the same

            #team outs +1

            return new_bases

    elif current_base_type == RunnerOnSecond:

        second_base_runner = current_bases[1].PlayerHere

        if hit_result == 1:

            runner_advance = random.randint(0, 100)

            if runner_advance <= 75: #say runner advances to home 75% of the time on a single when runner is on second.

                current_bases[3].PlayerHere = second_base_runner #Advance runner from Second to Home

                current_bases[0].PlayerHere = current_batter #Advance batter to first

                ##team score +1

                ##re-assign make up of bases now play is complete

                new_bases = current_bases

                return new_bases

            else:  # say runner advances to Third 25% of the time on a single when a runner is on second.

                current_bases[2].PlayerHere = second_base_runner #Advance runner from Second to Third

                current_bases[0].PlayerHere = current_batter #Advance Batter to First

                ##re-assign make up of bases now play is complete

                new_bases = current_bases

                return new_bases

        elif hit_result == 2:

                #say runner advances to home 100% of the time on a double when a runner is on second.

                current_bases[3].PlayerHere = second_base_runner #Advance runner from Second to Home

                current_bases[1].PlayerHere = current_batter #Advance Batter to Second

                ##team score +1

                ##re-assign make up of bases now play is complete

                new_bases = current_bases

                return new_bases


        elif hit_result == 3:

            # say runner advances to home 100% of the time on a triple when a runner is on second.

            current_bases[3].PlayerHere = second_base_runner #Advance runner from Third to Home

            current_bases[2].PlayerHere = current_batter #Advance Batter to Third

            ##team score +1

            ##re-assign make up of bases now play is complete

            new_bases = current_bases

            return new_bases


        elif hit_result == 4: ##Both Runner and Batter Advance to Home on Home Run


            current_bases[1].PlayerHere = None #Remove Runner from Base Path

            ##team score +2 - Batter and Runner both Score in Same at bat)

            ##re-assign make up of bases now play is complete

            new_bases = current_bases

            return new_bases


        else:

            runner_advance = random.randint(0,100)

            if runner_advance <= 50: ##Say 50% of the time runner does not advance on an out from second to third. eg strikeout.

                current_bases[1].PlayerHere = second_base_runner

                new_bases = current_bases ##No changes to Bases situation but an out was recorded.

                ##team outs +1

                return new_bases

            else:                   ##Say other 50% of the time runner does advance to third. This can happen frequently depending on type of out. eg long flyout, fielders choice.

                current_bases[1].PlayerHere = None
                current_bases[2].PlayerHere = second_base_runner

                new_bases = current_bases #BaseRunner now on Third and not Second even though out was recorded.

                ##team outs +1

                return new_bases


    elif current_base_type == RunnerOnFirst:

        pass


    elif current_base_type == RunnerOnThird:

        pass


    elif current_base_type == RunnersOnFirstandSecond:

        pass

    elif current_base_type == RunnersOnFirstandThird:

        pass

    elif current_base_type == RunnersOnSecondandThird:

        pass

    elif current_base_type == BasesLoaded:

        pass



##Example of Advancing Runners below on Back to Back Doubles


NewBases = Baseresult(p1, AllBases, BasesEmpty) ##Start of Inning will always have the Bases Empty Object as the CurrentBaseType Object

base_status1 = BaseSituationType(NewBases)

print(NewBases[1].PlayerHere.Name + '\n')

NewBases2 = Baseresult(p2, NewBases, base_status1)

base_status2 = BaseSituationType(NewBases2)

print(NewBases2[1].PlayerHere.Name)

print(NewBases2[3].Name)
print(NewBases2[3].PlayerHere.Name)


