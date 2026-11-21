"""tl-gtin <barcode> — check and normalise a barcode (EAN-13, UPC-A, EAN-8, GTIN-14).

Prints: cleaned digits, type, whether the check digit is right, search variants (UPC-A ↔ EAN-13 with leading 0).
Wrong check digit: the correct check digit and a hint at typos/transposed digits.
Note: Discogs catalogue numbers are sometimes the barcode without check digit (e.g. Sony 88883716862).
"""
import re
import sys

from tracklist.common import die, run_cli

TYPES = {8: "EAN-8", 12: "UPC-A", 13: "EAN-13", 14: "GTIN-14"}


def check_digit(body: str) -> int:
    s = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(body)))
    return (10 - s % 10) % 10


def analyse(code: str) -> list[str]:
    digits = re.sub(r"\D", "", code)
    out = [f"input: {code!r} → digits: {digits} ({len(digits)} digits)"]
    if len(digits) not in TYPES:
        if len(digits) in (11, 12):
            out.append(f"Note: {len(digits)} digits – possibly a barcode without check digit (catalogue number?). "
                       f"With check digit: {digits}{check_digit(digits)}")
        out.append("valid: no (not a GTIN length 8/12/13/14)")
        return out
    body, cd = digits[:-1], int(digits[-1])
    ok = check_digit(body) == cd
    out.append(f"type: {TYPES[len(digits)]}  valid: {'yes' if ok else 'NO'}")
    if not ok:
        out.append(f"check digit should be {check_digit(body)} → corrected: {body}{check_digit(body)} "
                   "(or a typo/transposed digits elsewhere)")
    variants = {digits}
    if len(digits) == 12:
        variants.add("0" + digits)
    if len(digits) == 13 and digits.startswith("0"):
        variants.add(digits[1:])
    if len(digits) == 14 and digits.startswith("0"):
        variants.add(digits[1:])
    out.append("search variants: " + ", ".join(sorted(variants, key=len)))
    if len(digits) == 13:
        prefix = digits[:3]
        if "400" <= prefix <= "440":
            out.append("prefix 400–440: assigned in Germany (says nothing about the country of release)")
    return out


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        die(__doc__.strip(), 0)
    for code in sys.argv[1:]:
        print("\n".join(analyse(code)))


if __name__ == "__main__":
    run_cli(main)
