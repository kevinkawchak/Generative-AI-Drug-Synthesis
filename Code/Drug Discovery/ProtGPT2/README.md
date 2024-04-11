The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work.

# Protein Generator II:
A second protein generator has been further developed based on a Hugging Face nferruz/ProtGPT2 example of generating de novo proteins in an unsupervised 'zero-shot' fashion. Development of the generator was also assisted with ChatGPT3.5 coding prompts. The ProtGPT2 model was trained on the protein database UniRef50 - which allowed for the patterns of internal representations of proteins to be learned. 

Here, the upgraded protein generator was set to generate 10 different protein sequences of max length 300 using Phenylaline as the first amino acid. A perplexity difference was calculated between two of the sequences, which determined how much a sequence with lower perplexity was favored. In addition, a sequence identity score was calculated to determine amino acid overlap at every position when aligned. Future studies will focus on further fine-tuning models such as ProtGPT2, and modifying open-source GPT architectures with tensor networks to accelerate cancer drug discovery efficiency.  

References:
1) [Hugging Face](https://huggingface.co/nferruz/ProtGPT2) 
2) [ChatGPT3.5](https://chat.openai.com/)
3) [Hayes, J.](https://medium.com/labs-notebook/large-language-models-for-drug-discovery-7ddfc005e0bb)

# Protein Generator:
A protein generator has been further developed based on a Hayes, J. Hugging Face ProtGPT2 text-generation pipeline with assistance from an AssemblyAI tutorial and ChatGPT3.5 prompts. 

References:
1) [Hayes, J.](https://medium.com/labs-notebook/large-language-models-for-drug-discovery-7ddfc005e0bb) 
2) [AssemblyAI](https://www.youtube.com/watch?v=QEaBAZQCtwE&t=4s) 
3) [ChatGPT3.5](https://chat.openai.com/)
