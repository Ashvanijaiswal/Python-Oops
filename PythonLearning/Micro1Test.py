k = 2
notifications = [("user1", 'Hello', 1), ("user1", 'Hello', 2), ("user2", 'Hi', 3), ("user1", 'Hello', 4)]
hs = {}
res = []
for notification in notifications:
    if (hs.get(notification[0]+notification[1]) == None or notification[2] > k):
        hs[notification[0]+notification[1]] = notification[2]
        res.append(notification)

print(res)