n = int(input())
luggage = []

luggage = list(map(int, input().split()))

m = int(input())



for _ in range(m):
    high= luggage.index(max(luggage))
    low = luggage.index(min(luggage))
    luggage[high] -= 1
    luggage[low] += 1

high= luggage.index(max(luggage))
low = luggage.index(min(luggage))
print(luggage[high] - luggage[low])
