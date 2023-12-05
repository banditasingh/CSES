n = int(input())
events = []

for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, 1))  
    events.append((b, -1))  

events.sort()

max_customers = 0
current_customers = 0

for _, event_type in events:
    current_customers += event_type
    max_customers = max(max_customers, current_customers)

print(max_customers)
