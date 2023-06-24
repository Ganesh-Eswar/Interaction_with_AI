import openai

"""
Create your API SECRET KEY:
Visit the OpenAI website: Go to the OpenAI platform website at https://www.openai.com/.

Sign in or sign up: If you already have an account, sign in using your credentials. 
Otherwise, create a new account by signing up.

Access the API section: Once you're logged in, navigate to the API section of the OpenAI platform. 
This is where you can manage your API keys.

Generate a new API key: In the API section, look for the option to generate a new API key. 
Click on it to create a new key specifically for accessing the ChatGPT API.

Store your API key securely: Once the API key is generated, make sure to copy and store it in a safe and secure location. 
Treat your API key as confidential information and avoid sharing it publicly or committing it to version control repositories.

Configure your API key in your code: Depending on how you plan to use the ChatGPT API, you will need to configure your API key in your code. 
This typically involves adding the API key as a parameter or environment variable when making API requests. 
"""
        
class AIConnection():
    @staticmethod
    def connect_ai(user_content:str,robot_content:str):
        openai.api_key = "PASTE YOUR SECRET KEY HERE"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": robot_content},
                    {"role": "user", "content": user_content},
                ]
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        return result
