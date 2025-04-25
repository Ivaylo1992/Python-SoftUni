def negative_vs_positive(*args):

    def sum_negatives(nums):
        return sum(n for n in nums if n < 0)

    def sum_positives(nums):
        return sum(n for n in nums if n > 0)

    def compare(negative_sum, positive_sum):
        if abs(negative_sum) > positive_sum:
            return "The negatives are stronger than the positives"
        return "The positives are stronger than the negatives"

    negatives = sum_negatives(*args)
    positives = sum_positives(*args)

    return '\n'.join([str(negatives), str(positives), compare(negatives, positives)])


sequence = num_sequence = [int(n) for n in input().split(' ')]
print(negative_vs_positive(sequence))

