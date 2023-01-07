import openai

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "API-Key"

def generate_science_fact():
  # Set the prompt for the model
  prompt = "fetch random physics fact from wikipedia"

  # Use the OpenAI API to generate a science fact
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      temperature=0.5,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=1
  )
  # Return the generated science fact
  return response["choices"][-1]["text"]


# Generate a science fact
science_fact = generate_science_fact()
api.update_status(science_fact)
