## Speed-ups for State of the Art Generative AI Drug Discovery Applications | [PDF Download](https://drive.google.com/file/d/1fTYONxzpO0FW_EHJX5LzbgxlNAAs8sok/view?usp=sharing)

Here, (2) 2024 Generative AI reviews for drug discovery and molecular design were summarized. This was followed by a 2024 paper featuring a transcriptional signatures generator variational autoencoder for a pancreatic cancer application. The authors’ model was found to be faster than several others tested.

Hugging Face pipeline experiments were run several times as a rapid GenAI screening tool. In specific, over 30 pipelines were combined from several internet sources into a single Python notebook as a fast way to conceptualize types of advanced machine learning inference methods.

A Llama.cpp, TensorRT, and LibTorch table depicts the ways to use C++ and other techniques to improve the speed of Generative AI inference times, shown on slide 14.

Four LLMs were compared using the Groq Cloud inference engine, with responses judged by ChatGPT 4o, and Gemini.google. Inference times were fast, with llama3-8b generations close to 1000 tokens/second, followed by gemma-7b-it, mixtral-8x7b, and llama3-70b being last at a very good 413 tokens/second. The two judges were not made aware of which model created each generation - and preferred gemma > llama3-70b > mixtral-8x7b > llama3-8b. ChatGPT 4o provided the most detailed responses of the two judges. Notebook and results are on [GitHub](https://github.com/kevinkawchak/Generative-AI-Drug-Discovery/tree/main/Code/Groq). [Discussion](https://www.youtube.com/watch?v=UR3dxk-H4tM). 03Jul24, Kevin Kawchak. <br>
