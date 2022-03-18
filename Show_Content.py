def Show_Content():
    from Path_Type import Path_Type
    from File_Select import File_Select
    from File_Ex10stion import File_Ex10stion
    import os
    X = "Null"
    print("Enter the path: ")
    while X == "Null":
        Path = File_Select()
        X = Path_Type(Path)
        if X == "File":
            if File_Ex10stion(Path) != ".txt":
                L = 'Bi'
            else:
                L = 'txt'
            if L != "Bi":
                with open (Path, 'r') as f:
                    Size_To_Read = 100
                    f_Content = f.read(Size_To_Read)
                    while len(f_Content) > 0:
                        print (f_Content, end ='')
                        f_Content = f.read(Size_To_Read)
            else:
                os.startfile(Path)
                print("Non '.txt' file has been opened.")
        elif X == "Folder":
            Q = os.listdir(Path)
            for i in range(0, len(Q)):
                print(i + 1, Q[i])
        elif X == "Null":
            print("Please, Enter a valid path: ")
    print("\n----------------------------------------------------------------------------------")