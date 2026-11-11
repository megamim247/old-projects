#lang racket
(define remove (lambda (x y) (cond
((null? x) '())
((equal? (car x) y)(remove (cdr x) y))
(#t (cons (car x) (remove (cdr x) y)))
)))
(define count (lambda (x y) (cond
((null? x) 0)
((equal? (car x) y) (+ (count (cdr x) y) 1))
(#t (count (cdr x) y))
)))
(define concordance (lambda (L) (cond
((null? L) '())
(#t (cons (cons (car L) (count L (car L))) (concordance (remove L (car L)))))
)))

(define fibonacci (lambda (x) (cond
((= x 0) 0)
((= x 1) 1)
(#t (+ (fibonacci (- x 1)) (fibonacci (- x 2))))
)))

(define removeAllMatches (lambda (Fn L) (cond
    ((null? L) '())
    ((list? (car L)) (cons (removeAllMatches Fn (car L)) (removeAllMatches Fn (cdr L))))
    (#t (cond 
        ((null? L) '()) 
        ((Fn (car L)) (removeAllMatches Fn (cdr L)))
        (#t (cons (car L) (removeAllMatches Fn (cdr L))))
    ))
)))

(removeAllMatches odd? '(1 2 3 4 (11 12 13 14) 15 16))