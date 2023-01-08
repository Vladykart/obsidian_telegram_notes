
import re
import pandas as pd
from snakemd import Document


df = pd.read_csv('message_webpage.csv')

def generate_md(df):
    messages = df.to_dict('records')
    print(messages)
    for message in messages:
        filename = str(message.get('title'))
        # replace special characters
        filename = re.sub(r'[^a-zA-Z0-9]', '_', filename)
        # replace multiple underscores with one
        filename = re.sub(r'_{2,}', '_', filename)
        # remove underscore from the beginning and the end of the string
        filename = re.sub(r'^_|_$', '', filename)
        # limit filename length to 100 characters
        filename = filename[:100]


        metadata = {
            'title': str(message['title']),
            'date': message['date'],
            'description': message['description'],
            'site_name': message['site_name'],
            'author': str(message['author']),
            'url': str(message['message']),
        }

        metadata_y = '''
        --- 
        alias: "Message"
        title: {title} 
        date: {date} 
        site_name: {site_name}
        author: "{author}"
        url: "{url}"
        --- 
        '''.format(**metadata)

        doc = Document(name=filename,)
        doc.add_paragraph('---')
        doc.add_paragraph('alias: "Message"')
        doc.add_paragraph('title: {title}'.format(**metadata))
        doc.add_paragraph('date: {date}'.format(**metadata))
        doc.add_paragraph('site_name: {site_name}'.format(**metadata))
        doc.add_paragraph('author: "{author}"'.format(**metadata))
        doc.add_paragraph('url: "{url}"'.format(**metadata))
        doc.add_paragraph('---')
        doc.add_header(str(message.get('title')), 1)
        doc.add_paragraph(str(message['message']))
        doc.add_paragraph(str(message['description']))
        doc.add_paragraph(str(message['site_name']))
        doc.add_paragraph(str(message['author']))
        doc.add_paragraph(str(message['date']))
        doc.output_page(dump_dir='note_dir')


generate_md(df)



#%%


#%%
