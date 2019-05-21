def mutate_string(string, position, character):
    x=int(i)
    s1=s[x]
    s1=c
    s_new=s[:x]+c+s[x+1:]
    
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
