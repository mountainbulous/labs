from sys import argv


def get_arg(number: int, text: str) -> float:
    try:
        coefficient = float(argv[number])
    except IndexError:
        while True:
            try:
                coefficient = float(input(f"Введите {text}: "))
            except ValueError:
                print("Введено недействительное число!")
            else:
                break
    return coefficient


def get_root(a: float, b: float, c: float) -> list[float]:
    if a == 0.0:
        if b == 0.0:
            return []
        else:
            return [-1*c/b]
    roots = []
    d = b * b - 4.0 * a * c
    print(f"Дискриминант: {d}")
    if d == 0:
        root = -b / (2.0 * a)
        if root > 0:
            roots.append(root ** 0.5)
            roots.append(-(root ** 0.5))
        elif root == 0:
            roots.append(0)
    elif d > 0:
        root1 = (-b + d ** 0.5) / (2.0 * a)
        root2 = (-b - d ** 0.5) / (2.0 * a)
        if root1 > 0:
            roots.append(root1 ** 0.5)
            roots.append(-(root1 ** 0.5))
        elif root1 == 0:
            roots.append(root1)
        if root2 > 0:
            roots.append(root2 ** 0.5)
            roots.append(-(root2 ** 0.5))
        elif root2 == 0:
            roots.append(abs(root2))
    return sorted(roots)


def print_roots(result: list[float]) -> None:
    if len(result) == 0:
        print("Корней нет!")
    elif len(result) == 1:
        print(f"Корень: {result[0]}")
    else:
        print(f"Корни: {' '.join([str(i) for i in result])}")


def main() -> None:
    a = get_arg(1, "A")
    b = get_arg(2, "B")
    c = get_arg(3, "C")
    result = get_root(a, b, c)
    print_roots(result)


if __name__ == "__main__":
    main()
