import re


class PhoneDetailsGetter:
    producers_list = ['samsung',
                      'google',
                      'realme',
                      'alcatel',
                      'apple',
                      'oneplus',
                      'motorola',
                      'xiaomi',
                      'huawei',
                      'myphone',
                      'maxcom',
                      'blackview',
                      'evolveo',
                      'alcor',
                      'panasonic',
                      'nokia',
                      'sony',
                      'honor',
                      'asus',
                      'oppo',
                      ]

    def get_details(self, title):
        title = title.lower()
        title=title.replace('telefon mobil','')
        for producer in self.producers_list:
            if producer in title:
                has_model = re.search('{0} .[^,]+,'.format(producer), title)
                if has_model is None:
                    has_model = re.search('{0} \\S+ \\S+'.format(producer), title)
                    if has_model is None:
                        return None
                model = (has_model.group())
                model = model.replace(producer, '').replace(',', '')

                return producer, model

        return None
