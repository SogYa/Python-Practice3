def same_by(characteristic, objects):
    for i in range(0, len(objects) - 1):
        if characteristic(objects[i]) != characteristic(objects[i + 1]):
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x * 1, values):
    print('same')
else:
    print('different')