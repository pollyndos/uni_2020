import os.path
from nltk.tokenize import word_tokenize


class FileReader:
    
    def __init__(self, path):
        self.path = path
        
    def read(self):
        try:
            return open(self.path).read()
        except FileNotFoundError:
           return ''

    def write(self, message):
        with open(self.path, 'a') as file:
            file.write(message)
            file.close()
        return self
            
    def __str__(self):
        return f'{self.path}'
    
    def count(self):
        tokens = word_tokenize(self.read())
        self.word_count = len(tokens)
        # setattr(self, 'word_count', len(tokens))
        # setattr(self, 'line_count', len(open(self.path).readlines()))
        try:
            self.line_count = len(open(self.path).readlines())
        except FileNotFoundError:
            self.line_count = 0
            
        return f'Word count: {self.word_count}. Line count: {self.line_count}'
    
    def __add__(self, obj):
        first_basename = os.path.basename(self.path)
        second_basename = os.path.basename(obj.path)
        name_new_file = f'{os.path.splitext(first_basename)[0]}+{os.path.splitext(second_basename)[0]}.txt' 
        new_obj = FileReader(name_new_file)
        new_obj.write(self.read() + obj.read())
        return new_obj


def main():
    reader = FileReader('new.txt')
    reader.write('hello\nworld')
    print(reader.read())  # 'hello\nworld'
    print(reader.count()) # (2, 2) 
    print(reader.word_count)
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
        
