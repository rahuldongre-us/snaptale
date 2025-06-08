import base64
import io
import logging
from typing import Optional, Any 
from PIL import Image 
from openai import OpenAI

logging.basicConfig(level=logging.INFO) 

class CommonUtils:
    
    @staticmethod
    def convert_image_to_base64(image: Image.Image) -> str:
        """Converts the image to base64."""
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()
        return base64.b64encode(img_bytes).decode('utf-8')

    @staticmethod
    def validate_api_key(api_key: str) -> bool:
        """Validates that the API key is provided and not empty."""
        return bool(api_key and api_key.strip())

    @staticmethod
    def validate_image(image: Optional[Image.Image]) -> bool:
        """Validates that an image is provided."""
        return image is not None

    @staticmethod
    def call_mistral_vision_api(api_key: str, model_name: str, prompt: str, base64_image: str) -> str:
        try:
            client = OpenAI(base_url="https://api.studio.nebius.com/v1/", api_key=api_key)
            chat_completion = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                    ],
                }],
                model=model_name
            )
            return chat_completion.choices[0].message.content or "Error: No content returned"
        except Exception as e:
            error_message = f"Error calling Nebius Vision API: {str(e)}"
            logging.error(error_message)
            return error_message

    @staticmethod
    def create_story_prompt() -> str:

        ret_str =  f"""You are an expert storyteller. Based on the provided content, create a compelling story that captures the essence of the material.
        1. Focus on the main themes and key points.
        2. Use vivid descriptions and engaging language to bring the story to life.
        3. Ensure the story is coherent and flows logically from one point to the next.
        4. If the content is too short, expand on the themes and add relevant details to enrich the narrative.
        5. If the content is too long, summarize the key points while maintaining the story's essence.
        6. If the content is ambiguous, state your assumptions clearly.
        7. If the content is not suitable for storytelling, provide a brief explanation of why it cannot be transformed into a story.
        8. If the content is suitable for storytelling, present the story in a clear, engaging format.
        IMPORTANT: After the main story, include a section clearly marked with **Notes**: that summarizes the key points from the story, and another section marked with **QnA**: that contains questions and answers related to the story. 
        Example format:
        **Story**: [Your story here]
        **Notes**: [Key points from the story]
        **QnA**: [Questions and answers related to the story]"""
        return ret_str

    @staticmethod
    def process_story_teller(api_key:str, image_data: Any) -> str:
        """Processes the story teller query and returns a response."""
        try:
 
            logging.info(f"[process_story_teller]")

            if not CommonUtils.validate_api_key(api_key):
                return "Invalid API key. Please check your credentials." 
            
            if not CommonUtils.validate_image(image_data):
                return "Please upload image first."
            else:
                base64_image = CommonUtils.convert_image_to_base64(image_data)
                vision_model_name = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
                prompt = CommonUtils.create_story_prompt()
                response = CommonUtils.call_mistral_vision_api(api_key, vision_model_name, prompt, base64_image)

                logging.info(f"Raw AI response: {response}")

                if not response:
                    return "No response received from the API. Please try again later."  

                ai_response = response.strip() 

                if ai_response.lower().startswith("error"):
                    return ("An error occurred while processing your story. Please check the API key and try again.", "", "")
                 
                notes_idx = ai_response.find("**Notes")
                qna_idx = ai_response.find("**QnA")
                main = ai_response[:notes_idx].replace("**Story**:", "").replace("**","").strip()
                notes_data = ai_response[notes_idx:qna_idx].replace("**Notes**:", "").replace("**","").strip()
                qna_data = ai_response[qna_idx:].replace("**QnA**:", "").replace("**","").strip()
                return (main, notes_data, qna_data)
            
        except Exception as e:
            print(f"[process_story_teller ERROR] {e}")
            return "An error occurred while processing your story." 
        
    @staticmethod
    def clear_outputs():
        """Clear all outputs"""
        return ("🔄 Cleared All - Ready for new Story", "", "", "")