from urllib.request import urlopen
from urllib.parse import quote  # URL 인코딩을 위한 모듈
from bs4 import BeautifulSoup
import os

main_pages = {
    'en': 'Main_Page',
    'fr': 'Wikipédia:Accueil_principal',
    'id': 'Halaman_Utama',
    'tl': 'Unang_Pahina'
}

def get_links(language_code, page_title):
    # page_title을 URL 인코딩하여 비 ASCII 문자 처리
    url = f"https://{language_code}.wikipedia.org/wiki/{quote(page_title)}"
    response = urlopen(url)
    
    encoding = response.headers.get_content_charset(failobj='utf-8')
    html = response.read().decode(encoding)
    
    bs = BeautifulSoup(html, 'html.parser')
    
    # 모든 a 태그에서 href 추출
    links = []
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            href = link.attrs['href']
            if href.startswith('/wiki/') and ':' not in href:
                page = href.split('/wiki/')[1]
                links.append(page)
    return links

def crawl_wikipedia(language_code, page_title):
    try:
        # page_title을 URL 인코딩하여 비 ASCII 문자 처리
        url = f"https://{language_code}.wikipedia.org/wiki/{quote(page_title)}"
        response = urlopen(url)
        
        encoding = response.headers.get_content_charset(failobj='utf-8')
        html = response.read().decode(encoding)
        
        bs = BeautifulSoup(html, 'html.parser')

        # 페이지에서 텍스트만 추출
        content = bs.find('div', {'id': 'mw-content-text'}).get_text()
        return content
    except Exception as e:
        print(f"Error crawling {page_title}: {e}")
        return None

def save_to_file(language_code, file_num, content):
    filename = f"{language_code}-{file_num}.txt"  # 파일 이름을 언어코드-번호 형식으로 저장
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error saving file {filename}: {e}")

def crawl_main_pages_and_save(language_codes):
    file_counter = {code: 1 for code in language_codes}  # 각 언어별 파일 번호 카운터 생성

    for language_code in language_codes:
        page_title = main_pages.get(language_code, 'Main_Page')
        print(f"Crawling main page for {language_code}...")
        
        links = get_links(language_code, page_title)
        
        
        dir_name = "wiki_pages"
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        for i, link in enumerate(links):
            print(f"Crawling {link} in {language_code} Wikipedia...")
            content = crawl_wikipedia(language_code, link)
            if content:
                file_num = file_counter[language_code]  # 현재 언어 코드에 대한 파일 번호 가져오기
                save_to_file(f"{dir_name}/{language_code}", file_num, content)
                file_counter[language_code] += 1  # 파일 번호 증가
                print(f"Saved {language_code}-{file_num}.txt")
            else:
                print(f"Skipping page {i+1} due to an error.")


language_codes = ['en', 'fr', 'id', 'tl']


crawl_main_pages_and_save(language_codes)

