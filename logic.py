import random
import time
import emoji
# ⋯⋯⋯⋯⋯ Main Code ⋯⋯⋯⋯⋯ #

# Password Generator
def gen_pass(pass_length):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=~`"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

# Coin Flip
def flip_coin():
    time.sleep(1)  # Simulate the time taken to flip a coin
    return random.choice(["Heads", "Tails"])

# Emoji Generator
emojis = list(emoji.EMOJI_DATA.keys())

def gen_emoji():
    return random.choice(emojis)
