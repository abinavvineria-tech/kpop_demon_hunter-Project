#!/usr/bin/env python3

def rate_kpop_demon_hunters():
    print("🌟 K-POP DEMON HUNTERS EXPERIENCE RATER 🌟")
    print("=" * 50)
    
    # Input box for personal experience description
    print("📝 Describe Your Experience")
    print("-" * 30)
    experience = input("Please share your experience watching K-pop Demon Hunters: \n👉 ")
    
    # Input box for star rating
    print("\n⭐ Star Rating")
    print("-" * 15)
    while True:
        try:
            stars = int(input("Rate the show (1-5 stars): "))
            if 1 <= stars <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Display results
    print("\n" + "=" * 50)
    print("📊 YOUR RATING SUMMARY")
    print("=" * 50)
    print(f"Experience: {experience}")
    print(f"Rating: {'⭐' * stars} ({stars}/5 stars)")
    print("=" * 50)
    
    # Save to file option
    save = input("\nWould you like to save this rating to a file? (y/n): ").lower()
    if save == 'y':
        with open("kpop_demon_hunters_rating.txt", "w", encoding="utf-8") as f:
            f.write("K-POP DEMON HUNTERS EXPERIENCE RATING\n")
            f.write("=" * 40 + "\n")
            f.write(f"Experience: {experience}\n")
            f.write(f"Rating: {'⭐' * stars} ({stars}/5 stars)\n")
            f.write("=" * 40 + "\n")
        print("✅ Rating saved to 'kpop_demon_hunters_rating.txt'")

if __name__ == "__main__":
    rate_kpop_demon_hunters()

