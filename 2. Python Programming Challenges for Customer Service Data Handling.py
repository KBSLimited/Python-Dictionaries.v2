service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(customer, issue):
    ticket_id = f"Ticket{len(service_tickets) + 1:03}"
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"Opened new ticket {ticket_id} for {customer}: {issue}")

def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Updated status of ticket {ticket_id} to {new_status}")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(status=None):
    tickets = service_tickets if not status else {ticket_id: info for ticket_id, info in service_tickets.items() if info["Status"] == status}
    print(f"Tickets{' with status ' + status if status else ''}:")
    for ticket_id, ticket_info in tickets.items():
        print(f"{ticket_id}: Customer {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

# Example usage:
open_ticket("Eve", "Website down")
open_ticket("Charlie", "Product inquiry")
update_ticket_status("Ticket001", "closed")
display_tickets()
display_tickets("open")
