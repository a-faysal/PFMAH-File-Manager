def File_Rename():
    from File_Select import File_Select
    from File_Ex10stion import File_Ex10stion
    from Folder_Path import Folder_Path
    from Path_Type import Path_Type
    import os
    New_Name = input("Enter the New Name of your file: ")
    Q = " "
    while Q != "File":
        Path_1 = File_Select()
        Q = Path_Type(Path_1)
        if Q != "File":
            print("Please Enter a path of a file: ")
    Path_2 = Folder_Path(Path_1)
    with open(Path_1, 'rb') as r_file:
        with open(Path_2 + "\\" + New_Name + File_Ex10stion(Path_1), 'wb') as w_file:
            for line in r_file:
                w_file.write(line)
    os.remove(Path_1)
    print("File has been deleted successfully.")