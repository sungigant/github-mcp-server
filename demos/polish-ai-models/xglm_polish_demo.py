#!/usr/bin/env python3
"""
XGLM-564M Polish Language Demo

This script demonstrates facebook/xglm-564M model for Polish text generation.
XGLM is a multilingual generative language model that supports Polish.
"""

import torch
from transformers import XGLMTokenizer, XGLMForCausalLM
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

def main():
    print("=== XGLM-564M Polish Language Demo ===")
    print("Loading XGLM-564M model (multilingual, supports Polish)...")
    
    model_name = "facebook/xglm-564M"
    
    try:
        # Load tokenizer and model
        print("Downloading model... (this may take a while on first run)")
        tokenizer = XGLMTokenizer.from_pretrained(model_name)
        model = XGLMForCausalLM.from_pretrained(model_name)
        
        print(f"Model loaded: {model_name}")
        print("Model is running locally without cloud dependencies.")
        print()
        
        # Polish text prompts
        polish_prompts = [
            "Warszawa to stolica Polski i",
            "Polskie góry to",
            "Najlepsze polskie jedzenie to",
            "Historia Polski rozpoczęła się",
            "Współczesna Polska jest"
        ]
        
        print("Generating Polish text with XGLM-564M...")
        print("-" * 60)
        
        for prompt in polish_prompts:
            print(f"Prompt: {prompt}")
            
            # Encode the prompt
            inputs = tokenizer(prompt, return_tensors="pt")
            
            # Generate text
            with torch.no_grad():
                outputs = model.generate(
                    inputs["input_ids"],
                    max_length=inputs["input_ids"].shape[1] + 40,
                    num_return_sequences=1,
                    temperature=0.8,
                    do_sample=True,
                    pad_token_id=tokenizer.pad_token_id,
                    repetition_penalty=1.1
                )
            
            # Decode and print
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"Generated: {generated_text}")
            print()
        
        print("=== XGLM-564M Demo Complete ===")
        print("XGLM-564M provides excellent multilingual support including Polish.")
        print("This model is recommended for Polish text generation tasks.")
        
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please install required dependencies:")
        print("pip install torch transformers")
        print("\nNote: This model requires ~2.3GB of disk space.")

if __name__ == "__main__":
    main()