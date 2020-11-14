import itertools, pymorphy2, random

morph = pymorphy2.MorphAnalyzer()

nouns = []
adjfs = []

with open('rus_shuffled.txt', 'r', encoding='utf8') as f:
    n_lines = 0
    for line in f:
        if n_lines <= 20000:
            n_lines += 1   
            word = line[:-1]
            info = morph.parse(word)[0]
            if info.tag.POS == 'NOUN':
                nouns.append(info.normal_form)
            elif info.tag.POS == 'ADJF':
                adjfs.append(info.normal_form)
            
        
print(nouns[:5], len(nouns))
print(adjfs[:5], len(adjfs))

def phrases():
    print('///running gener///')
    result_pairs = list(itertools.product(adjfs, nouns))
    random.shuffle(result_pairs)
    for x in result_pairs:
        adj, noun = x[0], x[1]
        gender = morph.parse(noun)[0].tag.gender
        adj = morph.parse(adj)[0].inflect({gender}).word
        yield f'{adj} {noun}'
            
def take(n, gener):
    result = []
    try:
        for i in range(n):
            result.append(next(gener))  
    except StopIteration:
        pass
    return '\n'.join(result)

# неумное безумство, нежный работодатель, послеледниковый христианин, сверхсекретное безрассудство 
# экзистенциалистская завалина, отгульная ленивость, противоядерная суббота

print(take(25, phrases()))
