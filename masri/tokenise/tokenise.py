#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 12:28:27 2017

@author: albert
"""
from nltk.tokenize import RegexpTokenizer
from abc import ABC, abstractmethod
import re

class MTRegex:
    # Definite article + prepositions with cliticised article
    # DEF_ARTICLE = r'da|di|b[ħh]a|g[hħ]a|b[ħh]al|g[ħh]al|lil?|sa|ta|ma|fi?|mil?|bil?|[ġg]o|i|sa|bi[dtlrnsxzcżċ]-'
    DEF_ARTICLE = r'\w{0,5}?[dtlrnsxzcżċ]-'
    DEF_NUMERAL = r'-i[dtlrnsxzcżċ]'

    L_APOST = r"[’'](i?)l-?";

    # Apostrophised prepositions
    APOST = r'\w+a|[mtxbfs][\'’]'

    NUMBER = r'\d+'
    DECIMAL = r'\d+[\.,/]\d+'

    # All other tokens: string of alphanumeric chars, numbers or a single
    # non-alphanumeric char. (Accent or apostrophe allowed at end of string of alpha chars).
    WORD = r'\w+[`\']?|\S'

    ALPHA_WORD = "\w+";

    ALL_WORDS = DEF_ARTICLE + "|" + DEF_NUMERAL + "|" + L_APOST + "|" + APOST + "|" + WORD + "|" + ALPHA_WORD;

    END_PUNCTUATION = r'\?|\.|,|\!|;|:|…|"|\'|\.\.\.\''

    PROCLITIC_PREP = r"^\w['’]$"

    ABBREV_PREFIX = r"sant['’]|(a\.?m|p\.?m|onor|sra|nru|dott|kap|mons|dr|prof)\.?"

    NUMERIC_DATE = r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{2,4}[-/]\d{1,2}[-/]\d{1,2}"

    URL = "(((http|ftp|gopher|javascript|telnet|file|ssh|scp)://(www\.)?)|mailto:|www\.).+\\s$";
    URL2 = "(((http|ftp|https|gopher|javascript|telnet|file)://)|(www\.)|(mailto:))[\w\-_]+(\.[\w\-_]+)?([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?";

    # It-Tlieta, 25 ta' Frar, 2003
    FULL_DATE = "(^I[ltnsdxr]-(Tnejn|Tlieta|Erbgħa|Ħamis|Ġimgħa|Sibt|Ħadd), \d{1,2} ta' " + "(Jannar|Frar|Marzu|April|Mejju|Ġunju|Lulju|Awwissu|Settembru|Ottubru|Novembru|Diċembru), \d{4,}$)"

    # Hyphen-separated prefixes which shouldn't be separated from following words
    PREFIX = "(sotto|inter|intra|mini|ex|eks|pre|post|sub|neo|soċjo)-";

    # All tokens: definite article or token
    # TOKEN = DEF_ARTICLE + "|" + DEF_NUMERAL + "|" + APOST + "|" + L_APOST + "|" + ABBREV_PREFIX + "|" + NUMERIC_DATE + "|" + NUMBER + "|" + WORD;
    TOKEN = DEF_ARTICLE + "|" + DEF_NUMERAL + "|" + WORD + "|" + END_PUNCTUATION

    ALPHA_TOKEN = DEF_ARTICLE + "|" + DEF_NUMERAL + "|" + APOST + "|" + L_APOST + "|" + ABBREV_PREFIX + "|" + ALPHA_WORD;

    BLANK_LINE = r"^\s*[\r\n]+\s*$"

    @staticmethod
    def is_token(string):
        return re.match(MTRegex.TOKEN, string) is not None

    @staticmethod
    def is_end_of_sentence(word, next):
        if next is None:
            return False
        else:
            return MTRegex.is_end_punctuation(next) and not MTRegex.is_suffix(next) and not MTRegex.is_prefix(word)

    @staticmethod
    def is_end_punctuation(string):
        return re.match(MTRegex.END_PUNCTUATION, string) is not None

    @staticmethod
    def is_prefix(string):
        pattern = re.compile(MTRegex.DEF_ARTICLE + "|" + MTRegex.PROCLITIC_PREP + "|" + MTRegex.ABBREV_PREFIX,
                             re.IGNORECASE)
        return re.match(pattern, string) is not None

    @staticmethod
    def is_suffix(string):
        pattern = re.compile(MTRegex.DEF_NUMERAL, re.IGNORECASE)
        return re.match(pattern, string)

class MTTokenizer(ABC):

    @abstractmethod
    def tokenize(self, text):
        pass


class MTWordTokenizer(RegexpTokenizer, MTTokenizer):

    def __init__(self, *args):
        '''Initialise an MTTokenizer with a sequence of regexps that match different tokens.
        These are internally compiled in a disjunction (a|b|..|z)'''

        if len(args) == 0:
            args = [MTRegex.NUMERIC_DATE, MTRegex.DECIMAL, MTRegex.NUMBER,
                    MTRegex.DEF_ARTICLE, MTRegex.DEF_NUMERAL,
                    MTRegex.PROCLITIC_PREP,MTRegex.WORD,
                    MTRegex.END_PUNCTUATION]

        super().__init__("|".join(args), gaps=False, discard_empty=True,
                         flags=re.UNICODE | re.MULTILINE | re.DOTALL | re.IGNORECASE)

    def tokenize_fix_quotes(self, text):
        text = re.sub(u'[\u201c\u201d]', '"', text)
        text = re.sub(u'[\u2018\u2019]', "'", text)
        return self.tokenize(text)
