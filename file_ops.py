from pathlib import Path


def count_vowels_concise(text: str) -> int:
    """
    Counts vowels using a list comprehension and the sum() function.
    """
    vowels = {"a", "e", "i", "o", "u"}

    # The inner generator expression returns 1 for every vowel found,
    # and sum() adds them up.
    return sum(1 for char in text.casefold() if char in vowels)


def ispalindrome(s: str) -> bool:
    """
    Returns True if s is a palindrome, ignoring case and non-alphanumerics.
    """
    t = "".join(ch.casefold() for ch in s if ch.isalnum())
    return t == t[::-1]


def main() -> None:
    msg = "Programming is an enjoyable and powerful skill."
    names_list = ["Rouhollah", "Ehsan", "Negar", "Khalil", "Sina"]

    # Print the message in reverse order
    print(msg[::-1])

    # Count vowels in message
    count = count_vowels_concise(msg)
    print(f"Vowel Count: {count}")  # Output: 14

    # Palindrome check
    print(f"Is palindrome? {ispalindrome(msg)}")

    # Ensure ./files exists, then write
    path = Path("files") / "names.txt"
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write list names to names.txt
    try:
        with path.open("w", encoding="utf-8") as file:
            for name in names_list:
                file.write(f"{name}\n")

        with path.open("r", encoding="utf-8") as file:
            print(file.read().upper())

    except OSError as e:
        # Covers FileNotFoundError, PermissionError, etc.
        print(f"fFile error: {e}")

    finally:
        print("Operation complete!")


if __name__ == "__main__":
    main()
