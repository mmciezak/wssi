pogoda(lublin, lato, cieple).
pogoda(lublin, zima, umiarkowana).
pogoda(kair, lato, upalne).
pogoda(kair, zima, bardzo_ciepla).
pogoda(jakutsk, lato, umiarkowane).
pogoda(jakutsk, zima, bardzo_mrozna).

kobieta(grazyna).

mezczyzna(X) :-
    \+ kobieta(X).
	

rodzic(jan,x).
rodzic(grazyna,x).

rodzic(jan,y).
rodzic(grazyna,y).

rodzic(pawel,z).
rodzic(karolina,z).

rodzenstwo(X,Y) :-
    rodzic(jan,Y),
    rodzic(jan,X).

lubi(jan,pawel).

przyjazn(X,Y) :-
    lubi(X,Y),
    lubi(Y,X).

niby_przyjazn(X,Y) :-
    lubi(X,Y);
    lubi(Y,X).

love(jan,grazyna).
love(grazyna,jan).

true_love(X,Y) :-
    love(X,Y),
    love(Y,X).
