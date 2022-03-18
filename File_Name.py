def File_Name(Path):
    y = Path[::-1]
    S = ''
    for i in y:
        if str(i) != "\\":
            S = S + str(i)
        else:
            break
    S_new = S
    FileName = S_new[::-1]
    return(FileName)