from colorama import Fore, Back, Style

def foo():
    print(Fore.RED + bar() + Style.RESET_ALL)

def bar():
    return f"{__name__} is greeting you!"
