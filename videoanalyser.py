import openai
import youtube as yt
# Your OpenAI API key
openai.api_key = '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'

def generate_response(transcript, instructions):
    
    # Concatenate pre_prompt with instructions to form the full prompt
    full_prompt = transcript + " " + instructions
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": full_prompt}
            ]
        )
        
        # Extract and return the assistant's response
        if response and response['choices']:
            return response['choices'][0]['message']['content'].strip()
        else:
            return "No response generated."
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Example usage
video_url = 'https://www.youtube.com/watch?v=5JpPo-NOq9s'
transcript = yt.save_transcript_as_json_paragraph(video_url)
instructions = "IMPORTANT INSTRUCTION Please Read the  all of the above text and analyse the whole paragraph to select 3 of these 7 skills: 1.Articulate 2. Story teller 3. Technical Expert 4. Great Vocab 5. Grammar Master 6. Artistic Expressor 7.Empathy. Please note that you should give select the most appropriate skills first based on the text. OUTPUT MUST BE AS FOLLOWS: (articulate,empathy,story teller)"

generated_text = generate_response(transcript, instructions)
print(generated_text)
