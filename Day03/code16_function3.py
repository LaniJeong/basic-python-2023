# date : 2023-02-01
# author : Lani Jeong
# desc : 함수
## 매개변수가 일정치 않은 경우
def add(*args):
    result = 0
    for i in args:
        result += i

    return result

print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))
print(add(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))


