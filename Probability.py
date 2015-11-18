class Probability:
    def __init__(self, probability, category, instance):
        self.probability = probability
        self.category = category
        self.instance = instance

    def __float__(self):
        return self.probability

    def __cmp__(self, other):
        diff = self.probability - float(other)
        if diff < 0:
            return -1
        elif diff > 0:
            return 1
        return 0


class CombinedProbability:
    def __init__(self):
        self.items = list()
        self.probability = 1.0

    def __float__(self):
        return self.probability

    def __cmp__(self, other):
        diff = self.probability - float(other)
        if diff < 0:
            return -1
        elif diff > 0:
            return 1
        return 0

    def add(self, item):
        # assert that item is a probability
        assert isinstance(item, Probability)
        self.items.append(item)
        self.probability *= float(item)
