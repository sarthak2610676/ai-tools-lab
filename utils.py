def is_palindrome(s):
    """Return True if s reads the same forwards and backwards."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_words(text):
    """Return the number of words in text."""
    return len(text.split())

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32
