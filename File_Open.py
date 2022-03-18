def File_Open():
    import os
    from Path_Type import Path_Type
    from File_Select import File_Select
    print("Enter the path of the file you want to open: ")
    Q = " "
    while Q != "File":
        Path = File_Select()
        Q = Path_Type(Path)
        if Q != "File":
            print("Please Enter a path of a file: ")
    os.startfile(Path)
    print("File opened successfully.")
File_Open()