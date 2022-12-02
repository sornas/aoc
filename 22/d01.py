import sys

def main():
    elfs = "".join(sys.stdin)
    per_elf = elfs.split("\n\n")
    per_per_elf = [list(map(int, elf.strip().split("\n"))) for elf in per_elf]
    sum_per_elf = [sum(elf) for elf in per_per_elf]
    print(max(sum_per_elf))
    print(sum(sorted(sum_per_elf)[-3:]))

main()
