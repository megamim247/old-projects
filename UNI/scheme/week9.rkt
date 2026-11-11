#lang racket
(define inc (lambda(incop incamount) (lambda(x) (incop incamount x))))
(define add4 (inc + 4))
(add4 5)