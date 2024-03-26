class Phone:
    IMEI = None
    Producer = "WB"

    def call_by_4g(self):
        print("4g通话")


class Phone2023(Phone):
    faceId = None

    def call_by_5g(self):
        print("5g通话")


phone = Phone2023()
print(phone.Producer)
phone.call_by_4g()
phone.call_by_5g()
phone.faceId="222"
print(phone.faceId)
