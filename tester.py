
import csv
import time
from bot import ask, contains_secret
from attacks import ATTACKS


def run_tests(defended, filename):
    results = []

    mode = "DEFENDED" if defended else "BASELINE"
    print(f"\n=== {mode} TESTS ===")

    for i, attack in enumerate(ATTACKS, 1):
        try:
            reply = ask(attack, defended=defended)
            leaked = contains_secret(reply)
            status = "LEAKED" if leaked else "No direct leak detected"

            print(f"{i:2}. {status} | {attack[:55]}")

            results.append([
                i,
                attack,
                reply.replace("\n", " "),
                leaked,
                "OK",
            ])

        except Exception as error:
            print(f"{i:2}. ERROR | {error}")
            results.append([i, attack, "", False, str(error)])

        time.sleep(3)

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "attack", "reply", "leaked", "status"])
        writer.writerows(results)

    successful = sum(1 for row in results if row[4] == "OK")
    leaks = sum(1 for row in results if row[3] and row[4] == "OK")

    print(f"\n{mode}: {leaks} detected leaks; {successful}/{len(ATTACKS)} tests completed.")
    print(f"Saved results to {filename}")

    return leaks, successful


if __name__ == "__main__":
    baseline_leaks, baseline_done = run_tests(
        False, "results_baseline.csv"
    )
    defended_leaks, defended_done = run_tests(
        True, "results_defended.csv"
    )

    print("\n=== COMPARISON ===")
    print(f"Baseline: {baseline_leaks} detected leaks ({baseline_done}/20 completed)")
    print(f"Defended: {defended_leaks} detected leaks ({defended_done}/20 completed)")
