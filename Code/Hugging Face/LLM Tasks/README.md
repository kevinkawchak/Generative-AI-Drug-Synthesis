Large Language Models (LLMs) serve as multi-functional software platforms that can process a wide range of input types for Generative AI tasks. In specific, LLMs developed by the community serve as foundations for the next generation of Medical AI. Industry leader Hugging Face developed high-level objects built on top of pre-trained models referred to as 'Pipelines" for fast and simple inferencing to solve Natural Language Processing (NLP) tasks. [01-02]

Here, sentiment analysis, summarization, and text generation tasks were performed using LLMs of different architectures and sizes that were originally trained on datasets with different content. 30 experiments were executed using Pipelines to determine the highest performing leading plug and play LLMs using fixed statements.

Sentiment analysis using 10 different Hugging Face LLMs with statements "Large Language Models are really awesome!" and "Medical Generative AI is very practical!". The Top 3 Positive, Positive statement results are as follows:
1) distilbert/distilbert-base-uncased-finetuned-sst-2-english = 99.9868%, 99.8504%
2) RecordedFuture/Swedish-Sentiment-Fear = 99.8911%, 99.8686%
3) siebert/sentiment-roberta-large-english = 99.8494%, 99.8578%

Summarization using 10 different Hugging Face models, many being LLMs, of the statement "Medical Generative AI is very practical!" are available in Supplementary. The Top 3 summary results are as follows:
1) SyedShaheer/bart-large-cnn-samsum_tuned = Highest accuracy and insight
2) sshleifer/distilbart-cnn-12-6 = High accuracy and insight, but promotional
3) google/pegasus-xsum = Direct and accurate, but lacked additional detail

Generative AI using 10 different Hugging Face LLMs of a "Medical Generative AI is very".. sentence fragment, with Generations available in Supplementary. The Top 3 results are as follows: 
1) openai-community/gpt2-large = Medical GenAI learns from experience, adapts to environment
2) openai-community/gpt2-xl = Medical GenAI is very much a work in progress
3) alpindale/Mistral-7B-v0.2-hf = Medical GenAI is very much in early stages of development
A ChatGPT3.5 03/31/24 query reflected the early stages of the technology, and detailed 6 areas of active Medical GenAI research - being trained on more recent data than test GPTs.

The 30 experiments were conducted using a single High-RAM CPU, with the majority of time spent loading models, especially text generation models. Insight gained from the studies will be used to develop next generation tensor network generative AI applications based on customer demands using EHRs, medical images, or speech input data. 
 
References: <br>
[01] Pipelines: https://huggingface.co/docs/transformers/en/main_classes/pipelines <br>
[02] Pipelines tutorial: https://www.youtube.com/watch?v=ntz160EnWIc <br>
