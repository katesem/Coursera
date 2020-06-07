class FileReader:
    
    def __init__(self, path):
        self.path = path
        
    def read(self):
        st = ""
        try:
            with open(self.path, 'r') as f:
                st = f.read()
                return st
        except  FileNotFoundError:
            return st
            
        


    


        
'''
В классе FileReader должен быть реализован метод read,
 возвращающий строку - содержимое файла, путь к которому был указан при создании экземпляра класса. 
 Python модуль должен быть написан таким образом, чтобы импорт класса FileReader из него не вызвал ошибок.
'''