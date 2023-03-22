from datetime import datetime

WEEKDAY_NAME_FORMAT_CODE = "%A"
MONTH_NAME_FORMAT_CODE = "%B"
MY_NAME = "Serafim"


def main():
    t = datetime.now()

    weekday_name = t.strftime(WEEKDAY_NAME_FORMAT_CODE)
    month_name = t.strftime(MONTH_NAME_FORMAT_CODE)

    print(weekday_name, month_name, MY_NAME, sep="\n")


if __name__ == "__main__":
    main()
