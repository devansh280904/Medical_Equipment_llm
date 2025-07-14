from llama_cpp import Llama

model_path = "models/phi2-medical-merged-q8.gguf"
llm = Llama(model_path=model_path, n_ctx=2048, n_threads=8)

prompt = "Q:what are the steps to use infant incubators ,explain?\nA:"
output = llm(
                    prompt,
                    max_tokens=300,
                    temperature=0.7,
                    top_p=0.95,
                    echo=False
                )
print("Model response:", output["choices"][0]["text"].strip())