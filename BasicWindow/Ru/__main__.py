# импорт модуля
import pygame

# Желаемые размеры окна
WIDTH = 800
HEIGHT = 600

def main():
    # Инициализация фреймворка pygame
    pygame.init()
    # Создат окно размера WIDTHxHEIGHT с двойной буферизацией
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

    # Флаг, сигнализирующий, пришло ли уже время закрывать приложение
    quit_game = False
    # Основной цикл приложения
    while not quit_game:
        # Получение первого событие из очереди
        event = pygame.event.poll()
        # Пока очередь не пуста выполняется обработка событий
        while event.type != pygame.NOEVENT:
            # Если получен тип события "Выход", то флаг выхода выставляется в True
            if event.type == pygame.QUIT:
                quit_game = True
            # Получение следующего событие из очереди
            event = pygame.event.poll()

        # Очистка экрана приложения (просто заливка цветом)
        screen.fill(pygame.Color('black'))
        # -------------------
        # Здесь будет распологаться весь код, производящий отрисовку 
        # -------------------
        # Переключает буфер
        pygame.display.flip()

    # Финализация фреймворка pygame
    pygame.quit()

main()
