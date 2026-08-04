from ai.database_context import get_database_context


def test_database_context():
    """
    Print the complete database context.
    """

    print(get_database_context())


if __name__ == "__main__":
    test_database_context()