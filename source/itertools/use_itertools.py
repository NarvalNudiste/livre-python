#itertools 
# Chain, slice, ...
# Source : https://www.youtube.com/watch?v=xK7E2YmjyAc

#import de la librairie
from itertools import *

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ajout de nouvelles fonctions
#COUNT_BEGIN
#Attention boucle infini
'''for i in count(0, 0.4):
    print(i)'''

#génére une liste de 0..10 par step 1
#grace à la fonction iSlice()
for i in islice(count(), 0, 11, 1):
    print(i)
#COUNT_END
<<<<<<< HEAD
=======

>>>>>>> ajout de nouvelles fonctions


#CHAIN_BEGIN
=======
>>>>>>> refactor name
=======

<<<<<<< HEAD
#CONFIG_BEGIN
>>>>>>> ajout de la config + fonction compress
=======
#CHAIN_BEGIN
>>>>>>> Ajout de la fonction map et compress
a = [0, 1, 2, 3, 4]
b = ["zero", "un", "deux", "trois", "quatre"]
c = ["a", "b", "c", "d"]

<<<<<<< HEAD
<<<<<<< HEAD
for i in chain(a, b, c):
    print(i);

print(list(chain(a, b, c)))

print(list(chain(a[:1], b[:1], c[:1])))

print(list(chain(a[0:2], b[0:2], c[0:2])))
#CHAIN_END





#COMPRESS_BEGIN
ListeName = ["Johnny", "Toto", "Tata", "Roger", "Steve"]
filter_binaire = [1, 0, 1, 0, 1]

for i in compress(a, filter_binaire):
    print(i);

#on récupere sous forme de liste
b = list(compress(a, filter_binaire))
print(b)
#COMPRESS_END

#FILTER_BEGIN
listeNumber = [1,2,3,5,6];
listeNumberOdds = list(filter(lambda x:x%2, listeNumber)) #[0, 2, 4]
listeNumberEvens = list(filterfalse(lambda x:x%2, listeNumber)) #[1, 3, 5]

print(listeNumberOdds);
print(listeNumberEvens)
#FILTER_END

#MAP_BEGIN
listeNumber = [1, 2, 3, 4]

#fonction de callback
def cube(x):
    return x**3

listeNumberCube = list(map(cube, listeNumber))
print(listeNumber)     #[1, 2, 3, 4]
print(listeNumberCube) #[1, 8, 27, 64]

#autre syntaxe pour le même résultat
listeNumberCubeV2 = list(map(lambda x : x**3, listeNumber))
print(listeNumberCubeV2) #[1, 8, 27, 64]
#MAP_END

#DROPWHILE_BEGIN

dropwhile = list(dropwhile(lambda x:x<5, [1, 4, 23, 2,42,23,2]))
print(dropwhile) #[23, 2, 42, 23, 2]

#DROPWHILE_END

#TAKEWHILE_BEGIN
takewhile = list(takewhile(lambda x:x<5, [1, 4, 54, 23,2,42,23,2]))
print(takewhile) #[1, 4]
#TAKEWHILE_END
=======
#CHAIN_BEGIN
=======
>>>>>>> Ajout de la fonction map et compress
for i in chain(a, b, c):
    print(i);

print(list(chain(a, b, c)))

print(list(chain(a[:1], b[:1], c[:1])))

print(list(chain(a[0:2], b[0:2], c[0:2])))
#CHAIN_END


<<<<<<< HEAD
#COUNT_BEGIN
#Attention boucle infini
'''for i in count(0, 0.4):
    print(i)
'''
#génére une liste de 0..100 par step 1
for i in islice(count(), 0, 11, 1):
    print(i)
#COUNT_END
<<<<<<< HEAD
>>>>>>> refactor name
=======
=======

>>>>>>> ajout de nouvelles fonctions


#COMPRESS_BEGIN
ListeName = ["Johnny", "Toto", "Tata", "Roger", "Steve"]
filter_binaire = [1, 0, 1, 0, 1]

for i in compress(a, filter_binaire):
    print(i);

#on récupere sous forme de liste
b = list(compress(a, filter_binaire))
print(b)
#COMPRESS_END
<<<<<<< HEAD
>>>>>>> ajout de la config + fonction compress
=======

#FILTER_BEGIN
listeNumber = [1,2,3,5,6];
listeNumberOdds = list(filter(lambda x:x%2, listeNumber)) #[0, 2, 4]
listeNumberEvens = list(filterfalse(lambda x:x%2, listeNumber)) #[1, 3, 5]

print(listeNumberOdds);
print(listeNumberEvens)
#FILTER_END

#MAP_BEGIN
listeNumber = [1, 2, 3, 4]

#fonction de callback
def cube(x):
    return x**3

listeNumberCube = list(map(cube, listeNumber))
print(listeNumber)     #[1, 2, 3, 4]
print(listeNumberCube) #[1, 8, 27, 64]

#autre syntaxe pour le même résultat
listeNumberCubeV2 = list(map(lambda x : x**3, listeNumber))
print(listeNumberCubeV2) #[1, 8, 27, 64]
#MAP_END
<<<<<<< HEAD
>>>>>>> Ajout de la fonction map et compress
=======

#DROPWHILE_BEGIN

dropwhile = list(dropwhile(lambda x:x<5, [1, 4, 23, 2,42,23,2]))
print(dropwhile) #[23, 2, 42, 23, 2]

#DROPWHILE_END

#TAKEWHILE_BEGIN
takewhile = list(takewhile(lambda x:x<5, [1, 4, 54, 23,2,42,23,2]))
print(takewhile) #[1, 4]
#TAKEWHILE_END
>>>>>>> ajout de nouvelles fonctions