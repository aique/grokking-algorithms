# El algoritmo de Euclides para hallar el máximo común divisor es el siguiente:
#   Si A = 0 entonces MCD(A,B)=B.
#   Si B = 0 entonces MCD(A,B)=A .
#   Escribe A en la forma cociente y residuo (A = B ⋅Q + R).
#   Encuentra MCD(B,R), ya que MCD(A,B) = MCD(B,R).
#
# https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


def mcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    return mcd(b, a % b)


print(mcd(270, 192))
print(mcd(1680, 640))
