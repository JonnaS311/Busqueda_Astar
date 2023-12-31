from ciudades_nodo import Ciudad


bogota = Ciudad("bog", 0, 100)
tunja = Ciudad("tun", 1,  91)
yopal = Ciudad("yop", 2,  120)
bucaramanga = Ciudad("buc", 3,  80)
cucuta = Ciudad("cuc", 4, 110)
valledupar = Ciudad("val", 5, 50)
santa_marta = Ciudad("san", 6, 43)
riohacha = Ciudad("rio", 7, 75)
barranquilla = Ciudad("bar", 8, 18)
cartagena = Ciudad("car", 9, 0)
sincelejo = Ciudad("sin", 10, 25)
medellin = Ciudad("med", 11,  41)
manizales = Ciudad("man", 12,  52)
pereira = Ciudad("per", 13, 63)
cali = Ciudad("cal", 14, 77)
popayan = Ciudad("pop", 15, 88)
pasto = Ciudad("pas", 16, 121)
neiva = Ciudad("nei", 17,  130)
leticia = Ciudad("let", 18, 200)
villavicencio = Ciudad("vil", 19, 118)

lista_ciudades = [
                bogota,tunja,yopal,bucaramanga,cucuta,valledupar,santa_marta,riohacha,barranquilla,cartagena,
                sincelejo,medellin,manizales,pereira,cali,popayan,pasto,neiva,leticia,villavicencio
                ]
adyacentes = [
    #0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
    [0 , 7 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 10, 0 , 0 , 0 , 0 , 0 , 12], #0
    [7 , 0 , 5 , 11, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #1
    [0 , 5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #2
    [0 , 11, 0 , 0 , 15, 20, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #3
    [0 , 0 , 0 , 15, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #4
    [0 , 0 , 0 , 20, 0 , 0 , 8 , 0 , 20, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #5
    [0 , 0 , 0 , 0 , 0 , 8 , 0 , 15, 11, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #6
    [0 , 0 , 0 , 0 , 0 , 0 , 15, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #7
    [0 , 0 , 0 , 0 , 0 , 20, 11, 0 , 0 , 6 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #8
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 6 , 0 , 13, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #9
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 13, 0 , 16, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #10
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 16, 0 , 8 , 8 , 13, 0 , 25, 0 , 0 , 0 ], #11
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 8 , 0 , 4 , 0 , 0 , 0 , 0 , 0 , 0 ], #12
    [10, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 8 , 4 , 0 , 12, 0 , 0 , 0 , 0 , 0 ], #13
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 13, 0 , 12, 0 , 8 , 0 , 0 , 0 , 0 ], #14
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 8 , 0 , 10, 15, 0 , 0 ], #15
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 25, 0 , 0 , 0 , 10, 0 , 0 , 0 , 0 ], #16
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 15, 0 , 0 , 20, 0 ], #17
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 20, 0 , 26], #18
    [12, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 26, 0 ]] #19

visitados = [
    #0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #0
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #1
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #2
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #3
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #4
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #5
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #6
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #7
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #8
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #9
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #10
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #11
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #12
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #13
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #14
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #15
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #16
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #17
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], #18
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]] #19
