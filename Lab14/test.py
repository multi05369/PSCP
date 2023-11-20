import random

# Generate a random OTP with 4, 6, or 8 digits
for _ in range(10):
    otp_length = random.choice([4, 6, 8])
    otp = ''.join(random.choice('0123456789') for _ in range(otp_length))
    print(otp)