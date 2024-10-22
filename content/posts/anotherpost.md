---
title: "Control or Convenience? Lessons from Implementing Vision-Language Models"
date: 2024-10-16T12:00:00Z
draft: false
---

Date: October 16, 2024

Introduction: This blog captures the learning journey of implementing vision-language models, exploring trade-offs between convenience and control, and documenting the practical steps involved.

Caption: "Control or Convenience? Lessons from Implementing Vision-Language Models"

Key Takeaways:

Quick Wins for Learning:

Start with tangible projects to quickly gain experience with new models.

Image captioning with Llama 3.2 Vision Instruct is a great entry project to understand vision-language integration.

API vs. Local Model Deployment:

API Approach: Easy, fast setup with minimal control; ideal for prototyping.

Local Model Deployment: Requires infrastructure management but offers full control and cost efficiency for larger workloads.

Control vs. Convenience:

Use APIs for simple, fast use-cases.

Deploy locally for complex, customizable, or experimental projects that need advanced models.

Project Plan for Quick Tangible Output:

Build an image captioning app using Llama 3.2 Vision Instruct.

Follow structured steps: image preprocessing, model loading, generating captions, and UI integration.

Learning Curve Strategy:

Start small (single image captioning) and expand to advanced features (multi-image captioning).

Iteratively increase complexity to deepen understanding.

Note on AWS Setup:

The AWS setup for running Meta's Llama 3.2 Vision Instruct model involves creating an account, launching a GPU-supported EC2 instance, configuring storage, and managing dependencies. This provides full control but requires careful infrastructure management, like resizing storage and installing necessary packages.

Next Step: Ready to kickstart your own image captioning project? Focus on quick wins and iterate for deeper insights!

Date: October 17, 2024

Introduction: The challenges of selecting and configuring the right infrastructure for large AI models are part of the learning process. Today, it was all about recalibrating expectations, dealing with resource limitations, and adapting to practical constraints.

Caption: "A Day of Reevaluation: Matching Model Ambitions to Infrastructure Realities"

Key Takeaways:

Model Compatibility Frustrations:

Attempted to initialize the LLaMA-3.2-11B model, but hit memory limits on the g4dn.xlarge instance.

Learned that selecting the right infrastructure is key, especially when handling large models that require significant GPU memory.

Server Instance Challenges:

Faced delays when stopping and restarting the AWS server, leading to confusion about limits and resource requirements.

Realized the importance of matching the instance type (memory and GPU) to the model requirements.

Pivoting to a Smaller Model:

Decided to switch to a smaller 1B version of the LLaMA model to align with current infrastructure capacity.

The journey included reapplying for model access, dealing with download and setup instructions, and adapting to unexpected issues with hosting platforms.

Relying on Tools Can Be Both a Blessing and a Burden:

Relied heavily on copilot tools like Cursor and GPT for syntax and setup guidance, which provided helpful suggestions but also added challenges in diagnosing complex issues.

Taking a Step Back:

Decided to take a step back and reflect on the journey so far, evaluating the reasons behind each technical decision and understanding their impact on the overall process. Reflection helps reinforce learning and ensures a clearer direction moving forward.

Next Step: Now that the 1B model is downloaded and infrastructure requirements have been recalibrated, the focus will shift to getting the model up and running to start the actual project work. Keep adapting and moving forward!

Date: October 18, 2024

Caption: "The Art of Stepping Back: Reflecting on Complexity Before Moving Forward"

Key Takeaways:

Decision to Reflect:

Realized the need to take a step back to evaluate the entire setup process and its complexities.

Reflection helps in understanding the impact of each decision and reinforces learning.

Balancing Progress with Understanding:

Instead of blindly pushing forward, it's important to assess the reasons behind each technical change.

Techniques like quantization, LoRA, and gradient checkpointing were effective, but understanding why they work is crucial for future success.

Prioritizing Next Steps:

Complete One Cycle of Fine-Tuning: Let the fine-tuning process finish to evaluate the model’s performance and observe how all the techniques come together.

Experiment with Data Size: Reduce data size to speed up iteration and learn the fine-tuning process effectively before scaling up.

Analyze Training Speed: Training time has increased from 10s to 15s per iteration. Understanding the reasons for this change is essential for efficiency.

Evaluate Early Stops: Implement early stopping or reduce the number of epochs to obtain a checkpoint model for quicker evaluation.

Understand the Techniques: Take time to understand the individual impact of each technique (quantization, LoRA, etc.) on memory, speed, and accuracy.

Next Step: Reflecting on the process so far has highlighted areas for optimization. The focus will now be on completing a full training cycle and understanding the impact of each optimization technique. Keep learning, adapting, and moving forward!
