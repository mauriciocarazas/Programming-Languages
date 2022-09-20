/*alumno(marcos).
alumno(andre).
alumno(roberto).
escribirSinFail :- alumno(X), write(X).
escribirConFail :- alumno(X), write(X), nl, !,fail.*/


/*guess_number :-N is random(5) + 1,repeat,leer_datos(G),process_guess(G, N).
leer_datos(G):-write('Input your guess (from 1 to 5): '),read(G).
process_guess(N, N):-write('You win!'), nl.
process_guess(I, N):-I \= N,write('No, no!'), nl,fail.*/

/*repite :- repeat,
write('Digite el termino:'), read(Term), ( (Term == fin -> !; process(Term), fail )).
process(Term) :- write('==>'), write(Term), nl.*/



%ACTIVIDAD

/*1) Cree un programa en Prolog que lea un número, calcule e imprima el cuadrado
de ese número, el programa debe continuar la ejecución hasta que el usuario
digita la palabra ‘stop’.*/


square:- repeat,write('Digite el termino:'), read(Term), ( (Term == stop -> !; process(Term), fail )).
process(Term) :- write('==>'),Z is Term**2, write(Z), nl.


/*2) Cree una regla recursiva con un parámetro que es un número entero, la regla
debe imprimir los valores de cero hasta el número informado. Ej:
?- imprimeHasta(3).
0 1 2 3*/


imprime_hasta(N):- imprime_hasta(0, N).
imprime_hasta(X, Y):- X =< Y, write(X), write(' '), X1 is X + 1, imprime_hasta(X1, Y).


/*3) Usando un acumulador, y solamente las operaciones(+)(-)(*), cree una regla
que calcule X elevado a Y. Asuma X e Y enteros.*/


potencia(_,0,1).

potencia(X,Y,Z) :- Y1 is Y - 1,potencia(X,Y1,Z1), Z is Z1*X.

/*4)Cree una regla para calcular el enésimo término de la serie de Fibonacci. */

fib(0, 0) :- !.
fib(1, 1) :- !.
fib(N, F) :- N > 1, N1 is N-1,  N2 is N-2, fib(N1, F1), fib(N2, F2),F is F1+F2.



/*5)Escriba una regla que informe si el número es primo o no. Un número primo es
aquel divisible solamente por uno y por él mismo. Una de las formas de responder
a esa pregunta sería, tomar ese número y dividirlo por él mismo y después por
todos los números antecesores a él hasta llegar a uno. Asuma que los valores
informados serán mayores que cero.*/


num_div(_,1,1).
 
num_div(N,X,ND):-N>1,X>1, 0 is N mod X,NX is X-1,num_div(N,NX,SD),ND is 1+SD.
 
num_div(N,X,ND):-N>1,X>1,not(0 is N mod X),NX is X-1,num_div(N,NX,ND).
 
num_div(N,ND):-num_div(N,N,ND).
 
es_primo(N):-num_div(N,2).
