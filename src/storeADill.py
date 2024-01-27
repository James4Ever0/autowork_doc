import dill as pickle
def storeAList(a):
    pickle.dump(a, open("newFuckingDill.dill","wb"))
def storeXList(a,b):
    pickle.dump(a, open(b+".dill","wb"))
