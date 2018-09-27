"""Madlibs Stories."""

class Story:
    """Madlibs story.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """     

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.words = words
        self.text = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.text

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text    


# Here's a story to get you started

story_list = {
    'long_long_ago': Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
           large {adjective} {noun}. It loved to {verb} {plural_noun}."""
       ),
    'cave_battle': Story(
        ["place", "second_place", "third_place"],
        """ONCE IN A CAVE, A BATTLE OCCURED THERE, {place}. The cavemen who came from {second_place} battled the
           other cavemen who came from {third_place}. It was a bloody battle. Very bloody. The end"""
       ),
    'catz': Story(
        ["place", "noun", "verb", "adjective", "plural_noun","second_place", "second_noun", "second_verb", "second_adjective", "second_plural_noun"],
        """CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS """
       )
}

# long_long_ago = Story(
#         ["place", "noun", "verb", "adjective", "plural_noun"],
#         """Once upon a time in a long-ago {place}, there lived a
#            large {adjective} {noun}. It loved to {verb} {plural_noun}."""
#        )

# cave_battle = Story(
#         ["place", "second_place", "third_place"],
#         """ONCE IN A CAVE, A BATTLE OCCURED THERE, {place}. The cavemen who came from {second_place} battled the
#            other cavemen who came from {third_place}. It was a bloody battle. Very bloody. The end"""
#        )

# catz = Story(
#         ["place", "noun", "verb", "adjective", "plural_noun","second_place", "second_noun", "second_verb", "second_adjective", "second_plural_noun"],
#         """CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS CATS """
#        )


