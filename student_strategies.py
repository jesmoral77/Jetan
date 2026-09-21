"""Implement student evaluation, prompting, parsing, and fallback functions."""

from collections.abc import Sequence

from jetan import JetanBoard, Move, Player


def evaluate_position_1(board: JetanBoard, perspective: Player) -> float:
    raise NotImplementedError


def evaluate_position_2(board: JetanBoard, perspective: Player) -> float:
    raise NotImplementedError


def evaluate_position_3(board: JetanBoard, perspective: Player) -> float:
    raise NotImplementedError


def build_evaluation_prompt(
    board: JetanBoard, perspective: Player
) -> Sequence[dict[str, str]]:
    raise NotImplementedError


def parse_evaluation_response(response: str) -> float:
    raise NotImplementedError


def build_move_prompt(
    board: JetanBoard,
    actions: tuple[Move, ...],
    recent_moves: tuple[Move, ...],
) -> Sequence[dict[str, str]]:
    raise NotImplementedError


def parse_move_response(response: str, actions: tuple[Move, ...]) -> Move:
    raise NotImplementedError


def choose_fallback(board: JetanBoard, actions: tuple[Move, ...]) -> Move:
    raise NotImplementedError
