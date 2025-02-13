def startstop(funkcja):
    def wrapper(*args):
        print("_" * 50)
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")

    return wrapper


def zawijanie(cos):
    print(f"zawijanie {cos} w sreberka....")


wr = startstop(zawijanie)
print(wr)
wr("sreberka")


@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na urodziny')


dmuchanie("świeczek")
