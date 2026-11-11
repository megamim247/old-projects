#lang racket
;;lecture 1
(define sumPairs (lambda (x) (cond 
    ((< (length x) 2) 0)
    (#t (+ (* (car x) (car (cdr x))) (sumPairs (cdr x))))
    )))
;;lecture 2
(define bouncer (lambda (x) (cond
    ((null? x)               0                )
    ((< (car x) 18)          (bouncer (cdr x)))
    (#t              (+ (bouncer (cdr x)) 1))
)))
;;(bouncer '(20 17 18 10 4))





;;task
(((lambda (x) (x x))
    (lambda (function)
        (lambda (n)
            (display n)
            (if (zero? n)
                0
                (+ n ((function function) (sub1 n)))
            )
        )
    )
) 5 )

;;((lambda (func x) () (lambda (x) (+ x ))))

(define removeAfter (lambda (E L) (cond
((or (null? L) (equal? (car L) E)) '())
(#t (cons (car L) (removeAfter E (cdr L))))
)))
(removeAfter '(1 lemon) '( (4 apples) (3 bananas) (1 lemon) (1 orange) ) )

(define name (lambda (x) (cond
(()())
(()())
)))