import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time


def fetch(word):
    URL = f"https://dictionary.cambridge.org/us/dictionary/english/{word}"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                      'Safari/537.36',
        'Referer': URL,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    page_content = soup.find("div", class_="page")

    dictionary = page_content.find_all("div", class_="pr dictionary")[0]

    entries = dictionary.find_all("div", class_="pr entry-body__el")
    queries = []

    for entry in entries:
        # 包含单词、词性、音标
        header = entry.find("div", class_="pos-header dpos-h")
        # 包含定义、例句、近义词等
        body = entry.find("div", class_="pos-body")

        word_type_element = header.find("span", class_="pos dpos")
        if word_type_element is None:
            word_type = ""
        else:
            word_type = word_type_element.text

        try:
            pron_us_element = header.find("span", class_="us").find("span", class_="pron")
        except:
            pron_us_element = None
        if pron_us_element is None:
            pron_us = ""
        else:
            pron_us = pron_us_element.text


        boxes = body.find_all("div", class_="sense-body dsense_b")
        for box in boxes:
            definition_box = box.find("div", class_="ddef_h")
            examples_box = definition_box.parent.find("div", class_="def-body")

            definition_element = definition_box.find("div", class_="def")
            if definition_element is None:
                definition = ""
            else:
                definition = definition_element.text

            examples = []
            if examples_box != None:
                for example in examples_box.find_all("span", class_="eg deg"):
                    examples.append(example.text)

            s = pd.Series({
                "word": word,
                'wordType': word_type,
                "phoneticSymbol": pron_us,
                "definition": definition,
                "examples": "@".join(examples)
            })
            queries.append(s)

    return queries


if __name__ =="__main__":
    f = open('vocabulary/COCA_20000.txt')
    data = f.readlines()
    data = list(map(lambda x: x.replace('\n', ''), data))

    queries = []
    for word in tqdm(data):
        try:
            s = fetch(word)
            queries += s
        except:
            fuck = open('data/error.txt', 'a')
            fuck.write(f"{word}\n")

    df = pd.DataFrame(queries)
    df.to_csv('dictionary.csv')


