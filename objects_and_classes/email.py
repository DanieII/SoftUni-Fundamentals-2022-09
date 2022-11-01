class Email:

    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()
while command != "Stop":
    names = command.split()
    current_sender, current_receiver, current_content = names
    email = Email(current_sender, current_receiver, current_content)
    emails.append(email)
    command = input()

indices = list(map(int, input().split(", ")))
# Setting the boolean to true for the given indexes of all emails
for index in indices:
    emails[index].send()
for current_email in emails:
    print(current_email.get_info())
