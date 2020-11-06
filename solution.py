import os.path
from nltk.tokenize import word_tokenize


class FileReader:
    
    def __init__(self, path):
        self.path = path
        
    def read(self):
        try:
            if not os.path.exists(self.path):
                raise FileNotFoundError
        except FileNotFoundError:
            content = ''
        else:
            file = open(self.path, 'r') 
            content = file.read()
            file.close()
        return content 

    def write(self, message):
        with open(self.path, 'a') as file:
            file.write(message)
            file.close()
        return self
            
    def __str__(self):
        return f'{self.path}'
    
    def count(self):
        tokens = word_tokenize(self.read())
        setattr(self, 'word_count', len(tokens))
        lines = len(open(self.path).readlines())
        setattr(self, 'line_count', lines)
        return self.word_count, self.line_count
    
    def __add__(self, obj):
        first_basename = os.path.basename(obj.path)
        second_basename = os.path.basename(self.path)
        name_new_file = f'{os.path.splitext(first_basename)[0]}+{os.path.splitext(second_basename)[0]}.txt' 
        new_obj = FileReader(name_new_file)
        result_of_add = self.read() + obj.read()
        new_obj.write(result_of_add)
        return new_obj


def main():
    reader = FileReader('new.txt')
    reader.write('hello\nworld')
    print(reader.read())  # 'hello\nworld'
    print(reader.count())  # (2, 2) 
    new_reader = FileReader('very_new.txt')
    new_reader.write('\nthe most beutiful world')
    print(type(new_reader))  # <class '__main__.FileReader'>
    print(new_reader.count()) # (4, 2)
    all_together = reader + new_reader
    print(type(all_together)) # <class '__main__.FileReader'>
    print(all_together.count())  # (6, 3)
    print(all_together)  #  very_new+new.txt
     

if __name__ == '__main__':
    main()
        
