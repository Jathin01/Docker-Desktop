import os
import socket
import re
from collections import Counter

# Define file paths
input_files = ["/home/data/IF-1.txt", "/home/data/AlwaysRememberUsThisWay-1.txt"]
output_file = "/home/data/output/result.txt"

def read_file(filepath):
    """ Read file and return words as a list, handling contractions. """
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        text = re.sub(r"’", "'", text)  # Normalize apostrophes
        words = re.findall(r"\b\w+(?:'\w+)?\b", text)
        return words

# Read files and process word counts
word_counts = {}
total_words = 0

for file in input_files:
    words = read_file(file)
    word_counts[file] = len(words)
    total_words += len(words)

# Get top 3 most frequent words in IF-1.txt
freq_words_if = Counter(read_file("/home/data/IF-1.txt")).most_common(3)

# Handle contractions and get top 3 words in AlwaysRememberUsThisWay-1.txt
words_arutw = [word for word in read_file("/home/data/AlwaysRememberUsThisWay-1.txt")]
freq_words_arutw = Counter(words_arutw).most_common(3)

# Get machine IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"Total words in IF-1.txt: {word_counts['/home/data/IF-1.txt']}\n")
    f.write(f"Total words in AlwaysRememberUsThisWay-1.txt: {word_counts['/home/data/AlwaysRememberUsThisWay-1.txt']}\n")
    f.write(f"Grand total words: {total_words}\n")
    f.write(f"Top 3 words in IF-1.txt: {freq_words_if}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {freq_words_arutw}\n")
    f.write(f"Machine IP Address: {ip_address}\n")

# Print result file contents to console
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())
