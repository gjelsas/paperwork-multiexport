#Python
#created at https://github.com/gjelsas/paperwork-multiexport
import os
import shutil


# The top argument for walk
topdir = 'path/to/your/paperwork/dir' #maybe get this from the .config/paperwork.conf file one day...
destination = 'path/to/your/export/dir'  
extension = input ("what are you looking for? press 1 for words and 2 for labels:  ")                #specify the ending/the filename could also becom the words file?
if extension == "1":
    exten = 'words'
elif extension == "2":
    exten = 'labels'
else:
    print("Exiting the programm")
    quit()

keyword = input("Please Enter the label you are looking for:  ")      #keyword we will be looking for
i = 0




def isnotthumb(s):                  #define a function which returns false for .thumbs.jpg files
    if s.find("thumb.jpg") != -1:
        return False
    else:
        return True

def isjpg(s):                       #define a function which returns true for .jpg files
    if s.find(".jpg") == -1:
        return False
    else:
        return True






for dirpath, dirnames, files in os.walk(topdir):   
    for name in files:
        if name.lower().endswith(exten):    #close in on the labels
            f = open(os.path.join(dirpath, name),'r')   #open the files readonly 
            for line in f:
                if keyword in line:    #look for match with the keyword
                    paperworkdir=(dirpath)
                    thumblist = [os.path.join(root, name)   #create a list with all .jpg files
                        for root, dirs, files in os.walk(paperworkdir)
                        for name in files
                        if name.endswith((".jpg"))]
                    pdflist = [os.path.join(root, name)     #create a list with all .pdf files
                        for root, dirs, files in os.walk(paperworkdir)
                        for name in files
                        if name.endswith((".pdf"))]
                    jpglist = list(filter(isjpg,filter(isnotthumb,thumblist)))            #use function above to filter averything exept .jpg files and filter thumbs
                    i = i +10
                    for item in jpglist:
                        i = 1 + i
                        I = str(i)
                        print (item + "->" + destination + I + '.jpg')
                        shutil.copy2 (item, destination + I + '.jpg')
                    for item in pdflist:
                        I = str(i+1)
                        print (item + "->" + destination + I + '.pdf')
                        shutil.copy2 (item, destination + I + '.pdf')

quit()                        
