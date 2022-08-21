from zipfile import ZipFile

# specifying the zip file name
file_name = "zip_file.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
    zip.extract('zip_file.txt')
    # extracting all the files
    print('Extracting all the files now...')
    data = zip.read('zip_file.txt')
    for i in data:
        if(chr(i)==' '):
            print(chr(i),end="")
        else:
            print(chr(i),end="")
