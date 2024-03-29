import random
import time
import json
def load_leaderboard():
    try:
        with open("leaderboard.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def show_leaderboard():
    leaderboard = load_leaderboard()

    print("\nLeaderboard:")
    for i, entry in enumerate(leaderboard, start=1):
        print(f"{i}. {entry['username']}: {entry['wpm']} WPM")
def save_leaderboard(leaderboard):
    with open("leaderboard.json", 'w') as file:
        json.dump(leaderboard, file, indent=2)
def choose_words(category):
    categories_words = {
        "animals": ["dog", "cat", "elephant", "giraffe", "lion", "tiger", "zebra", "penguin", "kangaroo", "koala"],
        "fruits": ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "strawberry", "mango", "pineapple", "peach"],
        "countries": ["USA", "Canada", "Japan", "India", "Brazil", "Australia", "Germany", "France", "Italy", "China"],
      "Colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"],
      "Vegetables": ["carrot", "broccoli", "spinach", "potato", "tomato", "cucumber", "bell pepper", "onion", "garlic", "celery"],
      "Sports": ["football", "basketball", "soccer", "tennis", "golf", "baseball", "volleyball", "hockey", "swimming", "cycling"],
      "Movies": ["action", "comedy", "drama", "horror", "sci-fi", "romance", "thriller", "fantasy", "animation", "documentary"],
      "Technology": ["computer", "software", "internet", "keyboard", "mouse", "smartphone", "tablet", "laptop", "algorithm", "programming"],
      "Musical Instruments": ["piano", "guitar", "violin", "trumpet", "drums", "flute", "saxophone", "clarinet", "bass guitar", "accordion"],
      "Planets": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "sun"],
      "Weather": ["rain", "sunshine", "clouds", "wind", "storm", "snow", "hail", "fog", "thunder", "lightning"],
      "Clothing": ["shirt", "pants", "dress", "jacket", "shoes", "hat", "socks", "gloves", "scarf", "tie"],
      "Insects": ["ant", "bee", "butterfly", "dragonfly", "mosquito", "spider", "ladybug", "grasshopper", "beetle", "caterpillar"]
    }

    return categories_words.get(category, [])
def main():
    print("Welcome to Terminal Typing Master!")
    username = input("Enter your username: ")

    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")
        if choice == "1":
          category = input("Choose a typing category (animals, fruits, countries, Colors, Vegetables, Sports, Movies, Technology, Musical Instruments, Planets, Weather, Clothing, Insects): ")
          words = choose_words(category)

          if not words:
              print(f"Error: Words for category {category} not found.")
              continue
          input("Get ready! Press Enter to start typing.")
          start_time = time.time()

          print(" ".join(words)) 

          user_input = input("Type the words exactly as shown. Press Enter to finish: ")

          if user_input.lower() == 'ctrl+q':
              print("Exiting the typing test.")
              break

          if user_input.split() == words:
              end_time = time.time()
              time_taken = end_time - start_time

              words_typed = len(user_input.split())
              wpm = int((words_typed / time_taken) * 60)

              print(f"\nWords Typed: {words_typed}")
              print(f"Time Taken: {time_taken:.2f} seconds")
              print(f"Words Per Minute: {wpm} WPM")
              leaderboard = load_leaderboard()
              leaderboard.append({"username": username, "wpm": wpm})
              leaderboard = sorted(leaderboard, key=lambda x: x["wpm"], reverse=True)[:10]
              save_leaderboard(leaderboard)
          else:
              print("Incorrect! Please type the words exactly as shown.")
        elif choice == "2":
            show_leaderboard()
        
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()