import queue


#bfs 구현
def bfs(graph,start):
    visit = {}
    q = queue.Queue()
    q.put(start)
    
    #q가 존재할때
    while q.qsize()>0:
        node = q.get()
        # 만약 현재 노드의 방문 기록이 없다면 추가
        if visit.get(node) == None:
            visit[node]=True
        
        # 해당 노드의 인접 노드 큐에 추가
        for x in graph[node]:
            if visit.get(x) == None:
                q.put(x) 

        
    ans=[x for x in visit]

    return ans


def dfs(graph,start):
    visit = {}
    s = [start]


    #s가 존재할때
    while s:
        node = s.pop()
        if visit.get(node) == None:
            visit[node]=True
        
        for x in graph[node]:
            if visit.get(x) == None:
                s.append(x)
        

    ans = [x for x in visit]

    return ans