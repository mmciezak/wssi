zadanie 1
1.1
A - x i y to rodzeństwo(rodzone)
B - kuzyni (y to syn brata matki x)
C - x jest babcią wnuczki y
D - y to przybrany ojciec lub matka dla x
E - przyrodnie rodzeństwo
F - x to bratanica/bratanek dla y
G - kazirodztwo (syn mlodszego brata y dla x / dziecko rodzica mlodszego brata x dla y)

%zadanie 2

mezczyzna(jan).
mezczyzna(pawel).
mezczyzna(maciek).
mezczyzna(tadeusz).
mezczyzna(marcin).
mezczyzna(kuba).
mezczyzna(slawomir).
mezczyzna(antoni).

rodzic(antoni,grazyna).%dziadek pawla od strony matki
rodzic(antonina,grazyna).

rodzic(slawomir,tadeusz).%bracia, dziadek pawla od strony ojca
rodzic(slawomira,tadeusz).
rodzic(slawomir,jan).
rodzic(slawomira,jan).

rodzic(jan, pawel). %rodzenstwo 
rodzic(grazyna, pawel).
rodzic(jan, maciek).
rodzic(grazyna, maciek).
rodzic(jan, ola).
rodzic(grazyna, ola).

rodzic(tadeusz, marcin). %kuzyn pawla
rodzic(agnieszka, marcin).


rodzic(jan, kuba). %przyrodni brat pawla i macka
rodzic(malgosia, kuba).

kobieta(X) :-
    \+ mezczyzna(X).

ojciec(X,Y) :- 
    rodzic(X,Y), 
    mezczyzna(X).

matka(X,Y) :- 
    rodzic(X,Y), 
    kobieta(X).

corka(X,Y) :- 
    rodzic(Y,X), 
    kobieta(X).

brat_rodzony(X,Y) :- 
    rodzic(Z,X), 
    rodzic(Z,Y), 
    rodzic(W,X), 
    rodzic(W,Y), 
    mezczyzna(X), 
    Z \= W,
    X \= Y.

brat_przyrodni(X,Y) :- 
    rodzic(Z,X), 
    rodzic(Z,Y), 
    mezczyzna(X), 
    \+ brat_rodzony(X,Y), 
    X \= Y.

kuzyn(X,Y) :- 
    rodzic(Z,X), 
    rodzic(W,Y), 
    (   
    	brat_przyrodni(Z,W);
    	brat_rodzony(Z,W)
    ).

dziadek_od_strony_ojca(X,Y) :- 
    ojciec(Z,X), 
    rodzic(Y,Z),
	mezczyzna(Y).

dziadek_od_strony_matki(X,Y) :- 
    matka(Z,X), 
    rodzic(Y,Z),
    mezczyzna(Y).

dziadek(X,Y) :- 
    rodzic(Z,X), 
    rodzic(Y,Z), 
    mezczyzna(Y), 
    X \= Y.

babcia(X,Y) :- 
    matka(X,Z), 
    rodzic(Z,Y).

wnuczka(X,Y) :- 
    rodzic(X,Z), 
    rodzic(Z,Y), 
    kobieta(Y), 
    X \= Y.

przodek_do2pokolenia_wstecz(X,Y) :- 
    rodzic(X,Z), 
    rodzic(Z,Y).

przodek_do3pokolenia_wstecz(X,Y) :- 
    rodzic(X,Z), 
    rodzic(Z,W), 
    rodzic(W,Y).




