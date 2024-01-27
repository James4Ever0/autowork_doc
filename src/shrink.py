# all fucked up.
import winreg
# is this for free?
from storeADill import storeXList


def obtain():
    # it always have to end.
    # 获取该键的所有键值
    deadCode = []
    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,
                         r"")
# all fucked up.
    # 获取该键的所有键值，遍历枚举
    try:
        i = 0
        while 1:
            # EnumKey用来枚举子键，EnumValue方法用来枚举键值，
            ret = winreg.EnumKey(key, i)
            # print(ret)
            deadCode.append(ret if type(ret) == str else str(ret))
            # is it str?
            # print(repr(name),value)

            # return value
            i += 1
    except WindowsError:
        # print('error')
        return deadCode
    return deadCode


if __name__ == '__main__':
    o = obtain()
    storeXList(o, "shrink")
    print(o[0], o[-1],len(o))
# works like fuck.
# we only get the interested part.
# what the fuck?
# now we are gonna check items.
# quantum mechanics?