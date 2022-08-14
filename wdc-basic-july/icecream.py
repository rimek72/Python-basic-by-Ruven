class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop of {self.flavor}'


class Bowl:
    MAX_SCOOPS = 3    # class attribute on Bowl

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            if len(self.scoops) >= Bowl.MAX_SCOOPS:
                break
            self.scoops.append(one_scoop)

    def flavors(self):
        # output = []
        # for one_scoop in self.scoops:
        #     output.append(one_scoop.flavor)
        # return output
        #
        # list comprehension!!
        return [one_scoop.flavor
                for one_scoop in self.scoops]

    def __repr__(self):
        output = 'Bowl of: \n'
        #
        # for index, one_scoop in enumerate(self.scoops):
        #     output += f'\t{index+1}: {one_scoop}\n'
        #
        # return output
        #

        output += '\n'.join([f'\t{index+1}: {one_scoop}'
                             for index, one_scoop in enumerate(self.scoops)])

        return output

    def __len__(self):
        return len(self.scoops)

    def __eq__(self, other):
        return [one_scoop.flavor for one_scoop in self.scoops] == [one_scoop.flavor for one_scoop in other.scoops]