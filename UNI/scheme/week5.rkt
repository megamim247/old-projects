#lang racket
(define smallestList (lambda (L) (cond
((equal? (length L) 1) (car L))
((< (length (car L)) (length (smallestList (cdr L)))) (car L))
(#t (smallestList (cdr L)))
)))

(define joinOnTo (lambda (L L2) (cond
((null? L) L)
((null? L2) L)
(#t (joinOnTo (cons (car L2) L) (cdr L2) )))
))
(define reverseList (lambda (L) (cond
((null? L) '())
(#t (cons (lastInList L) (reverseList (allExceptLast L))))
)))
(define lastInList (lambda (L) (cond
((=(length L) 1) (car L))
(#t (lastInList (cdr L)))
)))
(define allExceptLast (lambda (L) (cond
((=(length L) 1) '())
(#t (cons (car L) (allExceptLast (cdr L))) )
)))

(define flatten (lambda (L) (cond 
((=(length L) 1) (car L))
((list? (car L)) (joinOnTo (flatten (cdr L)) (reverseList (car L))))
(#t (cons (car L) (flatten (cdr L))))
)))

(flatten '((I see) said Tom (coldly)))