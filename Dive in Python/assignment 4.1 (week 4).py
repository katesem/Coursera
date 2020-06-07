import os.path
import sys
import tempfile
import secrets #for generationg random and safe tokens

class File():
    def __init__(self, f_name):
            if os.path.exists(f_name):
                self._f_name = f_name
            else:
                 os.mknod(f_name)
                 self._f_name = f_name
                 
            #file.close()
            
    def  read(self): 
        fp = self._f_name
        content = ''
        with open(fp, 'r') as f:
            content+=f.read()
            return content
        
        
    def __str__(self):
        return self._f_name
    
    def write(self, text):
        fp = self._f_name
        length = len(text)
        with open(fp, 'w') as f:
            f.write(text)
        return length
        
        
    def __iter__(self):
        self._curr = 0
        with open(self._f_name, "r") as f:
            self._lines = f.readlines()
        return self
    
    
    def __next__(self):
        try:
            line = self._lines[self._curr]
            self._curr += 1
            return line
        except IndexError:
            raise StopIteration
        
    
    def __exit__(self, *args):
        self.close()
        

    def  __add__(self, other):
        directory = tempfile.gettempdir()
        obj_name = secrets.token_hex(6)
        new_path = os.path.join(directory, obj_name) #C:\Users\katew\AppData\Local\Temp\4e12aa24ca64
        obj = File(new_path) #creating class instance
        obj.write(self.read()+other.read())
        return obj


