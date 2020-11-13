"""
from corus import load_corpora
import tqdm

path = 'annot.opcorpora.xml.byfile.zip'
records = load_corpora(path)

with open('pos_data.txt', 'w', encoding='utf8') as f:
    for rec in tqdm.tqdm(records):
        for par in rec.pars:
            for sent in par.sents:
                for token in sent.tokens:
                    f.write(f'{token.text} {token.forms[0].grams[0]}\n')
print('Done')
"""
import pickle
from sklearn.model_selection import train_test_split

# не так поняла суть метода predict, переделываю

class UnigramMorphAnalyzer:
    
    def __init__(self, path_annot_corpus):
        self.path_annot_corpus = path_annot_corpus
        self.endings_stat = {}

                
    def __getitem__(self, ending):
        return self.endings_stat[ending]
    
    def train(self):
        print('Running train ')
        all_tags = set()
        with open(self.path_annot_corpus, 'r', encoding='utf8') as f:
            for line in f:
                word, pos = line.split()
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
            f.close()
            return len(self.endings_stat)
        
    def predict(self, token):
        print('Running predict')
        if token in self.endings_stat:
            all_counts = sum(self.endings_stat[token].values())
            res_prob = ''
            for key in self.endings_stat[token].keys():
                prob = round(self.endings_stat[token][key] / all_counts, 4)
                a = f'{key} : {prob}\n'
                res_prob += a
            return f'{token} \n{res_prob}'
        
    def save(self, name_pickle):
        print('Running save')
        with open(name_pickle, 'wb') as f:
            pickle.dump(self.endings_stat, f)
    
    def load(self, name_pickle):
        print('Running load')
        with open(name_pickle, 'rb') as f:
            pickle.load(f)
            
           
uni = UnigramMorphAnalyzer('pos_data.txt')
z = uni.train()
print(z)
print(uni)
print(uni.predict('ова'))
print(uni['ий'])
uni.save('model.pickle')
uni.load('model.pickle')


