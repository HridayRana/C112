import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/hrida/Downloads"
to_dir = "C:/Users/hrida/OneDrive/Desktop/destination"


list_of_file = os.listdir(from_dir)


for document_name in list_of_file:
    
     name, extension = os.path.splitext(document_name)
   

     if extension == '':
        continue
     if extension in ['.pdf']:

        path4 = from_dir + '/' + document_name                     
        path5 = to_dir + '/' + "Document_Files"                
        path6 = to_dir + '/' + "Document_Files" + '/' + document_name   
       
        if os.path.exists(path5): 
          print("Moving " + document_name + ".....")

          
          shutil.move(path4, path6)

        else:
          os.makedirs(path5)
          print("Moving " + document_name + ".....")
          shutil.move(path4, path6)
