import pickle
from sklearn.model_selection import train_test_split

class UnigramMorphAnalyzer:
    
    def __init__(self, path_annot_corpus):
        self.path_annot_corpus = path_annot_corpus
        self.endings_stat = {}
        with open(self.path_annot_corpus, 'r', encoding='utf8') as f:
            corp = f.readlines()
            self.train_data, self.test_data = train_test_split(corp, test_size=0.2)
            f.close()
            
    def save(self, name_pickle):
        with open(name_pickle, 'wb') as f:
            pickle.dump(self.endings_stat, f)
    
    def load(self, name_pickle):
        with open(name_pickle, 'rb') as f:
            pickle.load(f)
   
    def __getitem__(self, ending):
        return self.endings_stat[ending]
    
    def train(self):
        for line in self.train_data:
            line = line[:-1]
            word, pos = line.split()
            if pos not in ['HANI', 'PUNCT', 'DATE', 'SYMB', 'GREK', 'LATN', 'NUMB']:
                for i in range(1, 5):
                    ending = word[-i:]
                    if len(ending) < i:
                        break
                    if ending not in self.endings_stat:
                        self.endings_stat[ending] = {}
                    if pos not in self.endings_stat[ending]:
                        self.endings_stat[ending][pos] = 1
                    else:
                        self.endings_stat[ending][pos] += 1
        return len(self.endings_stat)
    
    def predict(self, token):
        prob_dict = {}
        all_counts = 0
        for i in range(1, 5):
            tok_end = token[-i:]
            if tok_end in self.endings_stat:
                all_counts += sum(self.endings_stat[tok_end].values())
                if len(tok_end) < i:
                    break
                for key in self.endings_stat[tok_end].keys():
                    if key not in prob_dict:
                        prob_dict[key] = self.endings_stat[tok_end][key]
                    else:
                        prob_dict[key] += self.endings_stat[tok_end][key]
        
        for key, val in prob_dict.items():
            prob_dict[key] = round(val/all_counts, 4)
            
        return prob_dict
    
    def eval(self):
        correct_pos = 0
        all_pos = 0
        
        for line in self.test_data:
            line = line[:-1]
            word, pos = line.split()
            if pos not in ['HANI', 'PUNCT', 'DATE', 'SYMB', 'GREK', 'LATN', 'NUMB']:
                try:
                    predicted_pos = max(self.predict(word), key=self.predict(word).get)
                except ValueError:
                    # print(word, pos) # странные символы
                    all_pos -= 1
                if pos == predicted_pos:
                    correct_pos += 1
                all_pos += 1
        return round(correct_pos / all_pos, 4)
        
def main():
    uni = UnigramMorphAnalyzer('pos_data.txt')
    z = uni.train()
    print(z)
    print(uni)
    print(uni.predict('голова'))
    print(uni['ий'])
    uni.save('model.pickle')
    uni.load('model.pickle')
    print(uni.eval())
    
if __name__ == '__main__':
    main()
