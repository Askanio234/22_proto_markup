import staticjinja


index_data = {
	"title": "Главная",
	"indents_title": "Свежие заявки",
	"user_name": "Леонид Федорович",
	"indents": 10
}


requests_data = {
    "title": "Заявки",
    "indents_title": "Заявки",
    "user_name": "Леонид Федорович",
    "indents": 10
}


if __name__ == "__main__":
    site = staticjinja.make_site(outpath="site", contexts=[
        ('indents.html', requests_data),
        ("index.html", index_data)
    ])
    site.render()
