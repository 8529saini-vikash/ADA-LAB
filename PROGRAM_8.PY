import heapq
from itertools import count


class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies):
        if not frequencies:
            raise ValueError("Frequency dictionary cannot be empty.")

        if any(frequency <= 0 for frequency in frequencies.values()):
            raise ValueError("All frequencies must be positive.")

        unique_order = count()
        priority_queue = []

        for character, frequency in frequencies.items():
            node = Node(character, frequency)
            heapq.heappush(
                priority_queue, (frequency, next(unique_order), node)
            )

        while len(priority_queue) > 1:
            first_frequency, _, first_node = heapq.heappop(priority_queue)
            second_frequency, _, second_node = heapq.heappop(priority_queue)

            merged_node = Node(
                None, first_frequency + second_frequency
            )
            merged_node.left = first_node
            merged_node.right = second_node

            heapq.heappush(
                priority_queue,
                (merged_node.frequency, next(unique_order), merged_node)
            )

        self.root = priority_queue[0][2]
        return self.root

    def generate_codes(self):
        if self.root is None:
            raise ValueError("Build the Huffman tree before generating codes.")

        self.codes = {}

        def traverse(node, code):
            if node.character is not None:
                self.codes[node.character] = code if code else "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")
        return self.codes


# Character frequency table
frequencies = {
    "A": 5,
    "B": 9,
    "C": 12,
    "D": 13,
    "E": 16,
    "F": 45
}

coder = HuffmanCoder()
coder.build_tree(frequencies)
codes = coder.generate_codes()

print("Huffman Codes:")
for character in sorted(codes):
    print(f"{character}: {codes[character]}")
