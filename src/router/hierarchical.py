"""Two-level language-family / encoder router."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RoutingDecision:
    family: str
    encoder: str
    score: float


class HierarchicalRouter:
    def __init__(self, family_centroids: dict[str, list[float]], encoder_map: dict[str, str]):
        self.family_centroids = family_centroids
        self.encoder_map = encoder_map

    def route(self, embedding: list[float]) -> RoutingDecision:
        best_family, best_score = None, float("-inf")
        for family, centroid in self.family_centroids.items():
            score = sum(a * b for a, b in zip(embedding, centroid))
            if score > best_score:
                best_family, best_score = family, score
        return RoutingDecision(family=best_family, encoder=self.encoder_map[best_family], score=best_score)
