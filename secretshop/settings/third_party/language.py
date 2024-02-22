# region			  -----Supporting Variables-----
gettext = lambda s: s
# endregion

LANGUAGES = (
    ('ru', gettext('Русский')),
    ('uk', gettext('Украинский')),
    ('en', gettext('Английский')),
    ('fr', gettext('Французский')),
    ('bn', gettext('Бенгальский')),
    ('pt', gettext('Португальский')),
    ('in', gettext('Индонезийский')),
    ('ar', gettext('Арабский')),
    ('hi', gettext('Хинди')),
    ('es', gettext('Испанский')),
)

LANGUAGE_CODE = 'ru'

LANGUAGE_CODES = [language[0] for language in LANGUAGES]
