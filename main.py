import pygame
pygame.init()
import time


window_size = (800, 600) # Размеры окна в виде картежа
screen = pygame.display.set_mode(window_size) # Переменная куда сохранили окно
pygame.display.set_caption("Тестовый проект") # Заголовок окна

image = pygame.image.load("picPython.png") # Это все модули пайгейм
image_rect = image.get_rect() # Берем рамку и сохраняем в переменную

image2 = pygame.image.load("pycharm.png")
image_rect2 = image2.get_rect()


# speed = 5 # Скорость с которой картинка проходит при нажатии опред клавиши


run = True # Игровой цикл

while run: # Цикл вайл будет работать пока переменная ран будет тру
    for event in pygame.event.get(): # Ивент - события, гет - получить,
# каждое отдельное событие сохраняется в переменную ивент,
# а пайгейм.ивент.гет - как бы список всех событии
        if event.type == pygame.QUIT: # Окно закрывается при нажатии на крестик
            run = False # Наш цикл прекращает работу
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 40
            image_rect.y = mouseY - 40
# Это управление изображением мышкой, вместо клавиш управления, для этого надо
# удалить speed = 5 и функцию if для клавиш, которая ниже и добавить if выше с #

#   👇отступ как у for
#   keys = pygame.key.get_pressed() # Сохраняем в переменную клавишу которую нажимаем
#   if keys[pygame.K_LEFT]: # Нажимаем на левую кнопку - это условие нажали ли мы на левую кнопку
#       image_rect.x -= speed # Берем рамку изображения, будем двигать в лево
#   if keys[pygame.K_RIGHT]:
#       image_rect.x += speed
#   if keys[pygame.K_UP]:
#       image_rect.y -= speed
#   if keys[pygame.K_DOWN]:
#       image_rect.y += speed
# ❗️❗️❗️Сейчас управлением клавишами с #, а управлением мышкой включено

    if image_rect.colliderect(image_rect2): # Условие функции, при столкновении изображении выйдет надпись ниже
        print("Произошло столкновение")
        time.sleep(1) # Импортировали выше и теперь при столкновении выходит всего 1 надпись выше


    screen.fill((0, 0, 0)) # Цвет окна
    screen.blit(image, image_rect) # Отрисовка и делаем это после цвета окна
    screen.blit(image2, image_rect2)



    pygame.display.flip() # Обновлять содержимое нашего окна

pygame.quit() # В самом конце нашей программы мы используем это
