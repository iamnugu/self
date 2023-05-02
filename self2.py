while count:
    checkDict['S'] = 0
    checkDict['B'] = 0
    a = str(input())
    for i in range(len(a)):                            #검증
        if a[i] == baseNum[i]:
            checkDict['S'] += 1
        elif a[i] in baseNum:
            checkDict['B'] += 1
    print(f"{checkDict['S']}S, {checkDict['B']}B")
    if checkDict['S'] == 4:
        break
    count -= 1




