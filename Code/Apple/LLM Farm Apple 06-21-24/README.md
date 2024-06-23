## [Preceding Generative AI Study](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/tree/main/Code/Generative%20AI%20Live)

Current study: The Hugging Face 4 bit model was downloaded to three devices and inferenced using the LLM Farm app utilizing Apple Metal with the following Prompt: What is the structure of adenine?

Speed: <br>
iPhone 15 Pro 8GB: 2.47 tokens/sec <br>
iPad Pro M4 16GB: 6.59 tokens/sec <br> 
MacBook Pro M3 Max 48GB: 42.19 tokens/sec <br>
 
Accuracy: <br>
iPad > MacBook > iPhone to answer C5H5N5, and additional context. <br>

Generations were performed on-device without internet connection. Speeds measured were indicative of running a 4.92GB LLM with Compute and RAM configurations for each respective device. Future models will focus on limiting overall parameters while being a better expert in more specific tasks to increase speed and decrease model size for broad software implementation. This study marks the first time for the company that a custom large language model was implemented across a range of devices, which currently has close to 4,000 downloads. 
Large Language Model on [Hugging Face](https://huggingface.co/kevinkawchak/gradientai-Llama-3-8B-Instruct-Gradient-1048k-Molecule-q4-k-m-GGUF).
