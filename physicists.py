infile = open('physicsts.txt')
dic = {}
withprob = {}
for line in infile:
    try:
        x = line.strip()
        
        x = x.split(' – ' ,1)
        hyp_i = x[1].index('–')
        born = 
        dic[x[0]]= x[1]
    except:
        withprob[line] = 'problem'


infile2 = open('Countries.txt')
countries = []
for line in infile2:
    x = line.strip()
    countries.append(x)

x  = 0
for string in list(dic.values()):
    print(string)
    if 'United States' in string and ',' in string:
        x+=1
nationality = {}
for scientist in dic:
    for country in countries:
        if country in dic[scientist] and 'Nobel' in dic[scientist] and ',' in dic[scientist]:
            nationality[country]= nationality.get(country, 0) + 1 

nationality 
sorted_dict = list(sorted(nationality.items(), key=lambda x: x[1]))

x = 0
for history in dic.values():
    if 'Nobel' in history:
        x+=1
sorted_dict
#inferences
# 93 of the 201 scientists who won a nobel prize are american and 24 of them are shared nationality
#