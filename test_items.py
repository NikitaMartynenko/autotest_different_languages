import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_guest_should_see_login_link(browser, user_language):
    button_dict = {"ar": "أضف الى سلة التسوق", "ca": "Afegeix a la cistella",
                   "cs": "Vložit do košíku", "da": "Læg i kurv",
                   "de": "In Warenkorb legen", "en-gb": "Add to basket",
                   "el": "Προσθήκη στο καλάθι", "es": "Añadir al carrito",
                   "fi": "Lisää koriin", "fr": "Ajouter au panier",
                   "it": "Aggiungi al carrello", "ko": "장바구니 담기",
                   "nl": "Voeg aan winkelmand toe", "pl": "Dodaj do koszyka",
                   "pt": "Adicionar ao carrinho", "pt-br": "Adicionar à cesta",
                   "ro": "Adauga in cos", "ru": "Добавить в корзину",
                   "sk": "Pridať do košíka", "uk": "Додати в кошик",
                   "zh-cn": "Add to basket"}

    browser.get(f"http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/")
    browser.implicitly_wait(6)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert add_to_basket_button.text == button_dict[user_language], f"expected '{button_dict[user_language]}', got {add_to_basket_button.text}"
    print(f'add_to_basket_button.text = {button_dict[user_language]}')
