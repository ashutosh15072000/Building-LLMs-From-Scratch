### 🧠 `What Is Chain-of-Thought (CoT) Prompting?`

-- Chain-of-thought prompting is a technique where language models are guided to generate intermediate reasoning steps, much like how humans think step-by-step. Instead of just producing an answer, the model first explains its thinking process, then concludes

### `🔬 Key Findings`

- CoT prompting significantly improves performance on math word problems, commonsense reasoning, and symbolic logic tasks.

- It works especially well for large models (100B+ parameters).

- Even without finetuning, just giving a few reasoning examples as prompts helps models generalize better.

### 🔢 `Example Comparison: Standard vs. CoT Prompting`

`Standard Prompting:`

Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 balls. How many tennis balls does he have?
A: 11

`CoT Prompting:`

A: Roger starts with 5 balls.
Each can has 3 balls, and he buys 2 cans → 2 × 3 = 6
Now, 5 + 6 = 11
So, the answer is 11.

`⏫ Result: `The model is more likely to get it right when it reasons through the steps.

![alt text](<IMG/Screenshot 2025-04-15 200137.jpg>)


`⚙️ How It Works`

`Few-shot prompting:` You give a few examples like this:

Input → Chain-of-thought → Answer.

`Large model (≥100B):` Small models struggle, but big ones can mimic the reasoning style.

### 🔁 `Tasks Covered`

`1. Arithmetic Reasoning`

`Datasets:` GSM8K, SVAMP, ASDiv, MAWPS, AQuA.

`Task:` Multi-step math word problems.

`Example:`

Q: A concert was scheduled for 06/01/1943 but delayed by one day. What is the date 10 days ago from today?
A: One day after 06/01/1943 is 06/02/1943.
10 days before that is 05/23/1943. So the answer is 05/23/1943.

`2. Commonsense Reasoning`

`Datasets:` CSQA, StrategyQA, Date Understanding, Sports Understanding.

`Example:`

Q: Would a pear sink in water?
A: The density of a pear is ~0.6g/cm³, less than water’s. It would float. So the answer is no.

`3. Symbolic Reasoning`

`Tasks:` Letter concatenation, coin flipping.

`Example:`

Q: Last letters of “Lady Gaga”?
A: “y” from Lady, “a” from Gaga → "ya"

### `💡 Emergent Ability of Large Models`

- Only large models (100B+ parameters) truly benefit.

![alt text](<IMG/Screenshot 2025-04-15 201504.jpg>)

![alt text](<IMG/Screenshot 2025-04-15 201445.jpg>)

- Small models produce fluent but illogical chains.

- With scale, reasoning ability "emerges."

![alt text](<IMG/Screenshot 2025-04-15 201737.jpg>)

#### `🧠 Real World Use Case`
They also tried:

“How would you bring me something that isn’t a fruit?”
`The model reasons:`
“An energy bar isn’t a fruit → Bring it.”

`And outputs a robotic plan:`

- find(energy bar)

- pick(energy bar)

- find(user)

- put(energy bar)

### `🧩 Final Thoughts`

`Strengths:`

- Easy to implement (no training needed).

- Works across domains (math, logic, commonsense).

![alt text](<IMG/Screenshot 2025-04-15 201909.jpg>)

- Helps uncover how models think.

`Limitations:`

- Only works well for large models.

![alt text](<IMG/Screenshot 2025-04-15 202044.jpg>)

- CoT might be factually wrong even if the final answer is correct.

- Manual crafting of exemplars still required (though automation is possible).