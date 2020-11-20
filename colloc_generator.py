import itertools, pymorphy2, random

morph = pymorphy2.MorphAnalyzer()

nouns = []
adjfs = []

with open('rus_shuffled.txt', 'r', encoding='utf8') as f:
    n_lines = 0
    for line in f:
        if n_lines <= 18000:
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
    pairs = list(itertools.product(random.sample(adjfs, 500), random.sample(nouns, 500)))
    random.shuffle(pairs)
    for pair in pairs:
        adj, noun = pair[0], pair[1]
        gender = morph.parse(noun)[0].tag.gender
        # print(adj, gender, noun)
        adj = morph.parse(adj)[0].inflect({gender}).word
        yield f'{adj} {noun}'
            
def take(n, gener):
    result = []
    try:
        for i in range(n):
            result.append(next(gener))
    # AttributeError молотовой neut, мецский femn --> не склоняет именно по этому роду
    # ValueError астроцит, бедняжка --> в тэге нет рода
    except (StopIteration):
        pass
    print(len(result))
    return '\n'.join(result)

# неумное безумство, нежный работодатель, послеледниковый христианин, сверхсекретное безрассудство 
# экзистенциалистская завалина, противоядерная суббота, отважная ресничка, недурственный дуралей

print(take(18, phrases()))
