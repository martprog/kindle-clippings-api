import re

# Parser logic function
def parse_clippings(file_path):
    clippings_list = []

    with open(file_path, 'r', encoding='utf-8') as file:
        clippings = file.read()

    # Define regular expressions for different locales
    locales = {
        'en': r'Your Highlight on page (\d+) \| Location (\d+)-(\d+) \| Added on (.+)',
        'de': r'Ihre Markierung auf Seite (\d+) \| bei Position (\d+)-(\d+) \| Hinzugefügt am (.+)',
        'es': r'Su marcador en la página (\d+) \| Posición (\d+)-(\d+) \| Agregado el (.+)'
    }

    # Split clippings by '=========='
    clipping_sections = clippings.split('==========')

    # Iterate through clipping sections and extract information
    for section in clipping_sections:
        if section.strip():
            lines = section.strip().split('\n')

            # Detect the locale by matching the message in the section
            detected_locale = None
            for locale, pattern in locales.items():
                if re.search(pattern, lines[1]):
                    detected_locale = locale
                    break

            if detected_locale:
                match = re.search(locales[detected_locale], lines[1])
                if match:
                    page = match.group(1)
                    location_start = match.group(2)
                    location_end = match.group(3)
                    added_date = match.group(4)
                    title_author = lines[0].strip()
                    clipping_text = lines[3].strip()
                    tit_aut_split = title_author.split("(")
                    title = tit_aut_split[0].strip()  # Remove leading/trailing whitespaces
                    author = tit_aut_split[-1].replace(")", "").strip()  # Remove ")" and whitespaces

                    # Create a dictionary to store the extracted data
                    clipping_data = {
                        'title': title,
                        'author': author,
                        'page': page,
                        'location_start': location_start,
                        'location_end': location_end,
                        'added_date': added_date,
                        'clipping_text': clipping_text,
                        #'sentiment': sentence.labels[0].value
                    }

                    clippings_list.append(clipping_data)

    return clippings_list