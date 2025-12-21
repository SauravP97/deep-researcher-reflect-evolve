"""Utility functions for agent context management."""

from structured_outputs.model_outputs import SearchQuery, SearchAnswer


def add_past_chat_to_context(
    query: SearchQuery, answer: SearchAnswer, context_path: str
) -> None:
    """Add past chat interactions to the agent context."""
    with open(context_path, "a") as file:
        file.write(f"Search Query: {query['query']}\n")
        file.write(f"Search Answer: {answer['answer']}\n\n")
    print("Chat added to context.")


def get_full_context(context_path: str) -> str:
    """Retrieve the full agent context from the specified path."""
    with open(context_path, "r") as file:
        return file.read()
    print("Full context retrieved.")


def clear_context(context_path: str) -> None:
    """Clear the agent context."""
    with open(context_path, "w") as file:
        pass
    print("Context cleared.")
