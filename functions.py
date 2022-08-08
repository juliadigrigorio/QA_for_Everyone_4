def approx_equals(a,b):
    diff = abs(a-b)
    return diff <= 0.001


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
