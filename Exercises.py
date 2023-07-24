# # import math


# # def Akermann(m,n):
# #     if m==0:
# #         return n+1
# #     elif m>0 and n==0:
# #         return Akermann(m-1, 1)
# #     elif m>0 and n>0:
# #         return Akermann(m-1, Akermann(m, n-1))
# def is_palindrome(str):
#     if str ==str[::-1]:
#         return True
#     else:
#         return False
    
# # def is_divisible(x,y):
# #     return x%y == 0
# # def is_power(x,y):
# #     if x==y:
# #         return True
# #     elif is_divisible(x,y):
# #         return is_power(x/y, y)
# #     return False

# # def print_n(s, n):
# #     while n>0:
# #         print(s)
# #         n = n-1

# # def square_root(a, epsilon=0.0001):
# #     x = a/2
    
# #     while True:
# #         y= (x + a/x)/2
# #         if x==y:
# #             break
# #         x=y

# #     return x

# from math import *

# # for i in range(1,9):
# #     his = sqrt(i)
# #     my = square_root(i)
# #     print(i, my, his, abs(my-his))
    
# # Exercise 7.4
# # def eval_loop():
# #     while True:
# #         inpt= input('Enter an expression')
# #         if inpt == 'Done':
# #            break
# #         else:
# #             a = eval(inpt) 
# #             print(a)
# #     return a

# # def estimate_pi():
# #     sum = k =0 
# #     while True:
        
# #         adendem = (factorial(4*k)*(1103 + 26390*k)/((factorial(k)**4)*396**(4*k)))
# #         print(adendem)
# #         sum+=adendem
# #         esmt = 1/(sum*2*sqrt(2)/9801)
# #         if (adendem < 1e-15):
# #             break

# #         k +=1

# #     return esmt
    
# # def find(word, letter ,start_i):
# #     index = start_i
# #     while index < len(word):
# #         if word[index] == letter:
# #             return index
# #         index = index + 1
# #     return -1

# # import random
# # def memo():
# #     dic = {
# #         'zepto-': -21,
# #         'atto-': -18,
# #         'femto-': -15,
# #         'pico-': -12,
# #         'nano-': -9,
# #         'micro-': -6,
# #         'milli-': -3,
        
# #         'centi-': -2,
# #         'deci-': -1,
# #         'deca-': 1,
# #         'kilo-': 3,
# #         'mega-': 6,
# #         'giga-': 9,
# #         'tera-': 12,
# #         'peta-': 15

# #     }
# #     reverse ={dic[i]: i for i in dic}
    
# #     weights = {i:1 for i in dic}
# #     rev_weights = {i:1 for i in reverse}
# #     correct = 0
# #     wrong = 0
# #     def all_weights_zero():
# #         for i in weights.values():
# #             if i!=0:
# #                 return False
# #         return True

# #     while True:
# #         if correct + wrong >=10:
# #             break
        
     
        
        
# #         if(inp== 'Done'):
# #             break
# #         if(inp=='w'):
# #             print(weights)
# #             continue
# #         flip = random.choice([True, False])
# #         if not flip:
# #             # if normal
# #             choice = (random.choices(list(dic.keys()),list(weights.values() )))[0]
# #             inp = (input(choice))
# #             if inp == dic[choice]:
# #                 print ('Bravo! That is correct')
# #                 weights[choice]-=1
# #                 correct+=1
# #                 print (f'correct: {correct}, wrong: {wrong}')
# #         else:
# #             print (f'Naah! That is wrong. The correct answer for {choice} is {dic[choice]} ')
# #             weights[choice]+=2
# #             wrong+=1
# #             print (f'correct: {correct}, wrong: {wrong}')

# #         else:
# #             pass
        
    
        
# #         if not flip: int(inp)
# #         if flip: wei
        
# #     print(weights)

# def rotate_word(s, n):
#     out = ''
#     for letter in s:
#         # if ord(letter)<107:
#         #     out += chr(ord(letter)+(n+26)) 
#         out += chr((ord(letter)-96 +n)%26 + 96)
         

        
#     return out

# # def rotate_sentence(s, n):
# #     words= s.split(' ')
# #     out = []
# #     for word in words:
      
# #         out.append( rotate_word(word, n))
# #         print (out)
# #     return ' '.join(out)
# # import math
# # import random

# # def avoiders(filename, forbidden):
# #     fin = open(filename)
# #     # forbidden = input('Enter forbidden letters')
# #     x= 0
# #     for line in fin:
# #         word = line.strip()
# #         if avoids(word, forbidden):
# #             # print(word)
# #             x+=1
# #     return x

# # def has_no_e(word):
# #     for letter in word:
# #         if letter == 'e':
# #             return False
# #     return True


# # def avoids(word, forbidden):
# #     for letter in word:
# #         if letter in forbidden:
# #             return False
# #     return True

# # def best_10():
# #     filename = 'words.txt'
# #     letters = [chr(i) for i in  range(97, 123)]
# #     single = {letter:avoiders(filename, letter) for letter in letters}
# #     # maxies = [chr(i) for i in  range(97, 107)]

# #     besties = []
# #     for (letter, avoided) in single.items():
# #         if math.log10(avoided) >=5:
# #             besties+= letter

# #     return besties

# # def permutate(string):
    
# #     chrs = []
# #     for char in string:
# #         chrs.append(char)
# #     random.shuffle(chrs)
# #     return ''.join(chrs)

# # def ally(string):
# #     out = []
# #     while len(out) < math.factorial(len(string)):
# #         x = permutate(string)
# #         if x not in out:
# #             out.append(x)


# #     return out

# # def has_meaning(string):
# #     fin = open('words.txt')
# #     words= []
# #     for line in fin:
# #         word = line.strip()
# #         words.append(word)
        
# #     if string.lower() in words:
# #         return True
# #     else:
# #         return False
    
# # def uses_only(word, letters):
# #     for letter in word:
# #         if letter not in letters:
# #             return False
# #     return True
# def all_words():
#     fin = open('words.txt')
#     words= {}
#     for line in fin:
#         word = line.strip()
#         words[word] = None
#     return words

# def all_words0():
#     fin = open('words.txt')
#     words= []
#     for line in fin:
#         word = line.strip()
#         words.append(word)
#     return words

# # def uses_all(word, letters):
# #     for letter in letters:
# #         if letter not in word:
# #             return False
# #     return True


# # def is_abecedarian(string):
# #     for (i, char) in enumerate(string):
# #         if i<len(string)-1:
# #             if char > string[i+1]:
# #                 return False
# #     return True
        
# # def is_three_double(string):
# #     if len(string)<6:
# #         return False
# #     for (i, char) in enumerate(string[:-5]):

# #         if string[i]==string[i+1] and string[i+2]==string[i+3] and string[i+4]==string[i+5]:
# #             return True
# #     return False


# # def odometer():
# #     """
# #     We are looking for a six digit number , n ,with the following characterstics
# #     1. n has the last 4 digits pallindromic
# #     2. n+1 has the last 5 digits pallindromic
# #     3. n+2 has the middle 4 digits pallindromic
# #     4. n+3 has all 6 digits pallindromic!
# #     What is the n?
# #     """

# #     # all_six_digits = [str(i).rjust(6,'0') for i in range(10**6)]
# #     # for num_string in all_six_digits:
# #     #     if is_palindrome(num_string[:-5:-1]) and :
# #     #         print(num_string)
# #     for i in range(10**6):
# #         if is_palindrome(str(i).rjust(6,'0')[:-5:-1]) and is_palindrome(str(i+1).rjust(6,'0')[:-6:-1]) and is_palindrome(str(i+2).rjust(6,'0')[1:5:]) and is_palindrome(str(i+3).rjust(6,'0')):
# #             print(str(i).rjust(6,'0'))

# # def is_reverse(n, m):
# #     if str(m)[::-1] == str(n):
# #         return True
# #     else:
# #         return False
    
# # def all_reverse_in_the_past(my_age, mom_age):
# #     k = 0
# #     for i in range(my_age):
# #         if is_reverse(my_age-i, mom_age-i):
# #             k+=1
# #             print(my_age-i,mom_age - i)
# #     return k 

# # def all_reverse_next_twenty(my_age, mom_age):
# #     k = 0
# #     for i in range(510):
# #         if is_reverse(my_age+i, mom_age+i):
# #             k+=1
# #             print(my_age+i,mom_age + i)
# #     return k 
# # def nested_sum(li):
# #     sumed = []
# #     for l in li:
# #         sumed.append(sum(l))
# #     return sum(sumed)

# # def cummulative(li):
# #     cum = [li[0]]
# #     for i in li[1:]:
# #         cum.append(cum[-1]+i)
# #     return cum

# # def middle(li):
# #     del[li[0]]
# #     del[li[-1]]
#     # return li

# def is_sorted(lis):
#     for (i, num) in enumerate(lis[:-1]):
#         if num> lis[i+1]:
#             return False
#     return True
            
# def is_anagram(word_1, word_2):
#     x = list(word_1)
#     y = list(word_2)
#     x.sort() 
#     y.sort()
#     if x ==y:
#         return True
#     else:
#         return False
    
    

# # def has_duplicates(lis):
# #     x = lis[:]
# #     for member in lis:
# #         x.remove(member)
# #         if member in x:
            
# #             return True
# #     return False
# # # import random

# # [has_duplicates([random.randint(1,365) for _ in range(23)] )for i in range(100)].count(True)

# def remove_duplicates(lis):
#     x = lis[:]
#     for (i,val) in enumerate(x):
#         if val in x[i+1:]:
#             lis.remove(val)
# import time

# def using_append():
#     x = all_words()
#     y = []
#     f =time.time()
#     for word in x:
#         y.append(word[-1])
#     s = time.time()
#     return s-f


# def using_concat():
#     x = all_words()
#     y = []
#     f =time.time()
#     for word in x:
#         y+= [word[-1]]
#     s = time.time()
#     return y

# def bisect(lis, target):
#     min = 0
#     max = len(lis)-1
#     while True:
        
#         if max < min:
#             return -1
#         guess = int((max + min )/2)
#         if lis[guess] == target:
#             return guess
#         elif lis[guess] < target:
#             min = guess +1
#         elif lis[guess] > target:
#             max = guess -1 


# def reverse_pair():
#     words = all_words()
#     reverse_pairs = []
#     for (i, word) in enumerate(words):
#         if bisect(words[i+1:], word[::-1])>0:
#             reverse_pairs.append(word)
#     return [(word, word[::-1] ) for word in reverse_pairs]
            

    
#     # if lis==[]:
#     #     return None
#     # mid_ind = int(len(lis)/2)
#     # mid = lis[mid_ind]
#     # if target==mid:
#     #     return mid_ind
#     # elif target>mid:
#     #     return bisect(lis[mid_ind:], target)
#     # elif target<mid:
#     #     return bisect(lis[:mid_ind], target)
# def divide(str):
#     x = ''
#     y = ''
#     z= ''
#     for (i, char) in enumerate(str):
#         if i%3==0:
#             x = x+char
#         elif i%3==1:
#             y = y+char
#         else:
#             z = z+char

#     return [x, y, z]

# def interlocked():
#     words = all_words()
#     all_interlocks = {}
#     for word in words:
#         divs = divide(word)

#         if bisect(words,divs[0]):
#             if bisect(words, divs[1]):
#                 if bisect(words, divs[2]):
#                     all_interlocks[word] = divs
#     return all_interlocks
            


    
# # def all_combin(names):
# #     # names = ['betty', 'tsega', 'robel', 'aklil', 'demax']
# #     combs = set()
# #     for i in range(5):
# #         for j in range(5):
# #             for k in range(5):
# #                 for l in range(5):
# #                     for m in range(5):
# #                         stri = names[0][i] + names[1][j] + names[2][k] + names[3][l] + names[4][m]
# #                         combs.add(stri)
# #     return combs
    
# # def comb_w_meaning(names):
# #     words= all_words()
# #     combs = all_combin(names)
# #     out = []
# #     for string in combs:
# #         if string in words:
# #             out.append(string)
# #     return out
# # import itertools


# # {
# #  'tetra': ['tsega', 'demax', 'betty', 'robel', 'aklil'],
# #  'omega': ['robel', 'demax', 'betty', 'tsega', 'aklil'],
# #  'lyase': ['robel', 'betty', 'aklil', 'tsega', 'demax'],
# #  'odyls': ['robel', 'demax', 'betty', 'aklil', 'tsega'],
# #  'eidos': ['betty', 'aklil', 'demax', 'robel', 'tsega'],
# # #  'delta': ['demax', 'tsega', 'robel', 'betty', 'aklil'],x
# #  'artel': ['demax', 'robel', 'tsega', 'betty', 'aklil']
# #  }


# def has_duplicates(lis):
#     dic = {}
#     for i in lis:
#         if i in dic:
#            return True
#         else:
#            dic[i] =1
#     return False
    
# def rotate_word(s, n):
#     out = ''
#     for letter in s:
#         # if ord(letter)<107:
#         #     out += chr(ord(letter)+(n+26)) 
#         out += chr((ord(letter)-96 +n)%26 + 96) 
#     return out
# def rotate_pairs():
#     pairs = {}
#     words = all_words()
#     for word in words:
#         rot13 = rotate_word(word, 13)
#         if rot13 in words:
#             if rot13 not in pairs:
#                 pairs[word] = rot13

#     return pairs

# def homonym_puzzler():
#     prc = {}
#     words = all_words()
#     out = []
#     infile = open('pronounciation.txt')
#     for line in infile:
#         line = line.strip()
#         x = line.split(' ',1)
        
#         prc[x[0]] = x[1]
#     for word in words:
#         word = word.upper()
#         trunc1 = word[1:]
#         trunc2 = word[0] + word[2:]
#         if trunc1 in prc and trunc2 in prc and word in prc:
#             if prc[word] == prc[trunc1] and prc[word] == prc[trunc2]:
#                 out.append(word)

#     return out


def most_frequent():
    infile = open("text.txt")
    string = ''
    for line in infile:
        x = line.strip()
        string = string + x
    
    a = dict((chr(97+i),0) for i in range(26))
    for char in string:
        try:
            a[char.lower()] +=  1
        except:
            continue
    rev = []
    for lt, f in a.items():
        rev.append((f, lt))
    freq = sorted(tuple(rev), reverse= True)
    out = []
    for f, lt in freq:
        # print(lt)
        out.append(lt)
    return out

def anagrams():
    words = all_words()
    anagrams = {}
    for word in words:
        letters = tuple(sorted(list(word)))
        if letters in anagrams:
            anagrams[letters].append(word) 
        else:
            anagrams.update({letters: [word] })
    for letters,words in anagrams.items():
        if len(words) <2:
            anagrams.__delitem__(letters)
    return anagrams.values()