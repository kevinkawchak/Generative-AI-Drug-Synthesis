## FOR IMMEDIATE RELEASE | [PDF Download](https://drive.google.com/file/d/1jAfDg9pQ_O1N5GKcGxtgv409mf8xDhF8/view?usp=sharing)


### Extra Large Language Models Benchmarking for Medicinal Chemistry

Purpose: 
Determine which unmodified Extra Large Language Model has the greatest speed and generation quality answering medicinal chemistry prompts.

Plan: 
Use OpenAI API for GPT 4o, and NVIDIA NIM API for Nemotron 4, Mixtral, and Arctic. To judge generations, use ChatGPT 4o and Llama 3 70B Groq.

Experimental: 
In a Colab notebook for either OpenAI API or NIM API, answer 10 medicinal chemistry prompts. Manually process all generations, and further analyze the first three prompts three times each with both judges. 

Key Takeaways <br>
1) Nemotron 4 had the most consistent high quality generations as tested by two different judges. <br>
2) Mixtral was the fastest XLLM tested by nearly 2x, and had the best balance of speed and quality. <br>
3) GPT 4o provide detailed and hypothetical solutions, but was less specific than Nemotron 4 or Mixtral. <br>
4) Arctic did not have high quality generations to synthetic chemistry prompts, but is economical for use. <br>
5) The improved triplicate judging method for each single generation was consistent for several prompts tested. <br>
6) The 1024 context window for each XLLM did not approach the generation limit, as experienced in prior findings. <br>
7) Myriad possibilities to further improve generation scores for each model exist by adding RAG and Agentic Workflows. <br>

July 18, 2024
