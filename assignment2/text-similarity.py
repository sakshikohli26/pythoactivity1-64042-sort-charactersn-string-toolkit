
def text_similarity_score(text1, text2):
    # Convert text into lowercase unique words
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    # Handle two empty strings
    if not words1 and not words2:
        return 1.0

    # Find common and total unique words
    common_words = words1 & words2
    all_words = words1 | words2

    # Return Jaccard similarity score
    return len(common_words) / len(all_words)
