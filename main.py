import tkinter as tk
import math

black = "#000000"
pink = "#FFD1DC"
white = "#FFFFFF"

# Настройки анимации
width, height = 800, 800
figure_type = "heart" # "circle" или "heart"
animation_speed = 2
scale = 20

def heart_function(t):
    """Параметрическое уравнение сердца"""
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

def circle_function(t):
    """Параметрическое уравнение круга"""
    x = 15 * math.cos(t)
    y = 15 * math.sin(t)
    return x, y

def create_figure_points(scale, width, height, figure_type="heart"):
    """Создает точки для рисования фигуры"""
    points = []
    steps = 628  # 2π * 100

    for i in range(0, steps, 2):
        t = i / 100
        # t изменяется от 0 до 2π с шагом 0.02

        if figure_type == "heart":
            x, y = heart_function(t)
            points.append((x * scale + width // 2, -y * scale + height // 2))

        elif figure_type == "circle":
            x, y = circle_function(t)
            points.append((x * scale + width // 2, y * scale + height // 2))

    return points

def create_animation():
    """Создает и настраивает анимацию"""
    # Создание главного окна
    root = tk.Tk()
    root.title("Анимированная фигура")
    root.geometry(f"{width}x{height}")

    # Создание холста
    canvas = tk.Canvas(root, width=width, height=height, bg=black)
    canvas.pack()

    # Создание точек фигуры
    points = create_figure_points(scale, width, height, figure_type)
    current_point = 0

    def draw_animation():
        """Функция для отрисовки анимации фигуры."""
        nonlocal current_point

        canvas.delete("all")

        # Рисование заполненной части фигуры
        if current_point > 2:
            fill_points = points[:current_point]
            canvas.create_polygon(fill_points, fill=pink, outline="")

        # Рисование контура
        if current_point > 1:
            for i in range(current_point - 1):
                if i < len(points) - 1:
                    x1, y1 = points[i]
                    x2, y2 = points[i + 1]
                    canvas.create_line(x1, y1, x2, y2, fill=white, width=3)

        if current_point < len(points):
            current_point += animation_speed
            root.after(10, draw_animation)

    draw_animation()
    return root

create_animation().mainloop()