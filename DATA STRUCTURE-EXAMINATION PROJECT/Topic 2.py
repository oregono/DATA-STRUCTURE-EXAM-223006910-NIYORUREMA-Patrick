import heapq


events = []


event_heap = []

def add_event(event_name, event_date, venue, tickets_available):
    
    event = {
        "name": event_name,
        "date": event_date,
        "venue": venue,
        "tickets": tickets_available
    }
    events.append(event)
    
    heapq.heappush(event_heap, (tickets_available, event_name, event_date, venue))
    print(f"Event '{event_name}' added successfully!")


def remove_event(event_name):
    global events, event_heap
    
    events = [event for event in events if event["name"] != event_name]
    
    event_heap = [(tickets, name, date, venue) for tickets, name, date, venue in event_heap if name != event_name]
    heapq.heapify(event_heap)
    print(f"Event '{event_name}' removed successfully!")


def search_event(event_name):
    for event in events:
        if event["name"] == event_name:
            return event
    return None

def display_events():
    print("All Events:")
    for event in events:
        print(f"Name: {event['name']}, Date: {event['date']}, Venue: {event['venue']}, Tickets: {event['tickets']}")

def get_event_with_least_tickets():
    if event_heap:
        tickets, name, date, venue = heapq.heappop(event_heap)
        print(f"Event with least tickets: {name}, Tickets: {tickets}, Date: {date}, Venue: {venue}")
        return tickets, name, date, venue
    else:
        print("No events available.")
        return None
    
add_event("New groove ceremony 2025", "2025-02-10", "City Arena", 150)
add_event("Worship concert", "2025-02-20", "Downtown Club", 80)
add_event("Fire Night club", "2025-03-01", "Stadium", 200)

display_events()
print()

get_event_with_least_tickets()
print()

remove_event("Jazz Night")
display_events()
