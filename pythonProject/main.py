class 부모:
    def 테스트(self):
        print("안녕하세요!")


class 자식(부모):
    pass


c = 자식()
c.테스트()


class 자동차:
    def 부품(self):
        print("데쉬보드입니다.")

    def 악세사리(self):
        print("방향제입니다.")


class 내부(자동차):
    pass


a = 내부()
a.악세사리()

목록 = [1, 52, 273, 32, 99, 101]

최대값 = 목록[0]
최소값 = 목록[0]

for i in 목록:
    if i < 최소값:
        최소값 = i

    if i > 최대값:
        최대값 = i

print(최대값)
print(최소값)
