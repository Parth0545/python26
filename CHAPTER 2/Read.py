class FileHandler:
    def read_file(self):
        try:
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

obj.read_file()

        