JAZZMIN_SETTINGS = {
    "site_title": "Bycomment",
    "site_header": "Bycomment",
    "site_logo": "assets/logo.png",
    "site_logo_classes": "",
    "changeform_format": "vertical_tabs",
    "hide_models": [
        "tariff.Giglet", 
        "project.Tariff", 
        "project.TariffCategory", 
        "project.TariffSubcategory"
    ],
    "custom_links": {
        "finance": [{
            "name": "Заявки на вывод",
            "url": "/admin/finance/transaction/?type__exact=2&status__exact=1",
            "icon": "fas fa-comments",
            "permissions": []
        }],
        "tariff": [
            {
                "name": "Категории тарифа",
                "url": "/admin/project/tariffcategory",
            },
            {
                "name": "Подкатегории тарифа",
                "url": "/admin/project/tariffsubcategory",
            },
            {
                "name": "Тарифы",
                "url": "/admin/project/tariff",
            },
        ],
    }
}
