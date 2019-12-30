import queue

def bfs(graph,start):
    visit = {}
    q = queue.Queue()
    q.put(start)
    
    #q가 존재할때
    while q.qsize()>0:
        node = q.get()
        # 만약 현재 노드의 방문 기록이 없다면 추가
        if node not in visit:
            visit[node]=True
        
        # 해당 노드의 인접 노드 큐에 추가
        for x in graph[node]:
            if x not in visit:
                q.put(x)            
        
    ans=[x for x in visit]

    return ans



    




graph={0 : [1,2,3,4] , 
1 : [0,2,4], 
2 : [0,1,3], 
3 : [0,2], 
4 : [0,1]
}

print(bfs(graph,0))
