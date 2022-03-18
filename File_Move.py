def File_Move():
    from File_Select import File_Select
    from File_Name import File_Name
    from Path_Type import Path_Type
    import os
    Q = " "
    print("Enter the Path of the file you want to copy: ", end='')
    while Q != "File":
        Path_1 = File_Select()
        Q = Path_Type(Path_1)
        if Q != "File":
            print("Please Enter a path of a file: ")
    Q = " "
    print("Enter the Path of the location at which you want to move your file: ", end='')
    while Q != "Folder":
        Path_2 = File_Select()
        Q = Path_Type(Path_2)
        if Q != "Folder":
            print("Please Enter a valid path of a Folder: ")
    X = File_Name(Path_1)
    with open(Path_1, 'rb') as r_file:
        with open(Path_2 + "\\" + X, 'wb') as w_file:
            for line in r_file:
                w_file.write(line)
    Path = Path_1
    os.remove(Path)
    print("File Moved successfully.")