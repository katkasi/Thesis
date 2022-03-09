import pympi
import pandas as pd

speakers = {
    "N1": {
        "elan_name": "05",
        "age": "46-",
        "dialect": "Szo",
        "location": "város",
        "rutin": "1",
    },
    "N2": {
        "elan_name": "N2",
        "age": "-45",
        "dialect": "Szo",
        "location": "város",
        "rutin": "1",
    },
    "N3": {
        "elan_name": "N3",
        "age": "-45",
        "dialect": "Szi",
        "location": "város",
        "rutin": "1",
    },
    "N4": {
        "elan_name": "N4",
        "age": "-45",
        "dialect": "Szi",
        "location": "város",
        "rutin": "1",
    },
    "N5": {
        "elan_name": "13",
        "age": "46-",
        "dialect": "Szi",
        "location": "falu",
        "rutin": "2",
        "con_tiernames": {'13_cl',
                      '13_int_clear',
                      '13_int_clear',
                      '13_int_type',
                      '13_cons',
                      '13_gloss',
                      '13_int_cl_2',
                      '13_cs',
                      '13_wd',
                      '13_morf',
                      '13_morf_dic',
                      '13_clause'
                          }
    },
    "N6": {
         "elan_name": "N6",
        "age": "-45",
        "dialect": "Szo",
        "location": "falu",
        "rutin": "0",
    },
    "N7": {
        "elan_name": "N7",
        "age": "-45",
        "dialect": "Szo",
        "location": "falu",
        "rutin": "0",
    },
    "N8": {
        "elan_name": "N8",
        "age": "46-",
        "dialect": "Szo",
        "location": "falu",
        "rutin": "0",
    },
    "N9": {
        "elan_name": "12",
        "age": "46-",
        "dialect": "Szi",
        "location": "falu",
        "rutin": "1",
        "con_tiernames": {'12_cl',
                      '12_int_clear',
                      '12_int_clear',
                      '12_int_type',
                      '12_cons',
                      '12_gloss',
                      '12_int_cl_2',
                      '12_cs',
                      '12_wd',
                      '12_morf',
                      '12_morf_dic',
                      '12_clause'
                          }
    },
    "N10": {
        "elan_name": "18",
        "age": "46-",
        "dialect": "Szo",
        "location": "falu",
        "rutin": "1",
        "con_tiernames": {'18_cl',
                      '18_int_clear',
                      '18_int_clear',
                      '18_int_type',
                      '18_cons',
                      '18_gloss',
                      '18_int_cl_2',
                      '18_cs',
                      '18_wd',
                      '18_morf',
                      '18_morf_dic',
                      '18_clause'
                          }
    },
    "F1": {
        "elan_name": "19",
        "age": "46-",
        "dialect": "Szi",
        "location": "falu",
        "rutin": "1",
        "con_tiernames": {'19_cl',
                      '19_int_clear',
                      '19_int_clear',
                      '19_int_type',
                      '19_cons',
                      '19_gloss',
                      '19_int_cl_2',
                      '19_cs',
                      '19_wd',
                      '19_morf',
                      '19_morf_dic',
                      '19_clause'
                          }
    }
}

con_filenames = {
    "K1": {
        "cl": ['05_cl', '12_cl'],
        "int_clear": ['05_int_clear', '12_int_clear'],
        "int_type": ['05_int_type', '12_int_type'],
        "cons": ['05_cons', '12_cons'],
        "gloss": ['05_gloss', '12_gloss'],
        "int_cl": ['05_int_cl_2', '12_int_cl_2'],
        "wd": ['05_wd', '12_wd'],
        "morf": ['05_morf', '12_morf'],
        "cs": ['05_cs', '12_cs'],
        "morf_dic": ['05_morf_dic', '12_morf_dic'],
        "clause": ['05_clause', '12_clause']
    },
    "K2": {
        "cl": ['05_cl', '13_cl'],
        "int_clear": ['05_int_clear', '13_int_clear'],
        "int_type": ['05_int_type', '13_int_type'],
        "cons": ['05_cons', '13_cons'],
        "gloss": ['05_gloss', '13_gloss'],
        "int_cl": ['05_int_cl_2', '13_int_cl_2'],
        "wd": ['05_wd', '13_wd'],
        "morf": ['05_morf', '13_morf'],
        "cs": ['05_cs', '13_cs'],
        "clause": ['05_clause', '13_clause']
    },
    "K3": {
        "cl": ['05_cl', '18_cl', '19_cl'],
        "int_clear": ['05_int_clear', '18_int_clear', '19_int_clear'],
        "int_type": ['05_int_type', '18_int_type', '19_int_type'],
        "cons": ['05_cons', '18_cons', '19_cons'],
        "gloss": ['05_gloss', '18_gloss', '19_gloss'],
        "int_cl": ['05_int_cl_2', '18_int_cl_2', '19_int_cl_2'],
        "cs": ['05_cs', '18_cs', '19_cs'],
        "wd": ['05_wd', '18_wd', '19_wd'],
        "morf": ['05_morf', '18_morf', '19_morf'],
        "clause": ['05_clause', '18_clause', '19_clause']
    }
}

mon_filenames = {
    "N1": {
        "speaker": "N1",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2-cp'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    },
    "N2": {
        "speaker": "N2",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    },
    "N3": {
        "speaker": "N3",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    },
    "N4": {
        "speaker": "N4",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    },
    "N5": {
        "speaker": "N5",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    },
    "N6": {
        "speaker": "N6",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    },
    "N7": {
        "speaker": "N7",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    },
    "N8": {
        "speaker": "N8",
        "tiers": {
            "cl": ['cl'],
            "int_clear": ['int_clear'],
            "int_type": ['int_type'],
            "cons": ['cons'],
            "gloss": ['gloss'],
            "int_cl": ['int_cl_2'],
            "wd": ['wd'],
            "morf": ['morf'],
            "cs": ['cs'],
            "morf_dic": ['morf_dic'],
            "clause": ['clause']
        }
    }
}

class EafLoader:
    def __init__(self):
        self.cache = {}

    def load_eaf(self, filename):
        if filename in self.cache:
            return self.cache[filename]

        eaf = pympi.Elan.Eaf(filename + ".eaf")
        pympi.Elan.parse_eaf(filename + ".eaf", eaf)
        self.cache[filename] = eaf
        return eaf


eaf_loader = EafLoader()
#felparsolja a fájlt és behatárolja a megadott korlátok közti beszédszakaszt
def get_raw_data(filename, tier_id):
    eaf = eaf_loader.load_eaf(filename)
    if filename == 'K3':
        annotations = eaf.get_annotation_data_between_times(tier_id, 0, 1055000)
    elif filename == 'N5':
        annotations = eaf.get_annotation_data_between_times(tier_id, 152000, 469611)
    elif filename == 'N6':
        annotations = eaf.get_annotation_data_between_times(tier_id, 32000, 386000)
    elif filename == 'N7':
        annotations = eaf.get_annotation_data_between_times(tier_id, 106000, 460000)
    else:
        print("Using all annotations file file", filename)
        annotations = eaf.get_annotation_data_for_tier(tier_id)

    return annotations

#kiszedi az adott annotációs sorából az annotációkat. A végeredmény egy tupleoket tartalmazó lista
def get_annotation_from_a_tier(filename, tier_id):
    data = []
    corpus = get_raw_data(filename, tier_id)
    for type in corpus:
        data.append(type)

    return data

#kinyeri az adott egységbe eső másik tier annotációit
def get_int_data_from_tier(filename, tier_id, clause_start, clause_end):
    """folparsolja a fajlt"""
    eaf = eaf_loader.load_eaf(filename)
    annotations = eaf.get_annotation_data_between_times(tier_id, clause_start, clause_end)
    ret = []
    for element in annotations:
        if (element[0] + 30) > clause_end or (element[1] - 30) < clause_start:
            continue
        ret.append(element)

    return ret

#előszedi a beszélőt a mapból
def get_speaker_by_tier_id(tier_id, spdata):
    sp = None
    for speaker in spdata:
        if tier_id[0:2] == spdata[speaker]['elan_name']:
            sp = speaker
            break
    return sp

#előszedi a beszélőt a mapból
def get_tier_id_by_speaker(tier_id, spdata):
    tiername = None
    sp = None
    for speaker in spdata:
        if tier_id[0:2] == spdata[speaker]['elan_name']:
            sp = speaker
            tiername = tier_id
            break
    return sp, tiername

#megállapítja, hogy egy egység teljesen vagy csak részlegesen esik-e bele a nagyobb egységbe
def get_type_int_data(filename, tier_id, clause_start, clause_end):
    data = []
    corpus = get_int_data_from_tier(filename, tier_id, clause_start, clause_end)
    for type in corpus:
        if type[0] < clause_start and type[1] > clause_end:
            type = (*type, 'part_beginning+end')
            data.append(type)
        elif type[0] < clause_start:
            type = (*type, 'part_beginning')
            data.append(type)
        elif type[1] > clause_end:
            type = (*type, 'part_+end')
            data.append(type)
        else:
            type = (*type, 'full')
            data.append(type)

    return data

#CLAUSES
all_annotations = []
#CONVERSATION DATA
for filename in con_filenames:
    labels = ["recording", "start", "end", "clause",
              "speech_type", "speaker", "age", "dialect", "location", "rutin", "words", "words_count"]
    for tier_id in con_filenames[filename]["clause"]:
        sp = get_speaker_by_tier_id(tier_id, speakers)

        data = get_raw_data(filename, tier_id)

        words = []
        for annotation in data:

            if annotation[2][0] == "<":
                tag = "partial"
            elif annotation[2][0] == "#":
                tag = "unknown"
            elif annotation[2][0] == "?":
                tag = "unknown"
            elif annotation[2][0] == "*":
                tag = "unknown"
            elif annotation[2][0] == "=":
                tag = "no_word"
            elif annotation[2][0] == "%":
                tag = "no_word"
            else:
                tag = "full"

            words = annotation[2].split(' ')
            while '%' in words:
                words.remove('%')
            while '=' in words:
                words.remove('=')
            while '*' in words:
                words.remove('*')

            a = [
                filename,
                annotation[0],
                annotation[1],
                annotation[2],
                'con',
                sp,
                speakers[sp]['age'],
                speakers[sp]['dialect'],
                speakers[sp]['location'],
                speakers[sp]['rutin'],
                words,
                len(words),
                tag
            ]

            all_annotations.append(a)

#NARRATIVE DATA
for filename in mon_filenames:
    labels = ["recording", "start", "end", "clause",
              "speech_type", "speaker", "age", "dialect", "location", "rutin", "words", "words_count"]
    tiername = mon_filenames[filename]['tiers']['clause'][0]
    data = get_raw_data(filename, 'clause')
    sp = filename
    words = []
    for annotation in data:

        if annotation[2][0] == "<":
            tag = "partial"
        elif annotation[2][0] == "#":
            tag = "unknown"
        elif annotation[2][0] == "?":
            tag = "unknown"
        elif annotation[2][0] == "*":
            tag = "unknown"
        elif annotation[2][0] == "=":
            tag = "no_word"
        elif annotation[2][0] == "%":
            tag = "no_word"
        else:
            tag = "full"

        words = annotation[2].split(' ')
        while '%' in words:
            words.remove('%')
        while '=' in words:
            words.remove('=')
        while '*' in words:
            words.remove('*')

        a = [
            filename,
            annotation[0],
            annotation[1],
            annotation[2],
            'mon',
            sp,
            speakers[sp]['age'],
            speakers[sp]['dialect'],
            speakers[sp]['location'],
            speakers[sp]['rutin'],
            words,
            len(words),
            tag
        ]

        all_annotations.append(a)

print(all_annotations)

#IU PER CLAUSE
int_in_clause = []
for i,annotation in enumerate(all_annotations):
    if i % 100 == 0:
        print('processing', i)
    if annotation[4] == 'mon':
        tiername = mon_filenames[annotation[0]]['tiers']['int_type'][0]
        data = get_type_int_data(annotation[0], tiername, annotation[1], annotation[2])
        sum_IE_length = 0
        token_IE = 0
        non_token_IE = 0
        for element in data:
            ty = element[4].split('_')
            if ty[0] == 'part':
                sum_IE_length = 'no_data'
            elif sum_IE_length != 'no_data':
                part_sum_IE_length = element[1] - element[0]
                sum_IE_length += part_sum_IE_length

            if element[3] == '%':
                non_token_IE = non_token_IE + 1
            elif element[3] == '*':
                non_token_IE = non_token_IE + 1
            elif element[3] == '#':
                non_token_IE = non_token_IE + 1
            elif element[3] == '@':
                non_token_IE = non_token_IE + 1
            elif element[3] == '=':
                non_token_IE = non_token_IE + 1
            elif element[3] == 'уты':
                non_token_IE = non_token_IE + 1
            else:
                token_IE = token_IE + 1
            a = [
                annotation[0],
                annotation[1],
                annotation[2],
                annotation[3],
                annotation[4],
                annotation[5],
                annotation[6],
                annotation[7],
                annotation[8],
                annotation[9],
                annotation[10],
                annotation[11],
                annotation[12],
                len(data),
                sum_IE_length,
                token_IE,
                non_token_IE,
                data
                ]
        int_in_clause.append(a)
    if annotation[4] == 'con':
        tiername = None
        for tn in con_filenames[annotation[0]]['int_type']:
            if tn[0:2] == speakers[annotation[5]]["elan_name"]:
                tiername = tn
                break
        if tiername is None:
            raise KeyError("No elan name matches the speaker id.")
        data = get_type_int_data(annotation[0], tiername, annotation[1], annotation[2])
        sum_IE_length = 0
        token_IE = 0
        non_token_IE = 0
        for element in data:
            ty = element[4].split('_')
            if ty[0] == 'part':
                sum_IE_length = 'no_data'
            elif sum_IE_length != 'no_data':
                part_sum_IE_length = element[1] - element[0]
                sum_IE_length += part_sum_IE_length

            words = annotation[3].split(' ')
            if element[3] == '%':
                non_token_IE = non_token_IE + 1
            elif element[3] == '*':
                non_token_IE = non_token_IE + 1
            elif element[3] == '#':
                non_token_IE = non_token_IE + 1
            elif element[3] == '@':
                non_token_IE = non_token_IE + 1
            elif element[3] == '=':
                non_token_IE = non_token_IE + 1
            elif element[3] == 'уты':
                non_token_IE = non_token_IE + 1
            else:
                token_IE = token_IE + 1
            a = [
                annotation[0],
                annotation[1],
                annotation[2],
                annotation[3],
                annotation[4],
                annotation[5],
                annotation[6],
                annotation[7],
                annotation[8],
                annotation[9],
                annotation[10],
                annotation[11],
                annotation[12],
                len(data),
                sum_IE_length,
                token_IE,
                non_token_IE,
                data
            ]
        int_in_clause.append(a)
    else:
        print('se nem mon, se nem con:', filename, tier_id)

print(int_in_clause)

#DATAFRAME
labels = ["recording", "start", "end", "clause", "speech_type", "speaker", "age", "dialect",
          "location", "rutin", "words", "words_count", "clause_type", "IEs_count", "sum_IE_length", "token_IE",
          "no_word_IE", "IEs"]
all_data = pd.DataFrame.from_records(int_in_clause, columns=labels)

#új oszlopok hozzáadása a df-hez (clauseok hossza, összevont int_typok (csak reg az altípusok helyett))
all_data['length'] = all_data['end'] - all_data['start']
all_data['sum_no_word_IE'] = all_data['IEs_count'] - all_data['token_IE']
all_data['average_sum_no_word_IE'] = all_data['no_word_IE']/all_data['IEs_count']*100

#ÚJ DF_EK LÉTREHOZÁSA, HOGY KIKERÜLJENEK az elemezhetetlen és a nem nyelvi elemet tartalmazó egységek
#új df, amiben nincsenek se elemezhetetlen egységek = all_clause_data
df1 = all_data[all_data.clause_type != 'unknown']
all_clause_data = df1.reset_index(drop=True)

#új df, amiben nincsenek se elemezhetetlen, se nyelvi elemet nem tartalmazható egységek = clause_data
clause_data = all_clause_data[all_clause_data.clause_type != 'no_word']
clause_data = clause_data.reset_index(drop=True)

#EXPORT
clause_data.to_csv('all_clause_data3.csv', header=True)