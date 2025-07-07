import pandas as pd
import re
from collections import defaultdict

# Load CSV
df = pd.read_csv("penguin_coming_soon_with_category-06-09-2025-07-08-AM.csv")  # Replace with your file path

# Drop rows with no Title
df = df.dropna(subset=['Title']).copy()
df['Title'] = df['Title'].astype(str)

# Prepare data structures
word_to_titles = defaultdict(list)
word_counts = defaultdict(int)

# Process each Title row
for title in df['Title']:
    # Find words in title (lowercase)
    words_in_title = set(re.findall(r'\b\w+\b', title.lower()))
    
    for word in words_in_title:
        word_counts[word] += 1
        word_to_titles[word].append(title)

# Prepare list of rows for output
output_rows = []
for word, count in word_counts.items():
    concatenated_titles = ";".join(word_to_titles[word])
    output_rows.append({'word': word, 'count': count, 'titles': concatenated_titles})

# Create DataFrame and save CSV
output_df = pd.DataFrame(output_rows)
output_df = output_df.sort_values(by='count', ascending=False)
output_df.to_csv("word_counts_with_titles_PENGUIN_COMING_SOON.csv", index=False)

print("Output saved to word_counts_with_titles_PENGUIN_COMING_SOON.csv")
