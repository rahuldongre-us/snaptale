import gradio as gr
from main_ui import main_ui_app 

theme = gr.themes.Ocean(
    secondary_hue="fuchsia",
    font=['IBM Plex Sans', gr.themes.GoogleFont('ui-sans-serif'), 'system-ui', 'sans-serif'],
).set(
    background_fill_secondary_dark='*block_background_fill',
    button_border_width='*block_border_width',
    button_border_width_dark='*block_border_width',
    button_large_radius='*radius_sm'
)

with gr.Blocks(theme=theme) as demo: 

    gr.HTML("""
    <div style="text-align: center; background: linear-gradient(135deg, #a2acda 0%, #846a9f 100%); border-radius: 12px; margin-bottom: 25px; padding: 20px;">
        <h1> 🧒📚 Snap-a-Tale - Snap a picture, get a tale!</h1>
        <p> 🦊 Snapster the Fox, A clever little fox with a camera around his neck and a scroll in his paw.</p>
        <ul style="list-style-type: none; padding: 0; margin: 0;">
            <li>📸 Upload an image</li>
            <li>📝 Get a Story, Notes, Questions and Answers</li> 
        </ul>
    </div>
    """) 
    
    main_ui_app()
            
demo.launch(max_file_size="5mb", debug=False, show_error=True)