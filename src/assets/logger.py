from datetime import datetime
def logit(x):
    f = open("logs/error.log","a")
    f.write("\n--------------------------------------------------------------------------\n"+x+datetime.now().strftime(" | %Y-%m-%d %H:%M:%S")+"\n--------------------------------------------------------------------------")
    f.close()
def loget(x):
    f = open("logs/success.log","a")
    f.write("\n--------------------------------------------------------------------------\n"+x+datetime.now().strftime(" | %Y-%m-%d %H:%M:%S")+"\n--------------------------------------------------------------------------")
    f.close()