def Folder_Filter():
    from Path_Type import Path_Type
    from File_Select import File_Select
    from File_Ex10stion import File_Ex10stion
    import os
    X = "Null"
    print("Enter the path: ")
    while X == "Null":
        Path = File_Select()
        Ex10sion = input("Enter the extension you need: ")
        X = Path_Type(Path)
        if X == "Folder":
            Q = os.listdir(Path)
            Count = 0
            for i in range(0, len(Q)):
                if File_Ex10stion(Q[i]) == Ex10sion:
                    Count += 1
                    print(Count,".", Q[i])
            if Count == 0:
                print("There are no files with the required extension:", Ex10sion)
        else:
            print("Please, Enter a valid path: ")
    print("-----------------------------------------------------------------------")