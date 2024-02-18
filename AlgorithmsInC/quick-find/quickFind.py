N = 10000

def main():
    id = [i for i in range(N)]

    while True:
        try:
            p, q = map(int, input().split())
        except EOFError:
            break
        
        if id[p] == id[q]:
            continue

        t = id[p]
        for i in range(N):
            if id[i] == t:
                id[i] = id[q]
        
        print("\n", p, q)

if __name__ == "__main__":
    main()