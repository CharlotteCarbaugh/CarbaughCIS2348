# Charlotte Carbaugh, ID 1815532
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError(print("Invalid age."))
    return age


def fat_burning_heart_rate(age):
    fat_rate = .7 * (220 - age)
    return fat_rate


def main():

    age_pass = 0

    try:
        age_pass = get_age()
        fat_burn = fat_burning_heart_rate(age_pass)
        print("Fat burning heart rate for a", age_pass, "year-old:", '{:.1f}'.format(fat_burn), "bpm")
    except ValueError:
        print("Could not calculate heart rate info.\n")


if __name__ == "__main__":
    main()

