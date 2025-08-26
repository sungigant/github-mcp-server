#!/usr/bin/env python3
"""
HerBERT Polish Language Demo

This script demonstrates allegro/herbert-base-cased model for Polish text processing.
HerBERT is a Polish BERT model specifically trained for Polish language understanding.
"""

import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

def main():
    print("=== HerBERT Polish Language Demo ===")
    print("Loading HerBERT model (specialized for Polish)...")
    
    model_name = "allegro/herbert-base-cased"
    
    try:
        # Load tokenizer and model
        print("Loading HerBERT model... (this may take a while on first run)")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForMaskedLM.from_pretrained(model_name)
        
        print(f"Model loaded: {model_name}")
        print("Model is running locally without cloud dependencies.")
        print()
        
        # Polish text examples with masked tokens
        polish_examples = [
            "Warszawa to [MASK] Polski.",
            "Polskie [MASK] są bardzo piękne.",
            "W Polsce mieszka około [MASK] milionów ludzi.",
            "Najsłynniejszy polski poeta to Adam [MASK].",
            "Polska [MASK] w Europie Środkowej."
        ]
        
        print("Performing masked language modeling with HerBERT...")
        print("-" * 60)
        
        for text in polish_examples:
            print(f"Input: {text}")
            
            # Tokenize input
            inputs = tokenizer(text, return_tensors="pt")
            
            # Find mask token position
            mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]
            
            # Get predictions
            with torch.no_grad():
                outputs = model(**inputs)
                predictions = outputs.logits
            
            # Get top 3 predictions for the masked token
            mask_token_logits = predictions[0, mask_token_index, :]
            top_tokens = torch.topk(mask_token_logits, 3, dim=1).indices[0].tolist()
            
            print("Top 3 predictions:")
            for i, token_id in enumerate(top_tokens, 1):
                token = tokenizer.decode([token_id])
                filled_text = text.replace("[MASK]", token)
                print(f"  {i}. {filled_text}")
            print()
        
        # Demonstrate text encoding/understanding
        print("Demonstrating text understanding capabilities...")
        print("-" * 60)
        
        sample_texts = [
            "To jest przykład polskiego tekstu.",
            "HerBERT rozumie język polski bardzo dobrze.",
            "Model został wytrenowany na polskich tekstach."
        ]
        
        for text in sample_texts:
            inputs = tokenizer(text, return_tensors="pt")
            with torch.no_grad():
                outputs = model(**inputs)
            
            print(f"Text: {text}")
            print(f"Encoded length: {inputs['input_ids'].shape[1]} tokens")
            print(f"Hidden states shape: {outputs.last_hidden_state.shape}")
            print()
        
        print("=== HerBERT Demo Complete ===")
        print("HerBERT excels at Polish language understanding tasks like:")
        print("- Text classification")
        print("- Named entity recognition")
        print("- Sentiment analysis")
        print("- Masked language modeling")
        
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please install required dependencies:")
        print("pip install torch transformers")
        print("\nNote: This model requires ~500MB of disk space.")

if __name__ == "__main__":
    main()