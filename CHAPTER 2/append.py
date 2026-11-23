class FileHandler:
    def append_file(self):
        try:
            File=open("simple.txt","a")
            File.write("\n second year mca")
            
            File=open("simple.txt","r")  
          
            data=File.read()
            print(data)
            
        except FileNotFoundError:
            print("error: file not found")
            
        except PermissionError:
            print("per:permission derived")
            
        except Exception as e:
            print(e)
            
        finally:
            # File.close()
            print("program executed")
        
        
obj=FileHandler()

obj.append_file()

        