## Multi-token prediction

`Multi-token prediction `refers to the task of predicting more than one token at a time in language models, instead of just the next single token. Here's a breakdown:

## 🔹 In Standard Language Models

Language models like GPT typically do next-token prediction:

Given a sequence: "The cat sat on the", the model predicts the next token (e.g., "mat").

## 🔹 What is Multi-Token Prediction?

Instead of predicting just one token, the model tries to predict multiple tokens at once.

`For example:`
`Input:` "The cat sat on the"
`Goal:` Predict: "mat and purred"

This involves predicting:

`"mat"`

`"and"`

`"purred"`
...all in a `single forward pass`, either:

`Autoregressively` (predicting tokens one-by-one but in a loop), or

`In parallel` (predicting all tokens at once, used in training sometimes).

## 🔹 Use Cases

- `Training Efficiency:` During training, models often use multi-token prediction to speed up learning (e.g., using teacher forcing).

- `Sequence-to-Sequence tasks:` Like translation or summarization, where the entire output sequence is predicted.

- `Masked Language Modeling (MLM):` Predicts multiple masked tokens in a sequence (e.g., in BERT).

