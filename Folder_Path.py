def Folder_Path(Path):
    from File_Name import File_Name
    S = ''
    X = File_Name(Path)
    T = len(Path)-len(X)
    for i in range(0, T-1):
        S += Path[i]
    return (S)