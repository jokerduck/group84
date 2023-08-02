import hashlib
import base64


class MerkleTree:
    def __init__(self, leaves):
        self.leaves = leaves
        self.levels = self.build_tree()

    def build_tree(self):
        levels = [self.leaves]

        while len(levels[-1]) > 1:
            level = levels[-1]
            new_level = []
            for i in range(0, len(level), 2):
                if i + 1 < len(level):
                    hash_value = self.hash_nodes(level[i], level[i + 1])
                else:
                    hash_value = self.hash_nodes(level[i], level[i])
                new_level.append(hash_value)
            levels.append(new_level)

        return levels

    @staticmethod
    def hash_nodes(left, right):
        combined = left + right
        hash_value = hashlib.sha256(combined).digest()
        return base64.b64encode(hash_value)

    def root_hash(self):
        return self.levels[-1][0]
    def print_tree(self):
        for level in self.levels:
            for node in level:
                print('Node Hash:', node.decode())


leaves = [b'leaf1', b'leaf2', b'leaf3', b'leaf4']
print("h(leaf1+leaf2)",base64.b64encode(hashlib.sha256(leaves[0]+leaves[1]).digest()).decode())
print("h(leaf3+leaf4)",base64.b64encode(hashlib.sha256(leaves[2]+leaves[3]).digest()).decode())
tree = MerkleTree(leaves)
print('Root Hash:', tree.root_hash().decode())
tree.print_tree()
