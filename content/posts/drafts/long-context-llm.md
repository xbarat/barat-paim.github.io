# long context llm - explained in short answers

1. What is Long Context LLM?
Long Context LLM is a type of LLM that can handle longer sequences of text. Imagine AIs that can read a book, listen to a long podcast, attend a long meeting, or seminar. Anything longer than a few pages, paragraphs, or minutes.

2. What is the difference between Long Context LLM and other LLMs?
The main difference is the context window. The size is usually between 4k to 128k tokens. Imagine 4k as a few pages, and 128k as a few books. In podcast, imagein 4k as a few minutes, and 128k as a few hours. The modes can differ, reading or listening which essentially means text or audio, it can be video or speech, or images. In unknown use cases, it can be things we have not discovered yet, like smell, taste, or touch. Other than the senses, it can be also be other things like code, or even 3D objects. Understanding the entire codebase of a large project, or the entire internet are vast use cases that require long context LLMs. Imagine the internet as a book, how much context window do you think that would be? Yes, it could go in the billion of tokens.

As of now we have reached the limit of 128k tokens (a few books, or a few hours of podcast). The next frontier is to go beyond that. We do have 1 million tokens, but it is not yet available for public use. These are the current state of the art models.

3. How does it work?
We are yet to see an OSS model that works well on long context benchmarks beyond a simple needle search. This means that the performance of the current long context LLMs are only at par with the retrieval models. 


4. What is fp16 model?
The fp16 model is a 16-bit floating-point model, which is a more efficient model than the fp32 model. It is more efficient because it uses less memory and can run faster.
In simple words, 16-bit stores half the information of 32-bit but can do the same calculations. The technology is called quantization. Quantization is a technique used to reduce the precision of the model weights, which helps in reducing the memory usage and increasing the speed of the model. The precision is reduced by taking the mean of the weights, and the difference is stored in a smaller precision. It is the modern lossless compression technique, which does not lose any information and therefore the model performs the same as the fp32 model. Then why not use 16-bit always? The problem is that the model might not converge if we use 16-bit. So, we use a mix of 16-bit and 32-bit. The weights are stored in 16-bit, but the gradients are stored in 32-bit. This way we get the best of both worlds.

