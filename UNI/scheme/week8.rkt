#lang racket
(define Library (list 'library  'book 'chair ))
(define Dungeon (list 'dungeon 'skeleton Library))
(define Cellar  (list 'cellar 'treasure 'rats  Dungeon ))
(define Fridge  (list 'fridge 'sausages 'unidentified_head  ))
(define Kitchen   (list 'kitchen Cellar Fridge))
(define DiningRoom (list 'diningRoom 'table Library Kitchen)  ) 
(define Bathroom  (list 'bathroom 'toilet 'bath 'ghost  Dungeon))
(define Bedroom  (list 'bedroom 'bed Bathroom))
(define Hall  (list  'hall DiningRoom Kitchen Bedroom 'suit_of_armour))
(define House (list 'house Hall))
(define listremove (lambda (L) (cond
((null? L) '())
((list? (car L)) (listremove (cdr L)))
(#t (cons (car L) (listremove (cdr L))))
)))
(define objects (lambda (x S) (cond
((null? S) '())
((list? (car S)) 
    (cond 
    ((null? (objects x (car S))) (objects x (cdr S)))
    (#t (objects x (car S)))
    ))
((equal? (car S) x) (listremove (cdr S)))
(#t (objects x (cdr S)))
)))

(objects 'hall House)
(objects 'dungeon House)