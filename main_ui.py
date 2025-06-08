import gradio as gr 
from utils import CommonUtils 

def on_submit(text, context_input):
    return CommonUtils.process_story_teller(text, context_input)

def main_ui_app(): 
    
    with gr.Blocks() as app:
       
        with gr.Row(): 
              with gr.Column():
                gr.Markdown("**🔒 Privacy:** Your images will not be stored or shared with other users.")
                gr.Markdown("**🔐 Sensitive Image :** Please do not upload sensitive image containing personal data.")
                image_data = gr.Image(type="pil", label="Upload Image", sources=["upload"],
                                    elem_id="story-image-upload", show_label=True, height=500)

        with gr.Row(): 
            with gr.Column():
                gr.Markdown("**🔒 Privacy:** Your API keys is not stored or shared with other users.")
                api_key_input = gr.Textbox(
                    label="Enter your API KEY", placeholder="Your Nebius API Key...", info="NEBIUS, Personal API key for authentication", type="password",
                )
                submit_button = gr.Button("🚀 Generate Your Story", variant="primary")
                clear_button = gr.Button("Clear", variant="secondary")  

                gr.Markdown(
                    value="""
                            ## 🦊 Say hello to Snapster the Fox 
                            ### Your brave and curious companion on a picture-powered storytelling journey!
                            ### Ready to Generate Story! 📝
                            **How to use:**
                            1. Upload an image using the **Upload Image** button.
                            2. Enter your **API Key** in the provided field. Make sure you have a valid API key from Nebius Vision. https://studio.nebius.com/
                            3. Click the **'Generate Your Story'** button to process the image and generate a story.
                            4. View the generated story, notes, and questions and answers in the respective boxes below.
                            5. You can clear the input and output fields using the **Clear** button.

                            **Note:**
                            - Ensure your API key is valid and has access to the Nebius Vision API.
                            - The image should be relevant to the story you want to generate.
                            - The image should be in a supported format (JPEG, PNG).
                            - The image size should not exceed 5MB.
                            - The image should not contain sensitive personal data.
                            - The image should not contain any copyrighted material.
                            - The image should not contain any offensive or inappropriate content.""",
                                                height=500,
                                                show_label=True
                )

            with gr.Column():
                ai_output = gr.Textbox(
                    label="Your Story",
                    placeholder="AI story response will appear here...",
                    lines=10,
                ) 
                notes_box = gr.Textbox(
                    label="Notes", 
                    lines=10,
                    placeholder="Notes about the story will appear here...",
                    interactive=False,
                )
                qna_box = gr.Textbox(
                    label="Questions and Answers", lines=10, interactive=False, placeholder="Relevant Question and Answers regarding the story will appear here...",
                )   

    # Define the function to handle the submit and clear button   

    submit_button.click(CommonUtils.process_story_teller, inputs=[api_key_input, image_data], outputs=[ai_output,notes_box,qna_box])

    clear_button.click(CommonUtils.clear_outputs, outputs=[ai_output,notes_box,qna_box, api_key_input])
 

    return app
