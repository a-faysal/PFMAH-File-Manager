def File_Search():
    import os
    from File_Select import File_Select
    KeyWord = input("Enter, your Keyword: ")
    print ("The location you want to search: ")
    Path = File_Select()
    for root, dirs, files in os.walk(Path):
        if KeyWord in files:
            print("Keyword exists as a file at: ", os.path.join(root, KeyWord))
            C = 1
            break
        elif KeyWord in dirs:
            print("Keyword exists as directory at: ", os.path.join(root, KeyWord))
            C =1
            break
    if C != 1:
        print("Keyword has not been found :(")