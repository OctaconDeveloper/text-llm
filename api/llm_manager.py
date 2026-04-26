import os
from llama_cpp import Llama
from .config import MODELS_DIR, N_CTX, N_THREADS

class LLMManager:
    def __init__(self):
        self.llm = None
        self.current_model_name = None

    def load_model(self, model_filename):
        model_path = os.path.join(MODELS_DIR, model_filename)
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file {model_filename} not found")

        # Unload previous model
        if self.llm is not None:
            print(f"Unloading model: {self.current_model_name}")
            del self.llm
            self.llm = None
        
        print(f"Loading model: {model_filename}...")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=N_CTX,
            n_threads=N_THREADS,
            verbose=False
        )
        self.current_model_name = model_filename
        return self.llm

    def get_llm(self):
        return self.llm

    def get_current_model(self):
        return self.current_model_name

# Singleton instance
manager = LLMManager()
