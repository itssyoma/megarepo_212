#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func_show(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
    return wrapper


@func_show
def get_sq(width, height):
    return width * height


if __name__ == "__main__":
    get_sq(5, 10)
