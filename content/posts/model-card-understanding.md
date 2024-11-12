# Model Card Understanding
The goal of this exercise is to understand how to read and understand a model card.

## Model Card for LLama 3.2 1B


Model Information:
The Llama 3.2 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction-tuned generative models in 1B and 3B sizes (text in/text out). The Llama 3.2 instruction-tuned text only models are optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks. They outperform many of the available open source and closed chat models on common industry benchmarks.

STUDY:
what is instruction-tuned? the instruction is the prompt that the model is trained on.
why is it instruction-tuned text only? it is limited to text. it is limited to instruction following - like chatbots. the user gives an instruction and the model follows it. for instance, if the user says "write a poem about a cat", the model will follow the instruction and write a poem about a cat. more like master-slave relationship. thus the properties:
    properties:
    1. the model will not understand the intent of the user. it will only follow
    2. the model will perform the task based on the instruction.
    3. the model is trained similar to the master-slave relationship, however, not necessarily in a brutal manner. the model enacts a friendly relationship with the user.
    4. if the instruction is to question the user's intent, the model will try to understand the user's intent with enough context.
    5. the model is optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks.

how dialogue use cases are trained?
it is trained on a dataset of dialogues. the dataset is usually mentioned in the model card.

the agentic retrieval means that the model is trained to retrieve information from the database. is it programmatically trained to search or does it retrieve information from the training dataset?

Model Architecture:
Llama 3.2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety.

Llama 3.2 (text only) uses a new mix of publicly available online data. 1B. Multilingual. 128k context length.
Llama 3.2 Quantized: 1B. Multilingual. 8k context length.
Llama 3.2: 3B. Multilingual.

STUDY:
what is auto-regressive language model? it is a type of language model that generates text one token at a time, using the previously generated tokens as context.
what is transformer architecture? the older form of it is RNN where it addresseed the issue of vanishing gradient (which is the learning rate of the model it slows down as it goes deeper, it forgets the previous context), but the self attention mechanism allows the model to attend to all positions in the input sequence. 

the SFT and RLHF are the types of training. SFT is supervised fine-tuning where the model is trained on a dataset of dialogues. RLHF is reinforcement learning with human feedback where the model is trained on a dataset of dialogues with human feedback.

context length is the number of tokens that the model can attend to. 128k means that the model can attend to 128,000 tokens. for instance, it can attend to 128,000 tokens in the input sequence. you mean the prompt? the prompt size is 128k tokens, which is a whole lot of tokens. as big as a book. what do you mean by attend to? it can follow the instruction of the user with that many tokens. doesn't mean you can ask multiple questions. it means the model can follow the instruction of the user with that many tokens. can there be a context length of 128k tokens? yes, but it is not mentioned in the model card.

what is the difference between 1B and 3B? 1B is 1 billion parameters. 3B is 3 billion parameters. the bigger the model, the more powerful it is.
    it can be set 1B or 3B while training, number of weights they initialize. you can thus define the size of the model. you can even set it to 10B or 100B as long as you have the computational power. the computational power can be GPUs. FLOPS is the number of operations per second. If it is 70B model, it can do 70B operations per second. 

How to estimate the size based on the computational power?
    if you have 100 GPUs, you can train a 1B model. if you have 1000 GPUs, you can train a 3B model. The formula is: FLOPS * hours = number of parameters. 
    The formula for FLOPS is: FLOPS = 2 * #layers * #heads * hidden_size^2 / 3e9
    The formula for hours is: hours = number of parameters / (FLOPS * number of GPUs)
    For Heuristics, you can remember that 1B model is 100M FLOPS, and 100M FLOPS takes 1 hour to train on 100 GPUs

    For instance A100 GPU has 312 TFLOPS. Which means it can do 312 trillion operations per second, which means it can train a 1B model in 1 hour on 100 GPUs. How many GPUs does A100 have? 80. 

    How to read the GPU?
    A100 has 80 GPUs.
    H100 has 192 GPUs.
    T4 has 1536 GPUs.
    Tesla V100 has 128 GPUs.
    
    Why is H100 powerful than T4? Because it has more GPUs. But T4 has 1536 GPUs? Isn't that 10 times more than H100? Th

   what can you do with 4 GPUs?
   you can train a 1B model in 1 hour. No, that is not true.
   If you want to learn more about GPUs, you can read this: https://developer.apple.com/metal/tensorflow-plugin/

what is multilingual? the model can understand and generate text in multiple languages.

how to use?
Use with transformers
Starting with transformers >= 4.43.0 onward, you can run conversational inference using the Transformers pipeline abstraction or by leveraging the Auto classes with the generate() function.

Make sure to update your transformers installation via pip install --upgrade transformers.

import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B"

pipe = pipeline(
    "text-generation", 
    model=model_id, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

pipe("The key to life is")

Use with llama
Please, follow the instructions in the repository.

To download Original checkpoints, see the example command below leveraging huggingface-cli:

huggingface-cli download meta-llama/Llama-3.2-1B --include "original/*" --local-dir Llama-3.2-1B

STUDY:
huggingface-cli is a command-line tool for interacting with the Hugging Face platform. It allows you to download, upload, and manage datasets, models, and other resources.

llama is a command-line tool for interacting with the Llama platform. It allows you to download, upload, and manage datasets, models, and other resources.

how do you execute the command?
    you can execute the command in the terminal.

TRaining Data
raining Data
Overview: Llama 3.2 was pretrained on up to 9 trillion tokens of data from publicly available sources. For the 1B and 3B Llama 3.2 models, we incorporated logits from the Llama 3.1 8B and 70B models into the pretraining stage of the model development, where outputs (logits) from these larger models were used as token-level targets. Knowledge distillation was used after pruning to recover performance. In post-training we used a similar recipe as Llama 3.1 and produced final chat models by doing several rounds of alignment on top of the pre-trained model. Each round involved Supervised Fine-Tuning (SFT), Rejection Sampling (RS), and Direct Preference Optimization (DPO).

Data Freshness: The pretraining data has a cutoff of December 2023.

STUDY:
Is 9 trillion tokens of data structured? No, it is not structured. It is a whole lot of data from publicly available sources.

When they say 9 trillion tokens, they mean the data that the model is trained on.
Everybody says that, and if you haven't understood what that means. let me explain it to you.

Lets say a book is 1 million tokens. Then 9 million books are 9 trillion tokens.
The model is therefore trained on 9 million books of data.
Lets say the books were exclusively about history. Then the model is trained on history.

You may be wondered if the model read 9 million books. In a way, it did. There are different kind of training that can be done with the 9 million books. Lets explore that for now.
1. you split the 9 million books into first story and second story, and train the model to predict the second story based on the first story. That is called supervised fine-tuning.
2. or, you don't give an