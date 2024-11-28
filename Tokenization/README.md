`Tokenization` is the process of breaking down text into smaller units, called tokens, which can be words, subwords, characters, or other meaningful chunks. Tokenization is a foundational step in Natural Language Processing (NLP) tasks, enabling models to process and analyze text efficiently.

## Types of Tokenization
`Word Tokenization`
- Splits text into individual words based on spaces and punctuation.

`Example:`
Input: "Natural Language Processing is amazing!"
Tokens: ["Natural", "Language", "Processing", "is", "amazing", "!"]

## Subword Tokenization
- Breaks words into smaller units to handle rare or unknown words better.

- Techniques include `Byte Pair Encoding (BPE)`, `WordPiece`, and `Unigram`.

`Example:`

Input: "unbelievable"
Tokens: ["un", "##believ", "##able"] (using WordPiece, common in models like BERT)

## Character Tokenization
- Treats each character as a token.

`Example:`
Input: "AI"
Tokens: ["A", "I"]
## Sentence Tokenization
- Splits text into sentences. Common in tasks requiring sentence-level understanding.

`Example:`
Input: "I love NLP. It's fascinating!"
Tokens: ["I love NLP.", "It's fascinating!"]
