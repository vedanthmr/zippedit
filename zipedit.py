import zipfile, os
from pathlib import Path
choice=int(input("Enter \n1 if you wish to compress a file or folder \n2 if you wish to decompress a zip\n"))
if(choice==1):
    def backuptozip(folder):
        folder=os.path.abspath(folder)
        num=1
        while True:
            zipfilename=os.path.basename(folder)+"_"+str(num)+'.zip'
            if not os.path.exists(zipfilename):
                break
            num+=1
        print(f'Creating {zipfilename}...')
        backupzip=zipfile.ZipFile(zipfilename, 'w')
        print('Done')
        for foldername, subfolders, filenames in os.walk(folder):
            print(f"Adding files in {foldername}")
            backupzip.write(foldername)
            for filename in filenames:
                newBase=os.path.basename(folder)+'_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backupzip.write(os.path.join(foldername,filename))
        backupzip.close()
        print("Done")
    x=input("Enter the file/folder path to be compressed into zipfile in STRING format: ")
    backuptozip(x)

elif(choice==2):
    def decompress(folder): 
        examplezip=zipfile.ZipFile(y)
        examplezip.extractall()
        examplezip.close()
    y=input("Enter the zipfile/folder path to be decompressed in STRING format: ")
    decompress(y)