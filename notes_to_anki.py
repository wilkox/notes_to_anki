# Deck
currentDeck = "Medicine::Endocrine"

# Import the main window object (mw) from aqt
from aqt import mw
# Import the "show info" tool from utils.py
from aqt.utils import showInfo
# Import all of the Qt GUI library
from aqt.qt import *
# Import TextImporter tool
from anki.importing import TextImporter

def importFlashcards():

    # Import cards
    for notetype in ['Basic', 'Cloze', 'Definition']:

        filename = os.path.expanduser("~/tmp/" + notetype.lower() + ".csv")
        linecount = sum(1 for line in open(filename))
        if linecount > 1:
            # Select deck
            did = mw.col.decks.id(currentDeck)
            mw.col.decks.select(did)
            # Set note type
            m = mw.col.models.byName(notetype)
            # Set note type for deck
            deck = mw.col.decks.get(did)
            deck['mid'] = m['id']
            mw.col.decks.save(deck)
            # Import into the collection
            ti = TextImporter(mw.col, filename)
            ti.allowHTML = True
            ti.initMapping()
            ti.run()

    showInfo("Import complete")

# Create a new menu item in 'Tools'
action = QAction("Import flashcards into %s deck" % currentDeck, mw)
action.triggered.connect(importFlashcards)
mw.form.menuTools.addAction(action)
