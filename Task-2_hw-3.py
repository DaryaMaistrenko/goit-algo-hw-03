import turtle
import argparse

def draw_koch_segment(length, depth):
    """
    Малює один сегмент кривої Коха.
    :param length: Довжина лінії.
    :param depth: Поточний рівень рекурсії.
    """
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(length, depth-1)
        turtle.left(60)
        draw_koch_segment(length, depth-1)
        turtle.right(120)
        draw_koch_segment(length, depth-1)
        turtle.left(60)
        draw_koch_segment(length, depth-1)

def draw_koch_snowflake(length, depth):
    """
    Малює сніжинку Коха з трьох сегментів.
    :param length: Довжина кожного сегмента.
    :param depth: Рівень рекурсії.
    """
    for _ in range(3):
        draw_koch_segment(length, depth)
        turtle.right(120)

def main():
    # Парсинг аргументів для вказання рівня рекурсії
    parser = argparse.ArgumentParser(description='Малює фрактал "сніжинка Коха".')
    parser.add_argument('depth', type=int, help='Рівень рекурсії для сніжинки Коха')

    args = parser.parse_args()

    # Налаштування екрану Turtle
    turtle.speed(0)  # Максимальна швидкість
    turtle.penup()
    turtle.goto(-200, 100)  # Початкове положення черепашки
    turtle.pendown()

    # Викликаємо функцію для малювання сніжинки Коха
    draw_koch_snowflake(400, args.depth)

    # Завершення
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

