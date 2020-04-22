import sys

from Fifteen import solve

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print('Bledne argsy')
        exit(1)
    else:
        solve(sys.argv[1:6])
        exit(0)
