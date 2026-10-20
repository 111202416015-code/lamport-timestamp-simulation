class Process:

  def __init__(self, process_id):
    self.id = process_id
    self.clock = 0

  def internal_event(self, event_name):
    self.clock += 1
    print(
        f"[Process {self.id}] Event '{event_name}' terjadi. Clock:"
        f" {self.clock}"
    )

  def send_message(self, receiver, message_name):
    self.clock += 1
    timestamp = self.clock
    print(
        f"[Process {self.id}] Mengirim '{message_name}' ke Process"
        f" {receiver.id} dengan Timestamp: {timestamp}"
    )
    receiver.receive_message(self.id, message_name, timestamp)

  def receive_message(self, sender_id, message_name, received_timestamp):
    self.clock = max(self.clock, received_timestamp) + 1
    print(
        f"[Process {self.id}] Menerima '{message_name}' dari Process"
        f" {sender_id}. Clock diperbarui menjadi: {self.clock}"
    )


# Simulasi 3 Proses
p1 = Process(1)
p2 = Process(2)
p3 = Process(3)

print("--- Awal Simulasi Lamport Timestamps ---")
p1.internal_event("a1")  # Event internal P1
p1.send_message(p2, "m1")  # P1 kirim m1 ke P2
p3.internal_event("c1")  # Event internal P3
p2.send_message(p3, "m2")  # P2 kirim m2 ke P3
print("--- Simulasi Selesai ---")