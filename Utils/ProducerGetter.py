class ProducerGetter:
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

    def get_producer(self, title):
        title = title.lower()
        for producer in self.producers_list:
            if producer in title:
                return producer

        return ""
