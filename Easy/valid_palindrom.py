
def is_palindrome(s: str) -> bool:
    # Process the string to remove non-alphanumeric characters and convert to lowercase
    processed_str = ''.join(char for char in s if char.isalnum()).lower()

    # Check if the processed string reads the same forward and backward
    for i in range(len(processed_str) // 2):
        if processed_str[i] != processed_str[-i - 1]:  # Corrected index for the counterpart
            return False
    return True  # Moved outside of the loop

if __name__ == "__main__":
    print(is_palindrome("race a car"))