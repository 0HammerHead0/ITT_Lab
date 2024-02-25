import re

def find_replace_string(input_text, pattern, replacement):
    result = re.sub(pattern, replacement, input_text)
    return result

# Example usage:
original_text = "This is an example string with some pattern."
pattern_to_replace = r'\bexample\b'
replacement_text = "replacement"
modified_text = find_replace_string(original_text, pattern_to_replace, replacement_text)

print("Original Text:", original_text)
print("Modified Text:", modified_text)
