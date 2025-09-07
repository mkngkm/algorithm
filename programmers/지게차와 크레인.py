# 지게차와 크레인
# 알파벳 대문자로 컨테이너 구분
# storage	requests	result
# ["AZWQY", "CAABX", "BBDDA", "ACACA"]	["A", "BB", "A"]	11
# ["HAH", "HBH", "HHH", "HAH", "HBH"]	["C", "B", "B", "B", "B", "H"]	4


def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    for r in requests:
        if len(r) == 1: # 지게차
            storage = bfs(storage)
        else: # 크레인
            for s in range(n):
                for ss in range(m):
                    if storage[ss] == r[0]:
                        storage[ss] = '0' # 뽑은 컨테이너는 문자 0으로 변경

def bfs(storage):
    return storage
                        
            
    
    
    
    answer = 0
    return answer

# 지게차 로직 : 4면중 적어도 1면이 외부와 연결 - bfs
# 크레인 로직 : 상관 x 



if __name__=="__main__":
    storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
    requests = ["A", "BB", "A"]
    solution(storage, requests)
    