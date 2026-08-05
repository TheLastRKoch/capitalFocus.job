from datetime import datetime


class DateUtils:

    def formatter(self, date, source_format, target_format):
        raw_date = datetime.strptime(date, source_format)
        return datetime.strftime(raw_date, target_format)

    def get_month_number(self, month_key):
        eng_table = {
            'jan': '1',
            'feb': '2',
            'mar': '3',
            'apr': '4',
            'may': '5',
            'jun': '6',
            'jul': '7',
            'aug': '8',
            'sep': '9',
            'oct': '10',
            'nov': '11',
            'dec': '12',
        }

        esp_table = {
            'ene': '1',
            'feb': '2',
            'mar': '3',
            'abr': '4',
            'may': '5',
            'jun': '6',
            'jul': '7',
            'ago': '8',
            'sep': '9',
            'oct': '10',
            'nov': '11',
            'dic': '12',
        }

        month_key_to_search = month_key.lower()

        if month_key_to_search in eng_table.keys():
            return eng_table[month_key_to_search]
        if month_key_to_search in esp_table.keys():
            return esp_table[month_key_to_search]

    def replace_month_key_with_number(self, date):
        date_str = date.replace(" ", "")
        month_key = date_str[:3]
        month_number = self.get_month_number(month_key)
        return date_str.replace(month_key, month_number)
