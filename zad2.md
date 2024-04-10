# zadanie 1
1.1
A - x i y to rodzeństwo(rodzone)
B - kuzyni (y to syn brata matki x)
C - x jest babcią wnuczki y
D - y to przybrany ojciec lub matka dla x
E - przyrodnie rodzeństwo
F - x to bratanica/bratanek dla y
G - kazirodztwo (syn mlodszego brata y dla x / dziecko rodzica mlodszego brata x dla y)

# zadanie 2

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


# zad 1 dla chetnych

czlowiek(markus).
wladca(cezar).

pompejanczyk(X) :- 
    czlowiek(X),
    rzymianin(X).

pompejanczyk(markus).

rzymianin(X) :-    
    (   
    lojalny_wobec(X,Y); 
    nienawidzi(X,Y)
    ),
    wladca(Y).

lojalny_wobec(X, Y) :- 
    czlowiek(X), 
    wladca(Y),
    \+ probuje_zamachu(X, Y).

nienawidzi(X, Y) :- 
    probuje_zamachu(X, Y).

probuje_zamachu(markus, cezar).


![obraz](https://github.com/mmciezak/wssi/assets/127038795/72926c94-2f45-432c-9dad-561e11017231)

# zad 2 dla chetnych

jadalne(X) :-
    pozywienie(X).

lubi(jan, X) :- 
    pozywienie(X).

pozywienie(jablka).
pozywienie(kurczak).
pozywienie(orzeszki).

nie_zyje(X) :-
    je(X, Y),
    \+ jadalne(Y).

zyje_i_cos_zjadl(X, Y) :-
    je(X, Y),
    jadalne(Y).

je(basia, X) :- 
    je(adam, X).

je(adam,orzeszki).

![obraz](https://github.com/mmciezak/wssi/assets/127038795/87337b93-baed-4dd0-bd4e-d3f1dce4017d)

# zad 3 dla chetnych

urodzil_sie(markus, 40).
pompejanczyk(markus).
zniszczono_pompeje(79).
dlugosc_zycia(150).

zyje(X, Y) :- 
    urodzil_sie(X, Z), 
    Z + 150 >= Y, 
    \+ zniszczono_pompeje(_).


![obraz](https://github.com/mmciezak/wssi/assets/127038795/9e07170a-2612-4630-95a4-6bf19b0cf240)

