from bs4 import BeautifulSoup

with open ('123.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

tr_cards = soup.find_all('tr', class_='vcard user-row')

for i, tr_card in enumerate(tr_cards):
    span_elements_fn = tr_card.find('span', class_="fn")
    span_elements_username = tr_card.find('span', class_="username")
    span_elements_email = tr_card.find('span', class_="email")
    span_elements_td = tr_card.find('td', class_="minNoWrap")
    span_elements_ul = tr_card.find('ul', class_="toggle-list")

    print(
        f"{span_elements_fn.text}, {span_elements_username.text}, {span_elements_email.text}, {span_elements_td.text.split()},{span_elements_ul.text.split()},")
