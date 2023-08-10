from anki.hooks import addHook


def start_here():
    from . import prepare
    # wquery.config.read()
    if not prepare.have_setup:
        prepare.customize_addcards()
    # wquery.start_services()
    # prepare.set_shortcut(shortcut)

addHook("profileLoaded", start_here)

