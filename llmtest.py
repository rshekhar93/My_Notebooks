import json
import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def parse_unstructured_text(input):
    prompt = f"""
            For each entry in the JSON Array below, extract the following fields
            
            Input JSON: {input}
            
            Fields:
            - client_id
            - full_name (in separate parts)
            - address (dict of full address, city, state (infer from city, postcode or landline area code) 
            	and postcode if present, note that a Level or Suite number is part of the address)
            - position (dict of company and title if present, prefer to have title)
            - phone_numbers (dict of mobile and landline phone numbers if present, format as INTL string. 
            	Mostly Australian numbers, infer landline area code from address))
            - email_address (if present)
            - website (if present)
            - social_media (dict with full profile urls for platform)
            - other_info (dict of key-value pairs if present)
            
            Valid JSON Output, omit fields that are not present:
              """

    response = openai.Completion.create(
      					model="text-davinci-003", 
      					prompt=prompt, 
      					temperature=0, 
      					max_tokens=3000,
                        top_p=1, 
      					frequency_penalty=0, 
      					presence_penalty=0
    				)

    try:
        j = json.loads(response["choices"][0]["text"])
    except json.decoder.JSONDecodeError:
        j = None
        
    out = {"prompt": prompt, "output": response["choices"][0]["text"], "json": j, "response": response}

    return out


def main():
    input = """ Client ID: 123456, Daniel Lawson | Data Analytics Consultant, The Data School Australia |
            Lvl 12 500 Collins Street Melbourne Victoria 3000 // mob. 0455123456 / 
            e. daniel.lee.lawson@example.com insta: @_danlsn, twitter: @_danlsn, github: @danlsn, 
            w. danlsn.com.au | bus. 9555 5555 | B.Arch (Design), M.Marketing (Distinction)"""

    out = parse_unstructured_text(input)
    print(out["output"])


if __name__ == "__main__":
    main()
