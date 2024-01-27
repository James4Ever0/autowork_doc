from getFromDill import returnXList
from storeADill import storeXList
r = returnXList("shrink")
r0 = [x for x in r if "Application" in x]
# print(r0)
storeXList(r0,"apps")
# audacity is scriptable.
# but the most important thing, is that your programming language can give everything that you need.
# what will you do then?