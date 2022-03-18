def File_Select():
    from Path_Type import Path_Type
    import os
    Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W" ,"X", "Y", "Z"]
    Partitions = []
    Content = []
    Q = "Y"
    T  = "W"
    while T == "W":
        U = input("Do you want to \n 1. Enter the Path Manually \n 2. Use file browser? \n" )
        if U == "1":
            Path = input("Please, Enter your Path: ")
            while Path_Type(Path) == "Null":
                Path = input("invalid path, please, try again: ")
            T = "E"
            return (Path)
        elif U == "2":
            for i in Letters:
                Path = i+":\\"
                if Path_Type(Path) == "Folder":
                    Partitions.append(i)
            print("Choose from the following partitions:", Partitions, end =' ')
            Chosen_Partition = input()
            Path = Chosen_Partition + ":\\"
            while Q == "Y":
                R = os.listdir(Path)
                for i in range(0, len(R)):
                    print(i + 1, ".", R[i])
                    Content.append(R[i])
                Num = int(input("Select a number: "))
                Path = Path + "\\" + Content[Num-1]
                Content = []
                if Path_Type(Path) == "File":
                    Q == "N"
                    break
                else:
                    Q = input("Do you want to proceed? (Y/N): ")
            T = "E"
            return (Path)
        else:
            print("Please Enter a valid number!")
            T = "W"