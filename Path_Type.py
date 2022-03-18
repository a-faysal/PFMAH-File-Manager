def Path_Type(Path):
    import os
    if os.path.isfile(Path) == True:
        X = "File"
    elif os.path.isdir(Path) == True:
        X = "Folder"
    else:
        X = "Null"
    return (X)