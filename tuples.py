if __name__ == '__main__':
    n = int(input())
    x=map(int,input().split())
    print(hash(tuple(x)))
