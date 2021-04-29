import time
import os
import shutil
def main():
    deleted_foldercount=0
    deletedfilescount=0
    path=""
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds>=getfileorfolderage(folderpath):
                removefolder(folderpath)
                deleted_foldercount+=1
                break
            else:
                for folder in folders:
                    folderpath=os.path.join(rootfolder,folder)
                    if seconds>=getfileorfolderage(folderpath):
                       removefolder(folderpath)
                       deletedfoldercount+=1
                for file in files:
                    filepath=os.path.join(rootfolder,file)
                    if seconds>=getfileorfolderage(folderpath):
                        removefile(filepath)
                        deletedfilescount+=1
        else:
            if seconds>=getfileorfolderage(path):
                removefile()
                deletedfilescount+=1
    else:
        print(f"{path}isnotfound")
        deletedfilescount+=1

