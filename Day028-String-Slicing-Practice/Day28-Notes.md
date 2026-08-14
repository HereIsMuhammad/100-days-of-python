# Day 28: String Slicing Practice

String slicing allows us to extract a specific part of a string using indexes.

## Syntax
string[start : end]

- start → index where slicing begins (included)
- end → index where slicing stops (excluded)

## Key Points
- Indexing starts from 0
- Negative indexes work from the end
- Empty start or end means full range

## Examples
- text[0:4] → first 4 characters
- text[2:] → from index 2 to end
- text[:5] → from start to index 5
- text[-4:] → last 4 characters
