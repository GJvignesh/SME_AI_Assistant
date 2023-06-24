
class Preprocess:

    @staticmethod
    def pre_preprocess_text(list_of_text: list[str]) -> list[str]:
        """
        Takes list of raw string and pre-process it according to need for
        chat-gpt prompt
        :param list_of_text:
        :return: preprocessed string
        """
        processed_str = []
        for sub in list_of_text:
            print(sub)
            processed_str.append(sub.replace("\n", ""))
        return processed_str
