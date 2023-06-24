import openai
class AIConnection():
    @staticmethod
    def connect_ai(user_content:str,robot_content:str):
        openai.api_key = "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"

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
