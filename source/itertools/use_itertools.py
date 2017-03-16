#itertools 
# Chain, slice, ...
# Source : https://www.youtube.com/watch?v=xK7E2YmjyAc

#import de la librairie
from itertools import *


#CONFIG_BEGIN
a = [0, 1, 2, 3, 4]
b = ["zero", "un", "deux", "trois", "quatre"]
c = ["a", "b", "c", "d"]
#CONFIG_END

#CHAIN_BEGIN
for i in chain(a, b, c):
    print(i);

print(list(chain(a, b, c)));

print(list(chain(a[:1], b[:1], c[:1])));

print(list(chain(a[0:2], b[0:2], c[0:2])));
#CHAIN_END


#COUNT_BEGIN
#Attention boucle infini
for i in count(0, 0.4):
    print(i);

#génére une liste de 0..100 par step 1
for i in islice(count(), 0, 101, 1):
    print(i);
#COUNT_END


#COMPRESS_BEGIN
a = ["Johnny", "Toto", "Tata", "Roger", "Steve"];
filter_binaire = [1, 0, 1, 0, 1];

for i in compress(a, filter_binaire):
    print(i);

#on récupere sous forme de liste
b = list(compress(a, filter_binaire));
print(b);
#COMPRESS_END
