from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="Explain what an IT support assistant does in one sentence."
)

print("AI Response:")
print(response.output_text)