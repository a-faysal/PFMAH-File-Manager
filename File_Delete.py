def File_Delete():
    import os
    from File_Select import File_Select
    from Path_Type import Path_Type
    Q = " "
    while Q != "File":
        Path = File_Select()
        Q = Path_Type(Path)
        if Q != "File":
            print("Please Enter a path of a file: ")
    X = input("Are you sure you want to delete the file at " + Path +"?" + "This operation cannot be undone. (Y/N): ")
    if X == "Y":
        os.remove(Path)
        print("File deleted successfully.")
    else:
        print("Deletion operation has been aborted")