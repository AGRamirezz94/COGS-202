import random 

#Nouns
N = [' car ', ' tree ', ' whale ', ' pie ', ' dog ', ' phone ']

#Article
A = 'the '

#Verbs
V = [' ran ', ' hit ', ' smashed ', ' grazed ']

#Noun phrase = <Article>, <Noun>
def get_np():
    print A + random.choice(N)

#Predicate = <Verb>, <Article>, <Direct Object>
def get_p():
    print random.choice(V) + A + random.choice(N)
    
#print <Noun phrase> <Predicate> example
for i in range (1, 10):
    get_np() , get_p()

