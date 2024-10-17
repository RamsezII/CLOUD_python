import openai

# Remplace par ta propre clé d'API OpenAI
openai.api_key = 'TA_CLE_API'


def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Erreur : {str(e)}"


if __name__ == "__main__":
    prompt = "Tu es un PNJ dans un jeu vidéo. Quelle est ta mission ici ?"
    response = get_response(prompt)
    print(response)
