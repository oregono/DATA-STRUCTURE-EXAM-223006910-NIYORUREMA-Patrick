def quick_sort(events, low, high):
    if low < high:
        pi = partition(events, low, high)
        quick_sort(events, low, pi - 1)
        quick_sort(events, pi + 1, high)

def partition(events, low, high):
    pivot = events[high]['tickets']
    i = low - 1
    for j in range(low, high):
        if events[j]['tickets'] < pivot: 
            i += 1
            events[i], events[j] = events[j], events[i]
    events[i + 1], events[high] = events[high], events[i + 1]
    return i + 1

events = [
    {"name": "New groove concert", "tickets": 200, "date": "2025-03-01", "venue": "Amahoro Stadium"},
    {"name": "HIPOP show", "tickets": 80, "date": "2025-02-20", "venue": "Downtown Club"},
    {"name": "Buttle ceremony", "tickets": 100, "date": "2025-01-15", "venue": "Bk Arena"},
    {"name": "Mtn Iwacu Music", "tickets": 150, "date": "2025-02-10", "venue": "Huye Stadium"}
]

quick_sort(events, 0, len(events) - 1)

print("Sorted Events by Ticket Availability:")
for event in events:
    print(f"Event: {event['name']}, Tickets: {event['tickets']}, Date: {event['date']}, Venue: {event['venue']}")
