"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):

        resultado = []
        for i, caracter in enumerate(reversed(s)):
            posicion = len(s) - i
            resultado.append(f"{caracter}-{posicion}")
        return resultado


texto1 = ["a", "b", "c", "d", "e"]
resultado1 = fn_hack_8(texto1)
print(resultado1)  # Salida esperada: ["e-5", "d-4", "c-3", "b-2", "a-1"]

texto2 = ["a", "b", "c"]
resultado2 = fn_hack_8(texto2)
print(resultado2)  # Salida esperada: ["c-3", "b-2", "a-1"]

texto3 = ["a", "b", "c", "d"]
resultado3 = fn_hack_8(texto3)
print(resultado3)  # Salida esperada: ["d-4", "c-3", "b-2", "a-1"]

texto4 = ["a", "b"]
resultado4 = fn_hack_8(texto4)
print(resultado4)  # Salida esperada: ["b-2", "a-1"]
    

