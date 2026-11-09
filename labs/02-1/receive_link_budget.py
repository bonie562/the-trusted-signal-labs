"""Lab 2.1 from The Trusted Signal, Second Edition."""

import argparse
import math

THERMAL_NOISE_DBM_PER_HZ = -174.0
BANDWIDTHS_HZ = (10_000, 200_000, 2_000_000, 20_000_000)
REQUIRED_SNR_DB = 10.0
TARGET_DBM = -100.0


def noise_floor_dbm(bandwidth_hz, noise_figure_db):
    return THERMAL_NOISE_DBM_PER_HZ + 10 * math.log10(bandwidth_hz) + noise_figure_db


def main():
    parser = argparse.ArgumentParser(description="Estimate receiver sensitivity by bandwidth.")
    parser.add_argument("--noise-figure-db", type=float, default=6.0,
                        help="receiver noise figure in dB (default: 6)")
    args = parser.parse_args()
    if not math.isfinite(args.noise_figure_db) or args.noise_figure_db < 0:
        parser.error("--noise-figure-db must be a finite, nonnegative value")

    print(f"Receiver noise figure: {args.noise_figure_db:g} dB")
    print(f"{'Bandwidth (kHz)':>16} {'Noise floor (dBm)':>19} {'Minimum signal (dBm)':>22}")
    for bandwidth in BANDWIDTHS_HZ:
        floor = noise_floor_dbm(bandwidth, args.noise_figure_db)
        print(f"{bandwidth / 1_000:16,.0f} {floor:19.1f} {floor + REQUIRED_SNR_DB:22.1f}")

    exponent = (TARGET_DBM - REQUIRED_SNR_DB - THERMAL_NOISE_DBM_PER_HZ
                - args.noise_figure_db) / 10
    maximum_khz = 10 ** (exponent - 3)
    print()
    print(f"Maximum bandwidth for a {TARGET_DBM:g} dBm signal at "
          f"{REQUIRED_SNR_DB:g} dB SNR: {maximum_khz:,.1f} kHz")


if __name__ == "__main__":
    main()
