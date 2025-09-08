#round(X [,N]) rounds the number X to N fractional
#digits from the decimal point. If N is not provided
# It is taken to be zero.

round(27.168459, 1)# -> 27.2
round(27.168459, 2)# -> 27.17
round(27.168459, 3)# -> 27.168
round(27.168459, 4)# -> 27.1684
round(27.168459, 5)# -> 27.16846
round(27.168459, 6)# -> 27.168469

#abs(X)
#returns the absolute value of X
abs(-273)# -> 273
abs(-1.27)# -> 1.27
abs(0)# -> 0
abs(32)# -> 32

#pow(X, Y)
#Calculates X to the power of Y.(Same as X**Y)
pow(5, 2)# -> 25
pow(2, 16)# -> 65536
pow(4, 3)# -> 64