def all_words():
    fin = open('words.txt')
    words= set()
    for line in fin:
        word = line.strip()
        words.add(word)
    return words

all_words = all_words()
def children(word):
    # returns all the strings (with meaning or w/o meaning) that can be formed
    # from the string "word"
    # returns list
    l = list(word)
    out = set()
    for letter in list(word):
        l.remove(letter)
        s = ''.join(l)
        if s in all_words:
            out.add(s)
        l = list(word)

    return out

reducibles = set() #memoization
def is_reducible(word):
    if len(word)==1:
        return word == 'a' or word =='i'
    if word in reducibles:
        return True
    x= []
    y= children(word)
    for child in y:
        x.append(is_reducible(child))
    return any(x)



def all_reducibles():

    for word in all_words:
        if is_reducible(word):
            reducibles.add(word)

    return reducibles



def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res
import string

def opener(filename):
    """This open's the file an stips from each word punctuations
    """
    infile = open(filename)
    words = []
    
    for line in infile.readlines(): 
        line.split('-')         
        line_list = line.split(' ')
        word = [word.strip(string.punctuation+string.whitespace).lower() for word in line_list]
        if word != ['']:
            words= word+words   
    
    return words[::-1]

def word_frequency(filename):
    word_list= opener(filename)
    freq = {}
    for word in word_list:
        freq[word]= freq.get(word, 0) +1
    return freq

def most_frequent_words(filename):
    freq = word_frequency(filename)
    
    freq_words = []
    for word in freq:
        freq_words.append((freq[word],word))
    freq_words.sort(reverse=True)
    for word in freq_words[:20]:
        print(word)
    return 

def in_dictionary(word_list):
    for word in word_frequency(word_list).keys():
        if word not in all_words:
             (word)


import random
def choose_from_hist(histogram):
    """Accepts a histogram as dictionary with set and values
    and returns a random key with frequency(hist) in mind
    """
    keys = []
    freqs = []
    for key,value in histogram.items():
        keys.append(key)
        freqs.append(value)
    # total = sum(freqs)
    # freqs =
    #  li/total for i in freqs]
    # print(len(keys), len(freqs))
    # x= ''
    # for i in range(10):
    #     y = random.choices(keys,freqs)[0]
    #     x = x + ' ' +y
    return x

def substract(s1, s2):
    return s1.difference(s2)


# def random_word(filename):
#     hist = word_frequency(filename)
#     words = hist.keys()
#     freq = []
#     for word in words:
#         freq.append(hist[word])
#     for i,num in enumerate(freq):
#         freq[i] = num + freq[i-1]
#     n = freq[-1]  
#     k= random.randint(1,n)
#     def bisect(num_list, p):
#         check1 = num_list[int(len(num_list)/2)]
#         check2 = num_list[int(len(num_list)/2)+1]
#         if p< check1:
#             bisect(num_list[:check1], p)
#         elif p>check2:
#             bisect(num_list[check2:], p)
#         elif check1<p<check2:
#             return num_list.index(check2)
#     return words[bisect(freq, k)]


def Markov(filename, n=2, l=40):
    """Markov analysis results in a summary of a text
    filename is file name of text
    n is order of the markov analysis
    and l is the number of words of the output 
    """
    words= opener(filename)
    mapping = {}
    for i,word in enumerate(words[:-n-1]):
        keys  = tuple(words[i:i+n])
        
        x=  mapping.get(keys, [])
        x.append(words[i+n])
        mapping[keys] = x
    first_words = random.choice(list(mapping.keys()))
    out = list(first_words)
    for i in range(n,l):   
            next_word = random.choice(mapping[tuple(out[-n::])])
            out.append(next_word)
    return ' '.join(out)
        

# def atomic_spectra(n1, n2):
#     Rh = 3.29e15
#     c = 3e8
#     v = Rh*(1/(n1**2) - 1/(n2**2))
#     return f'{round((c/v)*(10**9),1)}nm'