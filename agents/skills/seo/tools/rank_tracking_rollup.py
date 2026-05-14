#!/usr/bin/env python3
"""Aggregate rank snapshots into actionable delta events.

Input CSV columns:
keyword,page,device,location,rank_previous,rank_current,serp_features,change_window
"""

from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class RankEvent:
    keyword: str
    page: str
    device: str
    location: str
    rank_previous: int
    rank_current: int
    delta: int
    classification: str
    serp_features: str
    change_window: str


def classify(delta: int) -> str:
    if delta <= -3:
        return "gain"
    if delta >= 3:
        return "loss"
    if abs(delta) <= 1:
        return "flat"
    return "volatile"


def to_int(value: str) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def load_events(path: str) -> List[RankEvent]:
    events: List[RankEvent] = []
    with open(path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            previous = to_int(row.get("rank_previous", "0"))
            current = to_int(row.get("rank_current", "0"))
            delta = current - previous
            events.append(
                RankEvent(
                    keyword=row.get("keyword", "").strip(),
                    page=row.get("page", "").strip(),
                    device=row.get("device", "").strip(),
                    location=row.get("location", "").strip(),
                    rank_previous=previous,
                    rank_current=current,
                    delta=delta,
                    classification=classify(delta),
                    serp_features=row.get("serp_features", "").strip(),
                    change_window=row.get("change_window", "").strip(),
                )
            )
    return events


def summarize(events: List[RankEvent]) -> dict:
    summary = {"gain": 0, "loss": 0, "flat": 0, "volatile": 0}
    for event in events:
        summary[event.classification] = summary.get(event.classification, 0) + 1
    return {
        "count": len(events),
        "classification_totals": summary,
        "events": [asdict(e) for e in events],
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: rank_tracking_rollup.py <input.csv>")
        return 2

    events = load_events(sys.argv[1])
    print(json.dumps(summarize(events), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
