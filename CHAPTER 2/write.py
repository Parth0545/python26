class FileHandler:
    def write_file(self):
        try:
            File=open("simple.txt","w")
            File.write("MCA First Year")
            
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

obj.write_file()

        