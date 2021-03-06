import pygame
from pygame.locals import*

larTela = 1024
altTela = 640
tela = pygame.display.set_mode((larTela, altTela))
clock = pygame.time.Clock()
FPS = 60
pygame.font.init()
font_padrao = pygame.font.get_default_font()
fonte_gool = pygame.font.SysFont(font_padrao, 100)
font_padrao2 = pygame.font.get_default_font()
fonte_tempo = pygame.font.SysFont(font_padrao, 30)
fundo = pygame.image.load("Mesa.Png")
tela_menu= pygame.image.load("MENU.png")
batedor_dir = pygame.image.load('b.png').convert_alpha()
batedor_esq = pygame.image.load('bte.png').convert_alpha()
fim = pygame.image.load("fim.Png")
batedor_dirMask = pygame.mask.from_surface(batedor_dir)
batedor_dirPos = batedor_dir.get_rect()
batedor_esqMask = pygame.mask.from_surface(batedor_dir)
batedor_esqPos = batedor_dir.get_rect()

pygame.display.set_caption("Aero Hockey")

disco = pygame.image.load('D1.png').convert_alpha()
disco2 = pygame.image.load('D2.png')
discobat = disco
preto = (0, 0, 0)
branco = (255, 255, 255)
discoPos = disco.get_rect()
placar = 0
placar2 = 0
sec = 0
tempo = 0
discoMask = pygame.mask.from_surface(disco)
titulo_font = pygame.font.SysFont("LVDC Game Over 2", 50)
menu_titulo = titulo_font.render("", True, branco)
fimjogo = titulo_font.render("", True, branco)
fimjogo2 = titulo_font.render("", True, branco)



def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont("Arial", tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])





disco_x = 250
disco_y = 150

disco2_x = 250
disco2_y = 270

batedor_esq_x = 855
batedor_esq_y = 335

batedor_dir_x = 60
batedor_dir_y = 250


#VELOCIDADE DO BATEDOR
vel_x = 15
vel_y = 14

#VELOCIDADE DO DISCO
velocidade_x = 5
velocidade_y = 4

pygame.display.set_caption("Air Hockey")

menu = True
pygame.init()
while True:

    while menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


            elif event.type == pygame.MOUSEBUTTONDOWN:
               if event.button == 1:
                    menu = False


        tela.blit(tela_menu, (0, 0))
        tela.blit(menu_titulo, (250,400))


        clock.tick(30)

        pygame.display.update()

    eventos = pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        batedor_esq_x -= vel_x
    if keys[pygame.K_RIGHT]:
        batedor_esq_x += vel_x
    if keys[pygame.K_UP]:
        batedor_esq_y -= vel_y
    if keys[pygame.K_DOWN]:
        batedor_esq_y += vel_y

    if keys[pygame.K_a]:
        batedor_dir_x -= vel_x
    if keys[pygame.K_d]:
        batedor_dir_x += vel_x
    if keys[pygame.K_w]:
        batedor_dir_y -= vel_y
    if keys[pygame.K_s]:
        batedor_dir_y += vel_y

    if batedor_esq_x <= 845:
        batedor_esq_x = 845
    if batedor_esq_x >= 855:
        batedor_esq_x = 855

    if batedor_esq_y >= 515:
        batedor_esq_y = 515
    if batedor_esq_y <= 20:
        batedor_esq_y = 20

    if batedor_dir_x <= 70:
        batedor_dir_x = 70
    if batedor_dir_x >= 80:
        batedor_dir_x = 80

    if batedor_dir_y >= 515:
        batedor_dir_y = 515
    if batedor_dir_y <= 20:
        batedor_dir_y = 20

    hit = pygame.mixer.Sound("hit.wav")
    hit2 = pygame.mixer.Sound("hit3.wav")
    gol = pygame.mixer.Sound("G.wav")
    pygame.draw.rect(fundo, (39, 49, 56), [520, altTela - 615, 80, 40])
    texto("" + str(placar2), branco, 50, 550, altTela - 624)

    pygame.draw.rect(fundo, (39, 49, 56), [425,altTela-615,80,40])
    texto("" + str(placar), branco, 50, 450, altTela-624)






#COLISÃO DISCO DIR

    Colisao = (batedor_dir_x - discoPos[0] - disco_x, batedor_dir_y - discoPos[1] - disco_y)

    result = discoMask.overlap(batedor_esqMask, Colisao)
    if result:
        velocidade_x = - velocidade_x-1
        hit.play()
    if abs(batedor_dir_y - disco_y) < 80 and abs(batedor_dir_x - disco_x) < 60:
        velocidade_y = - velocidade_y
    
        hit.play()
        #if disco_y > batedor_dir_x:
         #   disco_y = batedor_dir_y - 50
        #else:
         #   disco_y = batedor_dir_y + 50
            



#COLISÃO DISCO ESQ
    Colisao1 = (batedor_esq_x - discoPos[0] - disco_x, batedor_esq_y - discoPos[1] - disco_y)

    result = discoMask.overlap(batedor_esqMask, Colisao1)
    if result:
        velocidade_x = - velocidade_x+1
        hit.play()


    if abs(batedor_esq_y - disco_y) < 80 and abs(batedor_esq_x - disco_x) < 60:
        velocidade_y = - velocidade_y

#TELA FINAL
    if sec >=0:
        tela.blit(fundo, (0, 0))
        tela.blit(disco, (disco_x, disco_y))
        tela.blit(batedor_dir, (batedor_dir_x, batedor_dir_y))
        tela.blit(batedor_esq, (batedor_esq_x, batedor_esq_y))
        
    else:
        tela.blit(fim, (0, 0))
        pygame.display.update()
        vel_x = vel_y = velocidade_x = velocidade_y = 0
        fimjogo = titulo_font.render(str(placar), True, (255, 128, 0))
        fimjogo2 = titulo_font.render(str(placar2), True, (255, 128, 0))
        tela.blit(fimjogo, (400, 500))
        tela.blit(fimjogo2, (560, 500))








        # RETORNO DO DISCO

    if disco_x >= 930 and disco_y <= 160:
        velocidade_x = -velocidade_x
        hit2.play()





    if disco_x >= 930 and disco_y >= 375:
        velocidade_x = -velocidade_x
        hit2.play()


    if disco_x <= 5 and disco_y <= 160:
        velocidade_x = -velocidade_x
        hit2.play()


    if disco_x <= 5 and disco_y >= 375:
        velocidade_x = -velocidade_x
        hit2.play()


    if disco_y == 150 and disco_x <= 60:
        velocidade_x = - velocidade_x
        hit2.play()

    if disco_y == 150 and disco_x >= 870:
        velocidade_x = - velocidade_x
        hit2.play()

    if disco_y == 430 and disco_x >= 870 or disco_y == 400 and disco_x >= 870:
        velocidade_x = - velocidade_x
        hit2.play()

    if disco_y == 430 and disco_x <= 60 or disco_y == 400 and disco_x <= 60:
        velocidade_x = - velocidade_x
        hit2.play()
        disco = disco2

    else:
        disco = discobat
# MOVIMENTO DO DISCO

    disco_x -= velocidade_x
    disco_y += velocidade_y

    if disco_y >= altTela - 90 or disco_y <= 20:
        velocidade_y = -velocidade_y
        hit2.play()

#MUDANÇAS DE DISCO
    if disco_x <= 25 or disco_x >= 910:
        disco = disco2

    else:
        disco = discobat

    if disco_y <= 35 or disco_y >= 530:
        disco = disco2

    else:
        disco = discobat

        if abs(batedor_dir_y - disco_y) < 100 and abs(batedor_dir_x - disco_x) < 100:
            disco = disco2

        else:
            disco = discobat

            if abs(batedor_esq_y - disco_y) < 100 and abs(batedor_esq_x - disco_x) < 100:
                disco = disco2

            else:
                disco = discobat












    # GOOOOL
    if disco_x > 980:
        gol.play()
        disco_x = 450
        disco_y = 250
        velocidade_x, velocidade_y = 0, 0
        placar += 1

    if disco_x == 450 and disco_y == 250:
        text = fonte_gool.render('GOOOL!!!', True, (255, 215, 0))
        tela.blit(text, (350, 400))

    # GOOOOL
    if disco_x < -10:
        gol.play()
        disco_x = 450
        disco_y = 250
        velocidade_x, velocidade_y = 0, 0
        placar2 += 1

    if velocidade_x == 0 and keys[pygame.K_SPACE]:
        velocidade_x = -8
        velocidade_y = -6

    if velocidade_x == 0 and keys[pygame.K_SPACE]:
        velocidade_x = 8
        velocidade_y = 6
    # PLACAR

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pygame.display.update()

#PLACAR / TEMPO DO JOGO
    pygame.draw.rect(fundo, (39, 54, 66), [30, altTela - 615, 155, 45])
    sec = (tempo -pygame.time.get_ticks()) // 1000+10
    text2 = fonte_tempo.render("Tempo: "+str(sec), True, branco)
    fundo.blit(text2, (40, 40))

   






