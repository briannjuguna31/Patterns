from abc import ABC, abstractmethod


# Abstract interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Concrete implementations
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Client code
def make_animal_speak(animal):
    print(animal.speak())


# Usage
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!

# -----------------------------------------------



class NotificationChannel(ABC):
    @abstractmethod
    def send_message(self, message):
        pass


class EmailChannel(NotificationChannel):
    def send_message(self, message):
        print(f"Sending email: {message}")


class SMSChannel(NotificationChannel):
    def send_message(self, message):
        print(f"Sending SMS: {message}")


class NotificationService:
    def __init__(self, channel):
        self.channel = channel

    def send_notification(self, message):
        self.channel.send_message(message)


email_channel = EmailChannel()
sms_channel = SMSChannel()

notification_service = NotificationService(email_channel)
notification_service.send_notification("Hello, via email")

notification_service = NotificationService(sms_channel)
notification_service.send_notification("Hello, via SMS")
