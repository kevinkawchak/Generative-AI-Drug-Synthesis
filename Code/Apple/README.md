### [Download](https://drive.google.com/file/d/1E3sVgJ4cbhulpWvq_FO0pqgZkwhnMtLu/view?usp=sharing), [Results](https://drive.google.com/file/d/1s0imJ0zidk5-hraT46y8u4jnUby_oukk/view?usp=sharing), [Discussion](https://www.youtube.com/watch?v=PFOk-qJ9nr0&t=2s). WWDC June 10.

## 5 Guiding Principles for Apple On-Device Generative AI:
Guiding Principle #1: Workflow: MacBook Pro for training and finetuning models, iPad and iPhone for inferencing and RAG. <br>
Guiding Principle #2: Optimized generative AI LMM/LLM size, and Dataset size are top considerations for efficient usage. <br>
Guiding Principle #3: Random access memory RAM, Tokens per second, and Generation quality are key areas for developers. <br>
Guiding Principle #4: iPhone: Inference model size doesn’t exceed ¼ of device RAM. iPad, MacBook with higher RAM are more flexible. <br>
Guiding Principle #5: Apple’s own Generative AI for inferencing may be more efficient and always available due to iOS ‘Wired RAM’. <br>

Large Multimodal Models, LMMs, and LLMs developed by MacBook Pro for inferencing under two gigabytes in final size would likely run effectively on a variety of iOS devices. This can be done be focusing software parameters on contexts more applicable to mobile devices, instead of high proficiency in scores related to public internet data achieved by today’s larger models. 

MacOS and iOS have been utilized with a variety of lead optimization applications for drug discovery such as visualizing and analyzing Generative AI results, or complex simulations and virtual screening. Here, three sets of inference tests for iPhone 15 Pro 8GB, iPad Pro M4 16GB, and MacBook Pro M3 Max 48GB were conducted with the following findings 1) iPad Pro was fastest in iOS app environment, 2) Prompting with Ollama in MacOS Terminal saw generations at nearly 50 token/sec, but with minor RAM utilization, and was 10-15X faster than the reference Core i7-1255U 16GB, 3) MacBook Pro utilization of GPT4All using Apple Metal and two local RAG documents saw the highest generation rate of 59 tokens/sec, with negligible RAM and CPU impact, and was 14X faster than the Core i7-1255U. <br>

June 6th 2024 <br>
Kevin Kawchak
