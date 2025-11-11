# 🐍 Professional Python Program:
# Demonstrating re.search() and re.match() with Explanation
# ---------------------------------------------------------
# Author: Christian Jason Ranison
# Description:
#   This program demonstrates the difference between re.search() and re.match()
#   using a user-input word and a fixed example string.
#
#   🔹 re.search() → Searches for a pattern anywhere in the string.
#   🔹 re.match()  → Checks only if the pattern matches at the beginning of the string.

import re


def main():
    # Step 1: Define the base string to test
    text = "Python is a powerful programming language."
    print("🔹 Original String:", text)

    # Step 2: Take user input
    word = input("\nEnter a word to test: ")

    # Step 3: Escape any special regex characters in the word
    pattern = re.escape(word)

    # Step 4: Search for the word anywhere (case-insensitive)
    search_result = re.search(pattern, text, re.IGNORECASE)

    # Step 5: Match only at the start of the string (case-insensitive)
    match_result = re.match(pattern, text, re.IGNORECASE)

    # Step 6: Display Search Result
    print("\n🔍 --- Search Result (re.search) ---")
    if search_result:
        print(
            f"✅ Word '{word}' found in the string at position {search_result.start()}.")
    else:
        print(f"❌ Word '{word}' not found anywhere in the string.")

    # Step 7: Display Match Result
    print("\n🎯 --- Match Result (re.match) ---")
    if match_result:
        print(f"✅ The string starts with '{word}'.")
    else:
        print(f"❌ The string does not start with '{word}'.")

    # Step 8: Clear summary explanation
    print("\n📘 Summary:")
    print("• re.search() scans the entire string to find a match.")
    print("• re.match() checks only the beginning of the string.")
    print("• Example →")
    print("   - If input = 'Python' → both search & match succeed.")
    print("   - If input = 'powerful' → only re.search() succeeds.\n")


# Step 9: Execute main
if __name__ == "__main__":
    main()
