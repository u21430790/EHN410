q=173  ;
alpha=19 ;

#alice
Xa = 8
Ya = (alpha^Xa) % q 
K = (Yb^Xa) % q

#bob
Xb = 138
Yb = (alpha^Xb % q) 
K = (Ya^Xb) % q


"""
OUTPUT 
Xa =
     8
Ya =
   109
K =
   135
Xb =
   138
Yb =
    71
K =
   13
"""