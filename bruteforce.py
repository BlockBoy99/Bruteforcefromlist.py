import zipfile
import itertools
import time

# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        pass

# Main code starts here...

# The file name of the zip file.
zipfilename = 'data2.zip'

zip_file = zipfile.ZipFile(zipfilename)

#word list
wordfilename = 'words.txt'

f1 = open(wordfilename,"r")
r1 = f1.readlines()

MySuccess = False

for password in r1:
    password = password.rstrip()
    
    print ('Trying ' + str(password))
    time.sleep(0.001)
    if extractFile(zip_file, password):
        print ('*' * 20)
        print ('Password found: %s' % password)
        print ('Files extracted...')
        MySuccess = True
        f1.close()
        break

f1.close()

if MySuccess == False:
    # If no password was found by the end, let us know!
    print ('Password not found.')
