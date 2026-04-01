import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# ── Matrix pins (from schematic) ──────────────────────────────────────────────
# Row 0 → GP0 | Row 1 → GP1 | Row 2 → GP2
# Col 0 → GP3 | Col 1 → GP4 | Col 2 → GP5

keyboard.col_pins = (board.GP3, board.GP4, board.GP5)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ── Rotary Encoder ─────────────────────────────────────────────────────────────
# R1 (A) → GP6 | R2 (B) → GP7 | C → GND

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.GP6, board.GP7, None, False),  # (pin_a, pin_b, button_pin, is_inverted)
)

keyboard.modules.append(encoder_handler)

# ── Keymap ─────────────────────────────────────────────────────────────────────
# Layer 0: numpad-style layout
# ┌───┬───┬───┐
# │ 7 │ 8 │ 9 │  ← Row 0
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │  ← Row 1
# ├───┼───┼───┤
# │ 1 │ 2 │ 3 │  ← Row 2
# └───┴───┴───┘
# Encoder CW → Vol Up | CCW → Vol Down

keyboard.keymap = [
    # Layer 0
    [
        KC.P7, KC.P8, KC.P9,
        KC.P4, KC.P5, KC.P6,
        KC.P1, KC.P2, KC.P3,
    ],
]

# Encoder actions per layer: (ccw_key, cw_key)
encoder_handler.map = [
    # Layer 0
    ((KC.VOLD, KC.VOLU),),
]

if __name__ == '__main__':
    keyboard.go()
