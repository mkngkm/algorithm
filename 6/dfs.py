def DFS(v):
    if v>7:
        return 
    else:
        print(v, end="") ##전위순회
        DFS(v*2)
        ##print(v) 중위순회
        DFS(v*2 + 1)
        ##print(v) 후위순회

if __name__ == "__main__":
    DFS(1)