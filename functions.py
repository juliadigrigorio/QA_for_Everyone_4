def approx_equals(a,b):
    diff = abs(a-b)
    return diff <= 0.001

#----------

spisok1 = [5, 2, 6, 8]
spisok2 = [1, 2, 5, 10]

def change(var):
    var = spisok1
    temp = var.pop()
    var.insert(0, temp)
    temp = var.pop(1)
    var.append(temp)

    return var

print(change(spisok1))
print(change(spisok2))

#----------

def print_s(s):
    print(type(s))
    if str(type(s)) == "<class 'str'>":
        print(s[1])
        print('Hooray')
    else:
        print('invalid parameter')
st = 'dfdhbjh'
print_s(st)

#----------

lst = [5, 9, 2, 5, 9, 8]
def more_than_five(lst):
    new_lst = []
    for element in lst:
        if abs(element) > 5:
            new_lst.append(abs(element))
    print(new_lst)
    return new_lst
print(more_than_five([6, 2, 11, 3]))


#----------

arg1 = [4,10,10,9]
def two_highest(arg1):
    new = list(set(arg1))
    new_sorted = sorted(new)
    new_reversed = new_sorted[::-1]
    if len(new_sorted) > 2:
        return  print(new_reversed[0:2])
    else:
        return print(new_reversed)
two_highest(arg1)

#----------

arg1 = [4,10,10,9]
def two_highest(arg1):
        arg1 = list(set(arg1))
        arg1 = sorted(arg1)
        arg1.reverse()
        return print(arg1[0:2])
two_highest(arg1)


