import random

def main():
    print("Tossing a coin...")

    heads_count = 0
    tails_count = 0

    for i in range(1, 4):
        result = random.choice(["Heads", "Tails"])
        print(f"Round {i}: {result}")
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print(f"Heads: {heads_count}, Tails: {tails_count}")

if __name__ == "__main__":
    main()
