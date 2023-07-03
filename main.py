from faker import Faker
import random
import string

def generate_fake_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_fake_email():
    fake = Faker()
    email = fake.email()
    return email

# Example usage:
password = generate_fake_password()
email = generate_fake_email()

print("Fake Password:", password)
print("Fake Email:", email)
