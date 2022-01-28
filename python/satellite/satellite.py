"""Compute trees from traversals."""

def tree_from_traversals(preorder: list[str], inorder: list[str]) -> dict:
    """Return a tree from traversals."""
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")

    if not preorder:
        return {}

    # The first element of the preorder is always the root.
    root = preorder[0]
    # The inorder can be partitioned on the root to give the left and right inorder.
    idx = inorder.index(root)
    inorder_sub = inorder[:idx], inorder[idx + 1:]
    # With N = len(left subtree), preorder left can be found by taking the next N
    # elements after the root. The rest are preorder right.
    preorder_sub = (
        preorder[1:len(inorder_sub[0]) + 1],
        preorder[len(inorder_sub[0]) + 1:],
    )
    return {
        "v": root,
        "l": tree_from_traversals(preorder_sub[0], inorder_sub[0]),
        "r": tree_from_traversals(preorder_sub[1], inorder_sub[1]),
    }
