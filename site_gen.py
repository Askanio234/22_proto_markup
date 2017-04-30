import staticjinja


requests_data = {
    'title': 'Заявки',
    "indents_title": "Заявки",
    'user_name': 'Леонид Федорович',
    'indents': 10,
    "final_button_name": "Показать еще"
}

if __name__ == '__main__':
    site = staticjinja.make_site(outpath='site', contexts=[
        ('indents.html', requests_data)
    ])
    site.render()
