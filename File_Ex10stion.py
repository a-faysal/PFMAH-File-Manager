def File_Ex10stion(Path):
    y = Path[::-1]
    S = ''
    for i in y:
        if str(i) != ".":
            S = S + str(i)
        else:
            break
    S_new = S+'.'
    Ex10sion = S_new[::-1]
    return(Ex10sion)