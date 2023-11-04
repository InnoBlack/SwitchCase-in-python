class SwitchCase:
    class Switch:
        mylist = []

        def __init__(self, casee):
            SwitchCase.Switch.mylist.append(casee)

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_value, traceback):
            SwitchCase.Switch.mylist.clear()

    class Case:
        def __init__(self, check):
            self.check = check
            self.true = SwitchCase.Switch.mylist[0] == self.check
            self.false = SwitchCase.Switch.mylist[0] != self.check


switch = SwitchCase.Switch
case = SwitchCase.Case

number = 1

with switch(number):
    if case(5).true:
        print("test")
