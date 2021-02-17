# from .maltese_g2p import transcribe
from masri.transcribe.g2p.maltese_g2p import g2p_cw_rules
from masri.tokenise.tokenise import MTWordTokenizer

tokeniser = MTWordTokenizer()

def text2phon(text, tokenise=False):

    if tokenise:
        tokens = (tokeniser.tokenize(text))
        return ' '.join([g2p_cw_rules(tok) for tok in tokens])

    return g2p_cw_rules(text)
