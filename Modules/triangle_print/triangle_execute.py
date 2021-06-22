"""
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
"""

from triangle_print.line  import print_line


def print_the_triangle(n):
    # [print_line(1, x) for x in range(n)]
    for x in range(n):
        print_line(1, x + 1)
    for x in range(n-1, 0, -1):
        print_line(1, x)

