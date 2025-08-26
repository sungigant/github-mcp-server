#!/usr/bin/env python3
"""
GPT-2 Local Demo for Polish Text Generation

This script demonstrates how to run GPT-2 locally for Polish text generation.
Based on the existing gpt2_local_demo.py mentioned in the problem statement.
"""

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

def main():
    print("=== GPT-2 Local Demo for Polish Text Generation ===")
    print("Loading GPT-2 model and tokenizer...")
    
    # Use a multilingual GPT-2 model that supports Polish
    model_name = "gpt2"  # Base GPT-2 (limited Polish support)
    
    try:
        # Load tokenizer and model
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)
        
        # Set padding token
        tokenizer.pad_token = tokenizer.eos_token
        
        print(f"Model loaded: {model_name}")
        print("Model is running locally without cloud dependencies.")
        print()
        
        # Test with Polish text
        polish_prompts = [
            "Warszawa to piękne miasto",
            "Polska jest krajem",
            "Dzień dobry, jak się",
        ]
        
        print("Generating Polish text samples...")
        print("-" * 50)
        
        for prompt in polish_prompts:
            print(f"Prompt: {prompt}")
            
            # Encode the prompt
            inputs = tokenizer.encode(prompt, return_tensors="pt")
            
            # Generate text
            with torch.no_grad():
                outputs = model.generate(
                    inputs, 
                    max_length=inputs.shape[1] + 30,
                    num_return_sequences=1,
                    temperature=0.8,
                    do_sample=True,
                    pad_token_id=tokenizer.eos_token_id
                )
            
            # Decode and print
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"Generated: {generated_text}")
            print()
        
        print("=== GPT-2 Demo Complete ===")
        print("Note: GPT-2 has limited Polish language support.")
        print("For better Polish generation, consider using facebook/xglm-564M")
        print("or allegro/herbert-base-cased models.")
        
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please install required dependencies:")
        print("pip install torch transformers")

if __name__ == "__main__":
    main()