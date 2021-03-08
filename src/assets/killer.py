import os
def kill():
    if os.name == "nt":
        pid = os.getpid()
        os.system("cls")
        os.system(f"taskkill /im {pid} /f")
    else:
        return("Your Operating System is Not Supported.")