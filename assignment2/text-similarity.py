def text_similarity_score(text1, text2):
    # Convert both strings to lowercase and split them into words.
    # Use sets to keep only unique words.
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    # If both strings contain no words, return 1.0.
    if not words1 and not words2:
        return 1.0

    # Find the words common to both strings.
    common_words = words1.intersection(words2)

    # Find all unique words present in either string.
    all_words = words1.union(words2)

    # Calculate Jaccard similarity.
    # Similarity = Common words / Total unique words.
    similarity_score = len(common_words) / len(all_words)

    # Return the similarity score between 0 and 1.
    return similarity_score


# Test Case 1: Both strings are identical.
print(text_similarity_score("hello world", "hello world"))
# Expected output: 1.0

# Test Case 2: One word is common between the strings.
print(text_similarity_score("hello world", "hello python"))
# Expected output: 0.3333333333333333

# Test Case 3: No words are common.
print(text_similarity_score("hello", "python"))
# Expected output: 0.0

# Test Case 4: Both strings are empty.
print(text_similarity_score("", ""))
# Expected output: 1.0

# Test Case 5: Words differ only in letter case.
print(text_similarity_score("Hello World", "hello world"))
# Expected output: 1.0

