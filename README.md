# 🧒📚 Snap-a-Tale - Snap a picture, get a tale!

![Snapster](https://github.com/rahuldongre-us/snaptale/blob/main/assets/s1.jpg?raw=true) 

**SnapTale** is an open-source AI vision interface that combines Gradio and Mistral-Small-3.1-24B-Instruct-2503 to transform visual inputs into insightful, structured responses. Built for developers and researchers, SnapTale allows you to upload an image and receive intelligent interpretations using cutting-edge multimodal AI models.

![Upload Image ](https://github.com/rahuldongre-us/snaptale/blob/main/assets/s2.jpg?raw=true)

![Supply Nebius API KEY](https://github.com/rahuldongre-us/snaptale/blob/main/assets/s3.jpg?raw=true)

![Generated Story](https://github.com/rahuldongre-us/snaptale/blob/main/assets/s4.jpg?raw=true)

![Generated Note](https://github.com/rahuldongre-us/snaptale/blob/main/assets/s5.jpg?raw=true)

![Generate QnA](https://github.com/rahuldongre-us/snaptale/blob/main/assets/s6.jpg?raw=true)

---

## 🚀 Features

📸 Image Upload & Analysis: Easily upload images via an intuitive Gradio UI.

🧠 Powered by Mistral AI: Leverages the Mistral-Small-3.1-24B-Instruct-2503 model for high-quality instruction-following and visual understanding.

⚡ Fast, Local or Remote Inference: Supports local and remote model inference (e.g., via Hugging Face endpoints, Nebius or vLLM).

🌐 Web Interface: Clean, interactive UI using Gradio.

🔧 Modular Architecture: Organized into app.py, main_ui.py, and utils.py for easy customization and extension.

--- 

## 🛠️ Tech Stack

Python 3.10+

Gradio for front-end interface

mistralai/Mistral-Small-3.1-24B-Instruct-2503 for model inference

Hugging Face Transformers or vLLM for model deployment

---

## ⚙️ Quick Start

### Prerequisites

- Nebius Vision API Key, https://studio.nebius.com/
- Python 3.7+ 

### Clone the Repository

```bash
git clone https://github.com/rahuldongre-us/snaptale.git

cd snaptale

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python app.py or gradio app.py
```
---

🧠 Resources

[Gradio](https://www.gradio.app/) 

[Nebius](https://nebius.com/)

---

🙌 Acknowledgments

Built with ❤️ by Rahul Dongre
Inspired by open-source stacks worldwide.
