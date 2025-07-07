# 📚 Penguin Book Title Trend Analyzer

This script scans upcoming Penguin book titles and analyzes word usage to detect trending topics and phrases in publishing.

## 🔍 How It Works
- Reads a CSV containing book titles (e.g. scraped from a publisher's coming soon page)
- Cleans and tokenizes each title into unique lowercase words
- Tracks word frequency and maps each word to the titles it appears in
- Outputs a CSV report showing how often each word appears and in which titles

## 🧰 Tech Stack
- Python
- pandas
- Regular expressions (`re`)
- `collections.defaultdict`

## 📁 Input
CSV file with a column named `Title`.

## 📤 Output
CSV with columns:
- `word`: the lowercase keyword
- `count`: number of unique titles containing it
- `titles`: semicolon-separated list of titles where the word appears

## 🚀 Use Cases
- Trend detection in book publishing or marketing
- Editorial planning for emerging themes
- Text analysis in titles, headlines, or social content

---
