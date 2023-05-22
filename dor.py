from turtle import Turtle
# iniciar uma turtle 
# eu que fiz 
t = Turtle()
# Definir a velocidade
t.speed(1)
while True: 
    direcao = input('para qual direção devemos ir? "F:frente" ou "t:traz" ')
    if direcao == 'f':
        pixels = int(input('quantos pixels a turtle deve se movimentar para frente '))
        angulo_de_rotacao = input('qual angulo a turtle deve seguir? d:direita, e:esquerda, n:não rotacionar')
        if angulo_de_rotacao == 'd':
         pixels = int(input('quantos pixels a Turtle deve se movimentar para a direita '))
         t.right(pixels)
        elif angulo_de_rotacao =='e':
            pixels = int(input('quantos pixels a Turtle deve se movimentar para a esquerda '))  
            t.left(pixels)
        t.forward(pixels)
    if direcao == 't':
        pixels = int(input('quantos pixels a turtle deve se movimentar para traz'))
        angulo_de_rotacao = input('qual angulo a turtle deve seguir? d:direita, e:esquerda, n:não rotacionar')
        if angulo_de_rotacao == 'd':
            pixels = int(input('quantos pixels a Turtle deve se movimentar para a direita '))
            t.right(pixels)
        elif angulo_de_rotacao =='e':
            pixels = int(input('quantos pixels a Turtle deve se movimentar para a esquerda '))  
            t.left(pixels) 
        t.backward(pixels) 
    continuar = input('continuar andando?  "sim" ou "nao?" ')
    if continuar not in('sim, s'):
        break
print('fim do programa')


            
    
    
