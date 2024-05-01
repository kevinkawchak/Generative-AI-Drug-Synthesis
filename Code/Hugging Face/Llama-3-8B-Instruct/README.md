## The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work. Built with Meta Llama 3.
[Cover Image](https://drive.google.com/file/d/1lYHv7r_2CxuT4DQjd-3lkKfNZiJi_SDk/view?usp=sharing) <br>

The Meta-Llama-3-8B-Instruct Large Language Model was fine-tuned using the alpaca-cleaned dataset and varying LoRA values. LoRA experiments were run to affect model size and performance, with the top model being uploaded to Hugging Face as a 'Text generation' model: kevinkawchak/Meta-Llama-3-8B-Instruct-LoRA-R1. (a) 

Open-source Llama 3 8 Billion parameter model was released April 18, 2024, and it's selection was based on several highly functional existing Llama 2 Medical applications, an increase in Llama 3 downloads by developers, and Meta's growing infrastructure to support Llama improvements. (b-e)

Low-Rank Adaptation, also known as LoRA, makes fine-tuning LLMs easier by reducing the number of trainable parameters to produce lightweight and efficient models. LoRA was utilized by modifying matrix rank 'r' and alpha values. Run times were similar between experiments, however loss tended to favor lower values of rank, which corresponded to smaller model sizes. The most effective 'R1' model mentioned above was trained on a rank of 1 and alpha of 5, which performed better by loss than a rank of up to 5. Further testing of the model uploaded to Hugging Face is relevant to determine what benefits the finetuning has over the base Llama 3 8B Instruct model. (f) 

A recent Unsloth Llama 3 Colab Notebook, a Llama 3 discussion, and clarifications from Hugging Chat and ChatGPT allowed for the completion of the finetuned of the model using an NVIDIA 40GB A100. The remainder of the notebook experiments are avaialable on GitHub. (g-i)

The yahma/alpaca-cleaned dataset used is an update to resolve issues regarding the original 2023 Stanford alpaca instruction dataset. Text generations answering several questions were of high quality and comparable to other leading GenAI platforms. Answers to the following questions are available on GitHub notebooks such as 'What is a famous university in San Francisco bay area?', and 'What are the DNA bases?' (j) A look ahead at datasets for Drug Discovery Generative AI will be covered on Thursday 04/25/2024. 

a) https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-LoRA-R1 <br>
b) https://ollama.com/library/medllama2 <br>
c) https://github.com/AIAnytime/Llama2-Medical-Chatbot <br>
d) https://github.com/entbappy/End-to-end-Medical-Chatbot-using-Llama2 <br>
e) https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/ <br>
f) https://snorkel.ai/lora-low-rank-adaptation-for-llms/ <br>
g) https://colab.research.google.com/drive/1mPw6P52cERr93w3CMBiJjocdTnyPiKTX#scrollTo=6bZsfBuZDeCL <br>
h) https://www.youtube.com/watch?v=aQmoog_s8HE&t=1s <br>
i) https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/tree/main/Code/Hugging%20Face/Llama-3-8B-Instruct <br>
j) https://huggingface.co/datasets/yahma/alpaca-cleaned <br>
<br>
[META LLAMA 3 COMMUNITY LICENSE AGREEMENT](https://llama.meta.com/llama3/license/) <br>
