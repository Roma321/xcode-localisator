from googletrans import Translator
import json

translator = Translator()


def main():
    with open('trans.json', 'r') as f:
        data = json.load(f)
    strings = data['strings']
    localization_keys = []
    sdfsdfg = strings['001']['localizations']
    for x in sdfsdfg:
        localization_keys.append(x)
    print(localization_keys)
    for word_number in strings:

        info_by_key = strings[word_number]

        if info_by_key is None:
            strings[word_number] = {}
            print('ПОКА НЕ РЕАЛИЗОВАНО')
            # strings[word_number]['localizations'] = [get_localization_]
        else:
            all_locs = info_by_key['localizations']
            eng_loc = all_locs['en']
            eng_word = eng_loc['stringUnit']['value']
            for localization in localization_keys:
                if localization not in all_locs or all_locs[localization]['stringUnit']['value'] is None:
                    translated_word = transalte_word(eng_word, localization)
                    all_locs[localization] = {}
                    all_locs[localization]['stringUnit'] = {}
                    all_locs[localization]['stringUnit']['value'] = translated_word
                    all_locs[localization]['stringUnit']['state'] = 'translated'
    with open('res.json', 'w') as res_file:
        json.dump(data, res_file, ensure_ascii=False, indent=4)


def get_localisation_google(localization):
    inner_localization = localization
    if localization == 'nb':
        inner_localization = 'no'
    if localization == 'zh-Hant' or localization == 'zh-HK':
        inner_localization = 'zh-TW'
    if localization == 'zh-Hans':
        inner_localization = 'zh-CN'
    return inner_localization


def transalte_word(eng_word, localization):
    inner_localization = get_localisation_google(localization)
    if inner_localization.startswith('en'):
        translated_word = eng_word
    else:
        try:
            translated_word = translator.translate(eng_word, src='en', dest=inner_localization).text
        except:
            # print(
            #     f'localization problem: can not find {inner_localization}, translate to {inner_localization[:2]}')

            translated_word = translator.translate(eng_word, src='en', dest=inner_localization[:2]).text
    return translated_word


main()

# print(data)
# translated_text = translator.translate('안녕하세요.')
# print(translated_text.text)
#
# translated_text = translator.translate('안녕하세요.', dest='ja')
# print(translated_text.text)
#
# translated_text = translator.translate('veritas lux mea', src='la')
# print(translated_text.text)
