# Deck
currentDeck = "Medicine::Neuro"

# Import the main window object (mw) from aqt
from aqt import mw
# Import the "show info" tool from utils.py
from aqt.utils import showInfo
# Import all of the Qt GUI library
from aqt.qt import *
# Import TextImporter tool
from anki.importing import TextImporter

def importFlashcards():

    # Select deck
    did = mw.col.decks.id(currentDeck)
    mw.col.decks.select(did)

    # Import basic cards
    basicf = os.path.expanduser("~/tmp/basic.csv")
    # Set note type
    m = mw.col.models.byName("Basic")
    # Set note type for deck
    deck = mw.col.decks.get(did)
    deck['mid'] = m['id']
    mw.col.decks.save(deck)
    # Import into the collection
    ti = TextImporter(mw.col, basicf)
    ti.initMapping()
    ti.run()

    # Import definition cards
    basicf = os.path.expanduser("~/tmp/definition.csv")
    # Set note type
    m = mw.col.models.byName("Definition")
    # Set note type for deck
    deck = mw.col.decks.get(did)
    deck['mid'] = m['id']
    mw.col.decks.save(deck)
    # Import into the collection
    ti = TextImporter(mw.col, basicf)
    ti.initMapping()
    ti.run()

    # Import cloze cards
    basicf = os.path.expanduser("~/tmp/cloze.csv")
    # Set note type
    m = mw.col.models.byName("Cloze")
    # Set note type for deck
    deck = mw.col.decks.get(did)
    deck['mid'] = m['id']
    mw.col.decks.save(deck)
    # Import into the collection
    ti = TextImporter(mw.col, basicf)
    ti.initMapping()
    ti.run()

    showInfo("Import complete")

# Create a new menu item in 'Tools'
action = QAction("Import flashcards into %s deck" % currentDeck, mw)
action.triggered.connect(importFlashcards)
mw.form.menuTools.addAction(action)
