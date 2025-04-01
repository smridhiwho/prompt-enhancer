from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class PromptEnhancer:
    def __init__(self):
        # Using a smaller model for faster inference
        self.model_name = "facebook/opt-125m"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        
        # Load the model to GPU if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
        # Load prompt engineering best practices
        self.best_practices = [
            "Be specific and clear",
            "Include context and constraints",
            "Specify the desired output format",
            "Break down complex tasks",
            "Use examples when possible",
            "Include error handling requirements",
            "Specify performance criteria",
            "Add relevant constraints"
        ]
    
    def enhance_prompt(self, original_prompt):
        # Create a system prompt that incorporates best practices
        system_prompt = """You are a prompt engineering expert. Your task is to enhance the given prompt following these best practices:
        1. Be specific and clear
        2. Include context and constraints
        3. Specify the desired output format
        4. Break down complex tasks
        5. Use examples when possible
        6. Include error handling requirements
        7. Specify performance criteria
        8. Add relevant constraints
        
        Original prompt: {original_prompt}
        
        Enhanced prompt:"""
        
        # Prepare the input
        inputs = self.tokenizer(system_prompt.format(original_prompt=original_prompt), 
                              return_tensors="pt").to(self.device)
        
        # Generate enhanced prompt
        outputs = self.model.generate(
            inputs.input_ids,
            max_length=200,
            num_return_sequences=1,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        # Decode and clean up the output
        enhanced_prompt = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract only the enhanced part (after "Enhanced prompt:")
        enhanced_prompt = enhanced_prompt.split("Enhanced prompt:")[-1].strip()
        
        return enhanced_prompt

# Create a singleton instance
enhancer = PromptEnhancer()

def enhance_prompt(prompt):
    """
    Main function to enhance a prompt using the PromptEnhancer class.
    """
    return enhancer.enhance_prompt(prompt) 