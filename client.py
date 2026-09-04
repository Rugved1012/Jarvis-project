from google import genai

# Initialize the Gemini client with your API key
client = genai.Client(
    api_key="dfgg"  # Replace with your actual Gemini API key
)

# Generate a response using the Gemini API
response = client.generate_response(
    model="gemini-1",
    context="You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud",
    user_input="what is coding"
)

# Print the response text
print(response.text)
