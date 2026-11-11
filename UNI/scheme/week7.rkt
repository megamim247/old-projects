#lang racket
(define member? (lambda (e L) (cond
((null? L)  #f)
((equal? (car L) e) #t)
(#t (member? (cdr L)))
)))

(define maxFreq (lambda (L) (cond
((null? (cdr L)) (list (car L)))
((member? (car L) (maxFreq L)) (list (car L))
(#t )
))))

(define insertBy (lambda (C E S) (cond
((null? S) (list E))
((C E (car S)) (cons E S))
(#t (cons (car S) (insertBy C E (cdr S)))))))

(define mySort (lambda (C L) (cond
    ((null? L) '())
    (#t (insertBy C (car L) (mySort C (cdr L)))))
))
(mySort < '(4 6 1 3 2 5))