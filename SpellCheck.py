
import nltk
from nltk.tokenize import sent_tokenize
import language_tool_python
corr_text = ""
senlist = []

class SpellCheck():
    def __init__(self):
        pass
    def Checker(self,text):
        '''sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        dictionary_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_dictionary_en_82_765.txt")
        bigram_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
        )
        # term_index is the column of the term and count_index is the
        # column of the term frequency
        sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
        sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

        # lookup suggestions for multi-word input strings (supports compound
        # splitting & merging)
        # text = text.rstrip("\n")
        gg = ''
        k=[]
        #text = sent_tokenize(text)

        #for i in text:

            input_term = text

        # max edit distance per lookup (per single word, not per whole input string)
            suggestions = sym_spell.lookup_compound(
                input_term, max_edit_distance=2, ignore_non_words=True)
        # display suggestion term, edit distance, and term frequency

            #gg+=str(suggestions[0].term)
            #gg+=". "
            # k.append(list(gg))
        #with  language_tool_python.LanguageToolPublicAPI('en-us') as tool:
            #ntext= tool.correct(gg)
        print(suggestions[0].term)
        #return str(ntext)'''
    #text = sent_tokenize(text)
        with language_tool_python.LanguageToolPublicAPI('en-us') as tool:
            corr_text= tool.correct(text)

        return corr_text
#text, corr_text = checker(text=text)
# print(corr_text)
