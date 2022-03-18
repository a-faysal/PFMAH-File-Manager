def File_Copy():
    A = 'N'
    while A == "N":
        from File_Select import File_Select
        from File_Ex10stion import File_Ex10stion
        from Path_Type import Path_Type
        print("Enter the Path of the file you want to copy: ", end='')
        Q = " "
        while Q != "File":
            Path_1 = File_Select()
            Q = Path_Type(Path_1)
            if Q != "File":
                print("Please Enter a path of a file: ")
        print("Enter the Path of the location at which you want to place your copy file: ", end='')
        Q = " "
        while Q != "Folder":
            Path_2 = File_Select()
            Q = Path_Type(Path_2)
            if Q != "Folder":
                print("Please Enter a valid path of a Folder: ")
        Name = input("Enter the Name of your copy file: ")
        if Path_Type(Path_2+"\\"+ Name + File_Ex10stion(Path_1)) == 'File':
            A = input('The File you want to create already exists do you want to overwrite it? (Y/N): ')
        else:
            A = "Y"
    with open (Path_1, 'rb') as r_file:
        with open (Path_2+"\\"+ Name + File_Ex10stion(Path_1), 'wb') as w_file:
            for line in r_file:
                w_file.write(line)
    print("File copied successfully.")