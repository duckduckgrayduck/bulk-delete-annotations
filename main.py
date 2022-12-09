"""
This is a hello world add-on for DocumentCloud.

It demonstrates how to write a add-on which can be activated from the
DocumentCloud add-on system and run using Github Actions.  It receives data
from DocumentCloud via the request dispatch and writes data back to
DocumentCloud using the standard API
"""

from documentcloud.addon import AddOn


class MassDeleteAnnotations(AddOn):
    """Add-On that runs through all documents in a selection or query and deletes annotations for them""" 

    def main(self):
        """The main add-on functionality goes here."""
   
        for document in self.get_documents():
            for note in doc_obj.annotations:
                document.annotations.delete(note)

if __name__ == "__main__":
    MassDeleteAnnotations().main()
