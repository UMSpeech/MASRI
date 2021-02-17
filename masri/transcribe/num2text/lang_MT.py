from num2words import lang_EU, num2words

class Num2Word_MT(lang_EU.Num2Word_EU):

    def set_high_numwords(self, high):
        max = 3 + 3 * len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10 ** n] = word + "iljun"

    def setup(self):
        lows = ["non", "okt", "sett", "sist", "kwint", "kwadr", "tr", "b", "m"]
        units = ["", "un", "duo", "tri", "kwattor", "kwin", "sist", "sept",
                 "okto", "novem"]
        tens = ["deċ", "viġint", "triġint", "kwadriġint", "kwindiġint",
                "sestaġint", "septaġint", "oktoġint", "nonaġint"]
        self.high_numwords = ["ċent"] + self.gen_high_numwords(units, tens,
                                                               lows)
        self.negword = "nieqes "
        self.pointword = "punt"
        self.exclude_title = ["u", "punt", "nieqes"]

        # self.high_numwords = []
        self.mid_numwords = [(1000, "elf"), (2000, 'elfejn'), (100, "mija"),
                             (90, "disgħin"), (80, "tmenin"), (70, "sebgħin"),
                             (60, "sittin"), (50, "ħamsin"), (40, "erbgħin"),
                             (30, "tletin")]
        self.low_numwords = ["għoxrin", "dsatax", "tmintax", "sbatax",
                             "sittax", "ħmistax", "erbatax", "tlettax",
                             "tnax", "ħdax", "għaxra", "disgħa", "tmienja",
                             "sebgħa", "sitta", "ħamsa", "erbgħa", "tlieta", "tnejn",
                             "wieħed", "żero"]
        self.ords = {1: "l-ewwel",
                     2: "it-tieni",
                     3: "it-tielet",
                     4: "ir-raba'",
                     5: "il-ħames",
                     6: "is-sitt",
                     7: "is-seba'",
                     8: "it-tmien",
                     9: "id-disa'",
                     10: "l-għaxar",
                     100: "il-mitt"}
        self.counters = ["", "", "żewġ", "tlett", "erba'", "ħames", "sitt", "seba'", "tmin", "disa'", "għaxar"]
        self.hundreds = ["", 'mija', 'mitejn', 'mija', 'mija', 'mija', 'mija', 'mija', 'mija', 'mija', 'mija']
        self.thousands = ['', 'elf', 'elfejn', 'elef', 'elef', 'elef', 'elef', 'elef', 'elef', 'elef', 'elef']


    def _starts_with_vowel(self, text):
        return text[0] in ['a', 'e', 'i', 'o', 'u']


    def _starts_with_coronal(self, text):
        return text[0] in ['ċ', 'd', 't', 's', 'z', 'ż', 'x']


    def _add_article(self, text):
        template = "{d}-{t}"

        if self._starts_with_vowel(text):
            return template.format(d="l", t=text)
        elif self._starts_with_coronal(text):
            return template.format(d=text[0], t=text)
        else:
            return template.format(d="il", t=text)

    def _check_plural(self, lnum, ltext, rnum, rtext):
        # print(lnum)
        if (lnum % 10 > 1 or lnum == 10) and rnum > 1000:
            return rtext + "i"

        return rtext

    def _hundreds_thousands(self, lnum, ltext, rnum, rtext):
        is_dual = False
        r_list = []

        if rnum < 1000000:
            #choose the appropriate rtext:
            if rnum % 1000 == 0:
                r_list = self.thousands
                is_dual = (lnum == 2)

            elif rnum % 100 == 0:
                r_list = self.hundreds
                is_dual = (lnum == 2)

            if lnum < len(r_list):
                rtext = r_list[lnum]
            else:
                rtext = r_list[1]

        if is_dual:
            ltext = ""

        elif lnum <= 10:
            if lnum == 3 and rnum != 1000:
                ltext = 'tliet'
            elif lnum == 8 and rnum != 1000:
                ltext = 'tmien'
            else:
                ltext = self.counters[lnum]

                if len(ltext) > 0 and not ltext.endswith('t') and self._starts_with_vowel(rtext):
                    ltext = ltext.strip("'") + "t"

        elif lnum < 20:
            rtext = "il-" + rtext

        #Since lnum > rnum, if lnum % 100 >= 1, then rnum must be >= 1000
        #Here we only deal with 1 and 2
        #mitt elf u elf, mitt elf u elfejn
        elif (lnum % 100 == 1 or  lnum%100 ==2):
            #Example: 101,000 -> mitt elf u elf
            #Example: 101,101 -> mitt elf u elf u wieħed
            #lnum -> hundreds * rnum; units * rnum
            lnum_mod = lnum % 100
            lnum_h = lnum - lnum_mod #e.g. 101-1 = 100
            ltext = self.to_cardinal(lnum_h * rnum) #"mitt elf"
            rtext = " u " + self.to_cardinal(lnum_mod * rnum)  #"elf"

        #Here we deal with all other cases
        #mija u tlett elef
        elif(2 < lnum % 100 <= 10):
            lnum_mod = lnum % 100 #3
            lnum_h = lnum - lnum_mod #103-3 = 100
            ltext = self.to_cardinal(lnum_h) #mija
            rtext = " u " + self.to_cardinal(lnum_mod*rnum) # mija + u + tlett elef

        # Hundreds of thousands, etc: mija -> mitt
        elif 99 < lnum <= 900:
            if lnum % 100 == 0:
                ltext = ltext.replace("mija", "mitt")

        rtext = self._check_plural(lnum, ltext, rnum, rtext)
        return lnum, ltext.strip(), rnum, rtext.strip()

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s u %s" % (rtext, ltext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s u %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            (lnum, ltext, rnum, rtext) = self._hundreds_thousands(lnum, ltext, rnum, rtext)
            return ("%s %s" % (ltext, rtext), lnum * rnum)

        return ("%s u %s" % (ltext.strip(), rtext.strip()), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)

        if value in self.ords:
            return self.ords[value]
        else:
            return self._add_article(self.to_cardinal(value).strip())

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, suffix=None, longval=True):
        if val < 0:
            val = abs(val)
            suffix = 'QK' if not suffix else suffix

        card_text = self.to_cardinal(val)

        if suffix:
            return "%s %s" %(card_text, suffix)
        else:
            return card_text

# if __name__ == "__main__":
#
#     conv = Num2Word_MT()
#     print(conv.to_cardinal(103000))
#     print(conv.to_cardinal(3503302))
