 # **Sparse Mixture of Experts (MoE)**

This repository implements a Sparse Mixture of Experts (MoE) layer using PyTorch. The design includes top-k gating, load balancing, and optional noisy routing to dynamically route tokens to the most relevant experts in a transformer architecture.

### **🔍 What is Mixture of Experts?**

Mixture of Experts is a technique where, for a given input, only a subset of a larger set of expert networks are activated. This enables:

- Efficient computation (sparse activation).

- Scalability to large models.

- Dynamic selection of expert pathways.

`🧱 Architecture Overview`

The Mixture of Experts Module consists of the following core components:

- `Experts` — Each expert is a simple feedforward neural network (FFN) with:

- `Expansion layer` (increased hidden size),

- `ReLU activation`

- `Contraction layer` (back to embedding size),

- `Dropout layer`.

### `Router`  

A gating network that decides which tokens are routed to which experts based on the output of the attention block. There are two types:

- `Top-k Router`

- `Noisy Top-k Router`

### `Expert Selector Matrix` 

 Logits computed by multiplying input tokens with a learned routing matrix. Used to select top-k experts per token.

### `Load Balancing & Softmax` 

 Ensures only the top-k expert logits are used (others set to -inf), followed by softmax to get the weight distribution.

### `Sparse Aggregation `
 Final output is a weighted sum of outputs from selected experts for each token.

## **🚀 Key Components and Flow**

### **STPE 1 : Expert Definition**

Each expert is a simple feedforward neural network defined as:
```
expansion -> ReLU -> contraction -> Dropout
```

### **STEP 2 : Routing**

The **Router** determines which expert each token should go to:

- Input to the router: Output of the attention layer (tokens × embedding).

- The router multiplies this input with a **routing matrix** to generate **expert logits**.

- Apply **Top-k selection** per token to keep only the most relevant experts.

- Replace unselected logits with -inf and apply **softmax** for weight normalization.

```
logits = input @ routing_matrix
topk_logits, topk_indices = logits.topk(k=top_k, dim=-1)
```

### **Step 3: Noisy Top-k Routing (Optional)**

To encourage expert diversity and load balancing, Gaussian noise is added to the logits before selecting the top-k experts.

```
noisy_logits = logits + torch.randn_like(logits) * noise_std
```

### ***Step 4: Expert Selection and Weighted Sum**

For each token:

- Identify top-k experts.

- Fetch output from selected experts.

- Multiply expert output by corresponding weights.

- Aggregate to get final output.

- Efficient batching is achieved by looping over experts (not tokens), ensuring better GPU parallelism.

## **📦 How to Use**

```
# Create the router and mixture of experts module
router = NoisyTopKRouter(embed_dim=8, num_experts=3, top_k=2)
moe_layer = SparseMoE(embed_dim=8, num_experts=3, top_k=2, dropout=0.1)

# Forward pass through router
selector_weights = router(input_tensor)

# Forward pass through MoE
output = moe_layer(input_tensor, selector_weights)

```