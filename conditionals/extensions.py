def file():
    
        extension = input('File name: ')
        extension_list = extension.split('.')
        filename_end = extension_list[-1] 
        filename_beginning = extension_list[0] 

        if filename_end == 'gif' or filename_end == 'jpg' or \
           filename_end == 'jpeg' or filename_end == 'png':
            
            if filename_end == 'jpg':
                return 'image/' + 'jpeg'
            
            return 'image/' + filename_end
        elif filename_end == 'pdf':
                return 'applcation/' + 'pd'
            
        elif filename_end == 'txt':
                return 'text/' + filename_beginning
        
        elif filename_end == 'zip':
                return 'application/' + filename_end
        
        
        
        
        else:
            return 'application/octet-stream'
            
            

  
file()