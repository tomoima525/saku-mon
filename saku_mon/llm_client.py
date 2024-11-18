from openai import OpenAI

# TODO: Implement generic LLM Client
# TODO: Consider using https://platform.openai.com/docs/api-reference/assistants/createAssistant for LLM

# system prompt as a constant
system_prompt = "You are a software engineer at a tech company. You have been tasked with creating a coding test."

class OpenAIClient:
    def __init__(self):
      self.client = OpenAI()
      self.model = "gpt-4o"
      self.temperature = 0.7

    def generate_completion(self, prompt: str, response_format=None):
      if response_format is None:
        response = self.client.chat.completions.create(
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
        model=self.model,
        temperature=self.temperature,
        response_format=response_format
        )
        return response.choices[0].message.content.strip()
      else:
        response = self.client.beta.chat.completions.parse(
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
        model=self.model,
        temperature=self.temperature,
        response_format=response_format
        )
        return response.choices[0].message.parsed