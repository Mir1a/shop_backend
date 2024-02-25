# region			  -----Supporting Variables-----
gettext = lambda s: s
# endregion

LANGUAGES = (
    ('en', gettext('en')),
)

LANGUAGE_CODE = 'en'

LANGUAGE_CODES = [language[0] for language in LANGUAGES]
