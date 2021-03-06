# -*- coding: utf-8 -*-

# Global constants
SMALL_S_CEDILLA = u'\u015f'
CAPITAL_S_CEDILLA = u'\u015e'
SMALL_S_COMMA = u'\u0219'
CAPITAL_S_COMMA = u'\u0218'
SMALL_T_CEDILLA = u'\u0163'
CAPITAL_T_CEDILLA = u'\u0162'
SMALL_T_COMMA = u'\u021b'
CAPITAL_T_COMMA = u'\u021a'
QUOTATION_MARK1 = u'\u201c'
QUOTATION_MARK2 = u'\u201d'
QUOTATION_MARK3 = u'\u201e'
QUOTATION_MARK4 = u'\u201f'
QUOTATION_MARK5 = u'\u201a'
QUOTATION_MARK6 = u'\u201b'
APOSTROPHE1 = u'\u2018'
APOSTROPHE2 = u'\u2019'
DAGGER = u'\u2020'
DOUBLE_DAGGER = u'\u2021'
BULLET = u'\u2022'
HYPHEN_BULLET = u'\u2043'
TRIANGULAR_BULLET = u'\u2023'
DOUBLE_EXCL = u'\u203c'
HORIZ_ELLIPSIS = u'\u2026'
TWO_DOT = u'\u2025'
ONE_DOT = u'\u2024'
UNICODE_WSPACE = u' '
UNICODE_CR = u'\n'
UNICODE_VOID = u''

A_HAT1 = u'\u01ce'
A_HAT2 = u'\u0103'

INVERTED_QUESTION_MARK = u'\u00bf'
DOUBLE_QUESTION_MARK = u'\u2047'
INVERTED_EXCLAMATION_MARK = u'\u00a1'
DOUBLE_EXCLAMATION_MARK = u'\u203c'

SECTION_SIGN = u'\u00a7'
PILCROW_SIGN = u'\u00b6'

FIGURE_DASH = u'\u2012'
EN_DASH = u'\u2013'
EM_DASH = u'\u2014'
HORIZ_BAR = u'\u2015'

# Translation table
TRANSTAB = {ord(u'\t') : UNICODE_WSPACE, \
            ord(u'\f') : UNICODE_WSPACE, \
            ord(u'\v') : UNICODE_CR, \
            ord(A_HAT1) : A_HAT2, \
            ord(SMALL_S_CEDILLA) : SMALL_S_COMMA, \
            ord(CAPITAL_S_CEDILLA) : CAPITAL_S_COMMA, \
            ord(SMALL_T_CEDILLA) : SMALL_T_COMMA, \
            ord(CAPITAL_T_CEDILLA) : CAPITAL_T_COMMA, \
            ord(APOSTROPHE1) : u'\'', \
            ord(APOSTROPHE2) : u'\'', \
            ord(DOUBLE_EXCL) : u'!', \
            ord(INVERTED_EXCLAMATION_MARK) : u'!', \
            ord(DOUBLE_EXCLAMATION_MARK) : u'!', \
            ord(HORIZ_ELLIPSIS) : u'.', \
            ord(ONE_DOT) : u'.', \
            ord(TWO_DOT) : u'.', \
            ord(INVERTED_QUESTION_MARK) : u'?', \
            ord(DOUBLE_QUESTION_MARK) : u'?', \
            ord(FIGURE_DASH) : u'-', \
            ord(EN_DASH) : u'-', \
            ord(EM_DASH) : u'-', \
            ord(HORIZ_BAR) : u'-', \
            ord(DAGGER) : None, \
            ord(DOUBLE_DAGGER) : None, \
            ord(BULLET) : None, \
            ord(TRIANGULAR_BULLET) : None, \
            ord(HYPHEN_BULLET) : None, \
            ord(SECTION_SIGN) : None, \
            ord(PILCROW_SIGN) : None, \
            ord(QUOTATION_MARK1) : None, \
            ord(QUOTATION_MARK2) : None, \
            ord(QUOTATION_MARK3) : None, \
            ord(QUOTATION_MARK4) : None, \
            ord(QUOTATION_MARK5) : None, \
            ord(QUOTATION_MARK6) : None, \
            ord(u'"') : None, \
            ord(u'\r') : None, \
            ord(u'\a') : None, \
            ord(u'\b') : None}

# Allowed character set
ALLOWED_CHARSET = u' -\'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzĂăÂâȘșȚțÎîÃãẼẽĨĩÕõŨũỸỹÑñǍǎĚěǏǐǑǒǓǔŠšŤťȞȟĽľŇňŽžČčĎďŘřǨǩǙǚÊêÎîÔôÛûŶŷĴĵĈĉĤĥẐẑŜŝĔĕŎŏĬĭŬŭĞğÅåŮůĄąĘęĮįǪǫŲųßĐđŁłÀàÈèÌìÒòÙùỲỳẀẁȦȧĖėİıȮȯẆẇṖṗṘṙṄṅṀṁṪṫḊḋḞḟĠġḢḣȷĿŀḂḃŻżṠṡĊċÁáÉéÍíÓóÚúÝýŃńÇçŔŕŚśŹźḾḿĹĺḰḱǴǵẂẃǗǘŰűŐőÄäËëÏïÖöÜüŸÿẄẅẌẍŖŗŞşŢţḐḑĢģĻļÇçŅņȨȩḨḩ'

# Loan character set
LOAN_CHARS = u'ÃãǍǎÅåĄąÀàȦȧÁáÄäḂḃČčĈĉĊċĆćÇçĐđĎďḊḋḐḑẼẽĚěÊêĔĕĘęÈèĖėÉéËëȨȩḞḟĜĝǦǧĞğĠġǴǵĢģĤĥȞȟḢḣḦḧḨḩĨĩǏǐÎîĬĭĮįÌìİıÍíÏïĴĵǨǩḰḱĶķŁłĽľĿŀĹĺĻļṀṁḾḿÑñŇňǸǹṄṅŃńŅņÕõǑǒÔôŎŏǪǫÒòȮȯÓóŐőÖöṖṗṔṕẪầŘřṘṙŔŕŖŗŠšŜŝṠṡŚśŞşŤťṪṫŢţŨũǓǔÛûŬŭŮůŲųÙùÚúŰűÜüṼṽǙǚǛǜǗǘŴŵẀẁẆẇẂẃẄẅẊẋẌẍỸỹŶŷỲỳẎẏÝýŸÿŽžẐẑŻżŹźß'

# Romanian specific characters
ROU_CHARS = u'șțăîâȘȚĂÎÂ'

# Word separators
WORD_SEP = ur'\s|!|\?|;|,|\.|\(|\)|\[|\]|\{|\}|\^|~|#|\*|\+|/|<|>|:|"|”|„|§|©|€'

# Acronym suffixes
ACRONYM_SUFFIXES = [
    u'-ul', \
    u'-uri', \
    u'-ului', \
    u'-urile', \
    u'-urilor', \
]

STRANGE_NGRAMS = [u'vt', u'gg', u'ww', u'kk', u'qq', \
                  u'xx', u'hh', u'jj', u'tt', u'zz', \
                  u'vv', u'kp', u'zk', u'qw', u'df', \
                  u'hz', u'hj', u'jk', u'kj', u'kl', \
                  u'zx', u'xz', u'vc', u'bv', u'dd', \
                  u'bb', u'kc', u'yj', u'yg', u'yh', \
                  u'yz', u'yt', u'yq', u'aa', u'mh', \
                  u'nh', u'jh', u'xh', u'fh', u'hf', \
                  u'qh', u'hq', u'tg', u'fg', u'fb', \
                  u'fm', u'fp', u'pf', u'df', u'fd', \
                  u'wf', u'wk', u'tf', u'tg', u'tv', \
                  u'sd', u'sx', u'xs', u'xg', u'cx', \
                  u'xn', u'xm', u'xp', u'xj', u'xf', \
                  u'bz', u'cb', u'rr', u'ss', u'pp', \
                  u'pd', u'ăă', u'șș', u'țț', u'îî', \
                  u'ââ', u'iiii', u'eee', u'uuu', u'aaa', \
                  u'by', u'srsc', u'ăa', u'aă', u'âa', u'aâ', \
                  u'tț', u'șț', u'sț', u'țș', u'tș', u'jș']

