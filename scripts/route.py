"""Route a single query through the hierarchical router."""
import argparse

from src.router.hierarchical import HierarchicalRouter


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    args = parser.parse_args()
    router = HierarchicalRouter({"latin": [1.0, 0.0], "cyrillic": [0.0, 1.0]}, {"latin": "enc-a", "cyrillic": "enc-b"})
    print(router.route([0.8, 0.2]))


if __name__ == "__main__":
    main()
