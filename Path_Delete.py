def Path_Delete():
    import shutil
    from File_Select import File_Select
    Path = File_Select()
    Z = "Are you sure you want to delete the Path: " + Path + "?" + "This operation cannot be undone. (Y/N): "
    X = input(Z)
    if X == "Y":
        shutil.rmtree(Path)
        print("Path deleted successfully.")
    else:
        print("Deletion operation has been aborted")