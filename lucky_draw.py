import random

def pick_lucky_winners():
    # List of names
    names = [
        "Alice", "Bob", "Charlie", "David", "Eve", 
        "Frank", "Grace", "Heidi", "Ivan", "Judy",
        "Mallory", "Niaj", "Olivia", "Peggy", "Sybil"
    ]
    
    print("--- Lucky Draw System ---")
    print(f"Total Participants: {len(names)}")
    
    # Randomly pick 5 unique winners
    winners = random.sample(names, 5)
    
    print("\n🎉 The 5 Lucky Winners are:")
    for i, winner in enumerate(winners, 1):
        print(f"{i}. {winner}")

if __name__ == "__main__":
    pick_lucky_winners()
