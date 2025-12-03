"""Local LLM Module for running models locally.

This module provides a wrapper for running local LLM models using transformers.
"""

import logging
from typing import Optional, Tuple
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)


class LocalLLMClient:
    """Client for running local LLM models.
    
    This class provides an interface compatible with the LLMProvider
    for running models locally using transformers.
    """
    
    def __init__(self, model_name: str = "Qwen/Qwen2-0.5B-Instruct"):
        """Initialize the local LLM client.
        
        Args:
            model_name: HuggingFace model name to load
        """
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Initializing local LLM client with model: {model_name} on device: {self.device}")
        
    def _load_model(self):
        """Lazy load the model and tokenizer."""
        if self.model is None:
            logger.info(f"Loading model {self.model_name}...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto" if self.device == "cuda" else None
            )
            if self.device == "cpu":
                self.model = self.model.to(self.device)
            logger.info(f"Model loaded successfully on {self.device}")
    
    async def generate_content(
        self, 
        model: str, 
        contents: str, 
        config: dict
    ) -> 'LocalLLMResponse':
        """Generate content using the local model.
        
        Args:
            model: Model name (ignored, uses initialized model)
            contents: Input prompt
            config: Generation config with max_output_tokens and temperature
            
        Returns:
            LocalLLMResponse object with text and usage metadata
        """
        self._load_model()
        
        max_tokens = config.get("max_output_tokens", 512)
        temperature = config.get("temperature", 1.0)
        
        # Format prompt for chat models
        messages = [{"role": "user", "content": contents}]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        # Tokenize
        inputs = self.tokenizer([text], return_tensors="pt").to(self.device)
        input_length = inputs.input_ids.shape[1]
        
        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=temperature > 0,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        # Decode only the generated tokens
        generated_ids = outputs[0][input_length:]
        response_text = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        
        # Calculate token counts
        output_length = len(generated_ids)
        
        return LocalLLMResponse(
            text=response_text,
            prompt_token_count=input_length,
            candidates_token_count=output_length,
            total_token_count=input_length + output_length
        )


class LocalLLMResponse:
    """Response object for local LLM generation."""
    
    def __init__(
        self, 
        text: str, 
        prompt_token_count: int,
        candidates_token_count: int,
        total_token_count: int
    ):
        """Initialize response.
        
        Args:
            text: Generated text
            prompt_token_count: Number of tokens in prompt
            candidates_token_count: Number of tokens generated
            total_token_count: Total tokens used
        """
        self.text = text
        self.usage_metadata = type('obj', (object,), {
            'prompt_token_count': prompt_token_count,
            'candidates_token_count': candidates_token_count,
            'total_token_count': total_token_count
        })()


class LocalLLMWrapper:
    """Wrapper to make LocalLLMClient compatible with LLMProvider expectations."""
    
    def __init__(self, model_name: str = "Qwen/Qwen2-0.5B-Instruct"):
        """Initialize wrapper.
        
        Args:
            model_name: HuggingFace model name
        """
        self.client = LocalLLMClient(model_name)
        self.models = self.client
