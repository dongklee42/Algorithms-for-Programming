# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    t_queue = deque(truck_weights)
    b_queue = deque([0] * bridge_length)
    b_queue[-1] = t_queue.popleft()
    answer = 1
    while t_queue:
        if sum(b_queue) - b_queue[0] + t_queue[0] > weight:
            b_queue.popleft()
            b_queue.append(0)
            answer += 1
        else:
            b_queue.popleft()
            b_queue.append(t_queue.popleft())
            answer += 1
    answer += bridge_length
    return answer
