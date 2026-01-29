def recall_at_k(relevant_items, retrieved_items):
    relevant = set(relevant_items)
    retrieved = set(retrieved_items)

    if len(relevant) == 0:
        return 0.0

    return len(relevant & retrieved) / len(relevant)


def precision_at_k(relevant_items, retrieved_items):
    relevant = set(relevant_items)
    retrieved = set(retrieved_items)

    if len(retrieved) == 0:
        return 0.0

    return len(relevant & retrieved) / len(retrieved)
