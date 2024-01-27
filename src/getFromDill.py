import dill as pickle
def returnAList():
    return pickle.load(open("newFuckingDill.dill","rb"))
def returnXList(b):
    return pickle.load(open(b+".dill","rb"))
