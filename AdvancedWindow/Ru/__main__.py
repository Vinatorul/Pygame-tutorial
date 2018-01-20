import pygame

WIDTH = 800
HEIGHT = 600

def main():
    pygame.init()
    # Загрузка системного шрифта Courier
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    # Установка заголовка окна
    pygame.display.set_caption("Привет, pygame")
    # Инициализация часов pygame
    clock = pygame.time.Clock()

    quit_game = False
    while not quit_game:
        # Установка верхней границы FPS
        clock.tick(60)
        event = pygame.event.poll()
        while event.type != pygame.NOEVENT:
            if event.type == pygame.QUIT:
                quit_game = True
            # Если получен тип события "Клавиша нажата", то проверяется, что за клавиша была нажата
            elif event.type == pygame.KEYDOWN:
                # Если была нажата клавиша q
                if event.key == pygame.K_q:
                    # То приложение ставит себе в очередь событие "Выход" 
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                # Если была нажата клавиша Пробел
                elif event.key == pygame.K_SPACE:
                    # То происходит инвертирование захвата ввода
                    pygame.event.set_grab(not pygame.event.get_grab())
            event = pygame.event.poll()

        screen.fill(pygame.Color('black'))
        # В переменную fps_text сохраняется уже отрендренный текст (другими словами  изображение текста)
        # (255, 255, 255) - цвет текста в формате (R, G, B)
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, (255, 255, 255))
        # Текст выводится на экран в точке (10, 10)
        screen.blit(fps_text, (10, 10))
        # В переменную quit_text сохраняется отрендренная подсказка о том, как выйти из приложения
        quit_text = my_font.render("Нажмите Q для выхода", True, (255, 255, 255))        
        # Текст выводится на экран в точке (10, 30)
        screen.blit(quit_text, (10, 30))
        # Производится проверка, активирован ли режим захвата
        if pygame.event.get_grab():
            grab_text = my_font.render("Нажмите Пробел для выхода из режима захвата", True, (255, 255, 255))       
        else:
            grab_text = my_font.render("Нажмите Пробел для активации режима захвата", True, (255, 255, 255))
        # Текст выводится примерно в середине экрана
        screen.blit(grab_text, (WIDTH/2 - 170, HEIGHT/2 - 15))

        pygame.display.flip()

    pygame.quit()

main()
