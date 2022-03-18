def New_Folder():
    from File_Select import File_Select
    import os
    from Path_Type import Path_Type
    Q = " "
    R = " "
    Name = input("Enter the Name you desire for the Folder: ")
    print("Enter the Path of the location at which you want to create your folder: ", end='')
    while Q != "Folder":
        Path = File_Select()
        Q = Path_Type(Path)
        if Q != "Folder":
            print("Please Enter a valid path of a Folder: ")
    New_Folder_Path = Path + "\\" + Name
    R = Path_Type(New_Folder_Path)
    if R == "Null":
        os.mkdir(New_Folder_Path)
        print ("New folder","'" + Name + "'", "has been created successfully at:", New_Folder_Path)
    else:
        print ("Folder already exists.")