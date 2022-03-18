Options_List = ["Open a File", "Copy a File", "Delete a File", "Delete a Folder", "Create a New Folder", "Rename a File", "Move a File", "Show contents of a Folder", "Filtering", "Search a Keyword"]
print("Hello and welcome to PFMAH! \n Here is a list of the things you can do!")
N = "Q"
while N != "K":
    for i in range(0, len(Options_List)):
        X = Options_List[i]
        print(i + 1, X)
    N = int(input("Select a number: "))
    if N == 1:
        from File_Open import File_Open
        File_Open()
    elif N == 2:
        from File_Copy import File_Copy
        File_Copy()
    elif N == 3:
        from File_Delete import File_Delete
        File_Delete()
    elif N == 4:
        from Path_Delete import Path_Delete
        Path_Delete()
    elif N == 5:
        from New_Folder import New_Folder
        New_Folder()
    elif N == 6:
        from File_Rename import File_Rename
        File_Rename()
    elif N == 7:
        from File_Move import File_Move
        File_Move()
    elif N == 8:
        from Show_Content import Show_Content
        Show_Content()
    elif N == 9:
        from Folder_Filter import Folder_Filter
        Folder_Filter()
    elif N == 10:
        from File_Search import File_Search
        File_Search()
    else:
        print ("Wrong Number!")
        N = "Q"