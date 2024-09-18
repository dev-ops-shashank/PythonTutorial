from module import myFunc
# import module
'''
if I run main.py, the Output will be :
Hello User!
module              # means, file module.py is running with help of import

but if I run module.py, the Output will be:
Hello User!
__main__            # since file module.py is not importing anything, it returns __main__
                    # which is by default name of a file
                    # every python code runs from main
'''