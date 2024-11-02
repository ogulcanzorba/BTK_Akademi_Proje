# utils.py
import os
import google.generativeai as genai

# Configure API Key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Define a function to interact with the generative model

def generate_response(user_input):
    try:
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="tunedModels/pro-tuning-deneme-sj0763s2h4fw",
            generation_config=generation_config,
        )

        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_input)

        return response.text if response else "No response from the model."

    except Exception as e:
        print("Error in generate_response:", e)  # Log the error
        return "An error occurred while generating the response."
