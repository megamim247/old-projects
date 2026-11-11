#lang racket

(define sumTo (lambda (x) (if (> x 0) (+ x (sumTo (- x 1))) x)))

(define harmonic (lambda (x) (if (> x 0) (+ (/ 1 x) (harmonic (- x 1))) 0)))

(define sumOfF (lambda (n f) ( if (> n 0) (+ (f n) (sumOfF (- n 1) f)) 0)))

(define square (lambda (x) (* x x)))

(define fibonacci(lambda (x) (cond 
((equal? x 1) 1)
(#t ((lambda (x) (cond 
    ((equal? x 2) '(2 1 1))
    ((equal? x 3) '(3 2 1 1))
    (#t (cons (+ (car (fibonacci (- x 2))) (car (fibonacci (- x 1)))) (fibonacci (- x 1)) ) ))) x))
)))

(define sort
  (lambda (L)
    (cond
      ((null? L) L)
      ((null? (cdr L)) L)
      ( #t (divideAndSort '() '() L)))))

(define divideAndSort ;;
  (lambda (F S L)
    (cond
      ((null? L) (mergeSorted (sort F)(sort S))) ;;null unsorted list means F and S must be merged and passed back
      ((null? (cdr L)) (divideAndSort (cons (car L) F) S (cdr L))) ;;if odd number of unsorted elements
      ( #t (divideAndSort (cons (car L) F) (cons (car (cdr L)) S) (cdr (cdr L))))))) ;;first element in F and second element in S

(define (mergeSorted L1 L2) ;;merges F and S
  (cond
    ((null? L1) L2)
    ((null? L2) L1)
    ((<= (car L1) (car L2)) (cons (car L1) (mergeSorted (cdr L1) L2)))
    (#t (cons (car L2) (mergeSorted  L1 (cdr L2))))))