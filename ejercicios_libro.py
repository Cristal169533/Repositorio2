

!pip install --target=$nb_path nacal
from nacal import *

a= Vector ([1,2,3])
b= Vector ([4,5,6])
(a+b)

"""$\begin{pmatrix}5\\ 7\\ 9\end{pmatrix}$

"""

a= Vector ([1,2])
b= Vector ([4,5])
c= Vector ([1,0])
(a)+(b+c)

"""$\begin{pmatrix}6\\ 7\end{pmatrix}$

"""

a= Vector ([4,5,6])
b= Vector ([0,0,0])
(a+b)

"""$\begin{pmatrix}4\\ 5\\ 6\end{pmatrix}$"""

a= Vector ([4,5,6])
b= Vector ([-4,-5,-6])
(a+b)

"""$\begin{pmatrix}0\\ 0\\ 0\end{pmatrix}$

"""

a= Vector([1,-1])
b= Vector([4,5])
2*(a+b)

"""$\begin{pmatrix}10\\ 8\end{pmatrix}$

"""

a= Vector([1,2,3])
(2+3)*(a)

"""$\begin{pmatrix}5\\ 10\\ 15\end{pmatrix}$"""

a= Vector([1,2])
2*(3*(a))

"""$\begin{pmatrix}6\\ 12\end{pmatrix}$"""

a= Vector([1,2,3])
(a)

"""$\begin{pmatrix}1\\ 2\\ 3\end{pmatrix}$

"""