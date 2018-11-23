from class_factory import *
from base_running import *

DEBUG_MODE = True


def main(debug_mode):
    """
    Summary: 
        Entry point of program. 
        If debug mode then test code is run, otherwise
        main program is run

    Params:
        Takes global debug as bool

    """
    if(debug_mode):
        test = test_main()
    else:
        main = main()

    print("Hello")


if __name__ == '__main__':
    main(DEBUG_MODE)
