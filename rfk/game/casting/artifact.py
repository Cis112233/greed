from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """An artifact item, inherits from Actor
    
    The artifact stores and returns a message

    Attributes:
        self: an instance of artifact
    """
    def __init__(self):
        """Constructs a new artifact 

        Args:
            self: an instance of artifact
        """
        super().__init__()
        self.message = ""
    
    def get_message(self):
        """Returns the stored message

        Args:
            self: an instance of artifact
        """
        return self.message
    
    def set_message(self, mess):
        """Stores a given message

        Args:
            self: an instance of artifact
            mess: a message string
        """
        self.message = mess