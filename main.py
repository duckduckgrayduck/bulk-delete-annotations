"""
This is an Add-On derived from the Hello World Template, it allows you to mass delete all annotations in a set of documents. 
"""

from documentcloud.addon import AddOn

class MassDeleteAnnotations(AddOn):
    """Add-On that runs through all documents in a selection or query and deletes annotations for them""" 

    def main(self):
        """The main add-on functionality goes here."""
        for document in self.get_documents():
            for note in document.annotations:
                note.delete()
                note.save()

if __name__ == "__main__":
    MassDeleteAnnotations().main()
