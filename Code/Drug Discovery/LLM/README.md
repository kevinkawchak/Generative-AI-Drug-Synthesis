## FOR IMMEDIATE RELEASE | [PDF Download](https://drive.google.com/file/d/14Rl9lQuEmRtJfhuWaRo8ezH6dMDNpfdN/view?usp=sharing)


### Large Language Models for Early Phase GenAI Drug Discovery

Large Language Model (LLM) performance for drug discovery applications has improved in 2024 with the release of models such as Llama 3 70B and GPT 4o. State of the art drug synthesis utility can be achieved today when appropriate prompts are submitted with proper LLM settings using an API or Chat framework. The barrier to entry for medicinal chemists to design effective drug synthesis has been improved, while also providing expert chemists with greater chemical natural language processing than prior AI technologies. These enhanced functionalities are achieved through convenient and effective conversational innovation between AI and humans, often resembling dialogue with traditional medical experts.

Here, 4 LLMs across multiple context window configurations generated answers to 10 prompts regarding drug discovery synthesis using GroqCloud API or OpenAI API. An additional LLM chemical agent from literature was also tested against the other models. Performance was measured primarily in speed by the number of tokens generated per second, and the output was judged by separate GroqCloud or ChatGPT 4o chat interfaces. The two AI judges were asked to rate each generation for proficiency based on the quality and detail of their original responses to each question on a scale from 1-10. Current model versions of Gemma, Gemini.google, Sonnet, and Meta.ai were not able to generate effective responses to a drug synthesis question.

Explainability of the LLM decision making process were aided by the first two cases: 
A) Multiple generations were conducted of the same prompt, and multiple 
    generations of the judges’ decisions were further analyzed. 
B) LangSmith for the LLM chemical agent provided stepwise AI processes of outputs
    times for each step, and approximate costs. 
C) Additional analysis to re-run or discard generations is an option; or else use different  
    search or machine learning models, if the specific output quality is low.

LLM products for real-time generative chemistry problems will likely include one or more:
           A) Retrieval Augmented Generation (RAG): Aids in supporting LLM generations with 
     references, which is valuable for real-time step-wise drug synthesis. 
B) Agentic Workflows: In combination with RAG to further incorporate other machine
     learning tasks, chemical databases, and code executors with LLMs. 
C) Text Model Assist: With user image uploads and downloads, speech, and video  
     clip interactions for troubleshooting challenging molecular design. 

A range of use cases with Large Language Models are imminent in drug discovery: from more specific reactants and reagents to heavily influencing building block selection. LLMs have become more adaptable to answering a broader range of questions. Other supporting LLM and machine learning learning technologies also have the potential to significantly improve the quality of drug candidates for specific diseases. 

A look ahead for drug discovery research and develpment with Large Language Models:
A) Pre-training or fine-tuning open source models on specific datasets will continue. 
B) Future production ready software deployment will require improved explainabilty. 
C) Different approaches are needed to further the explainability of synthetic steps. 
D) Example RAG workflow: Cite specific GPT 4o synthetic steps in greater detail. 
E) Generating interactions of chemical compounds on a higher level is needed. 
F) The transition to reliable large biomolecule generations will likely follow. 
G) Base model results illustrated here represent good out of the box performance.
H) Expect more generative applications addressing larger chemical spaces. 

Each experiment consists of an input prompt, or query; and an output generation: 
A) Tokens: Represent words, subwords, or characters, Basic units of input and output. 
B) Context Window: The maximum combined input and output tokens allowes.
C) Tokens/Second: Generation speed determined by model size and hardware.

Next Page: Experimental Details <br>
10 Prompts for Large Language Models <br>
01 Provide a better, faster, and less expensive method to synthesize Methotrexate.<br>
02 Using only H2, N2, O2, and CO2 - provide a synthesis to create high purity Paclitaxel, showing relevant chemical structures. <br>
03 Using only sucrose and N2 as reactants under mild conditions, create 10 cancer drug candidates. <br>
04 Using an environmentally friendly catalyst and starting materials that are available for expedited shipment from Sigma Aldrich or VWR Chemicals, design a cancer drug candidate. <br>
05 Design a new cancer drug candidate using a goal oriented approach based on SAR, predict their physical properties, and provide SMILES. <br>
06 Following Lipinski’s rule of five, create a top cancer drug suitable for scale up in a high-throughput self-driving lab. <br>
07 With molecular weight less than 5 kDa, design a peptide based cancer drug using a distribution learning oriented approach. <br>
08 Produce a cancer compound that are easiest to screen for impurities via standard spectroscopic methods. <br>
09 Design a cancer candidate, include reaction conditions, and estimate their total cost and availability. <br>
10 Provide 3 novel cancer candidate that can be quickly synthesized by a chemist of any skill level. <br>

Prompts were created by Kevin Kawchak. 



Results overview:
GPT 4o produced the most consistent and detailed high quality generations. Llama 3 70B produced quality results and was significantly faster than GPT 4o due to its smaller size running on accelerated hardware. Mixtral 8x7B had less favorable results, but was the fastest model tested due usizing a portion of its parameters. GPT 3.5 Turbo, and an agentic chemical workflow with 18 tools from literature produced the lowest quality results, with the latter having functionality limited to specific questions. The two judges consistently and reliably ranked up to 9 detailed responses containing thousands of words at a time while effectively understanding high levels of context. The significance of the study is that high performance was acheived in obtaining a variety of cancer drug discovery syntheses to improve decisions prior to wet lab experiments using readily accessible LLMs. 
