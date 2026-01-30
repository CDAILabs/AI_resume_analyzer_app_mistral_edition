from llama_cpp import Llama
import os


class LLMClient:
    def __init__(self, model_path: str, use_gpu: bool = True):
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"LLM model not found at:\n{model_path}"
            )

        self.model_path = model_path

        # GPU if available, otherwise fallback to CPU
        if use_gpu:
            try:
                self.llm = Llama(
                    model_path=model_path,
                    n_ctx=2048,
                    n_gpu_layers=-1,   # Use GPU if supported
                    n_batch=512,
                    n_threads=4
                )
                print("✅ LLM running on GPU")
            except Exception as e:
                print("⚠️ GPU init failed, falling back to CPU")
                print(e)
                self._init_cpu()
        else:
            self._init_cpu()

    def _init_cpu(self):
        self.llm = Llama(
            model_path=self.model_path,
            n_ctx=2048,
            n_threads=4
        )
        print("✅ LLM running on CPU")

    def get_llm(self):
        return self.llm
