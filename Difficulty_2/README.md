# Difficulty 2

- [1926. 간단한 369게임](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)
  - str(), count()
- [2007. 패턴 마디의 길이](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)
  - 문자열 슬라이싱
- [1989.초심자의 회문검사](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)
  - 슬라이싱. n[시작 인덱스 : 끝 인덱스 : 간격]
- [1986. 지그재그 숫자](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)
- [1984. 중간 평균값 구하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)
  - 리스트명.sort(), del 리스트명[삭제할 인덱스], round(값, 몇째자리에서 반올림할건지)
  - round(값)만 하면 소수점 첫째자리에서 반올림함. 2라고 하면 소수점 3째자리에서 반올림해서 2째자리까지 보여줌. -1이라고 하면 1의 자리에서 반올림.
- [1983. 조교의 성적 매기기](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1)
  - 리스트, 딕셔너리를 잘 이해해야 할 듯..!
  - 변수명 정하기 어려웠음... k가 겹쳐서 문제 생기기도 했음. 
  - 딕셔너리에서 value값을 가지고 정렬하기. ```new_students=sorted(students.items(),key=lambda x:x[1], reverse=True)```
- [1970.쉬운 거스름돈](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2)
- [1966. 숫자를 정렬하자](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2)
  - 정렬은 그냥 sort()로 했는데, 정렬도 하나 하나 했어야 하는 건가..? 나중에 정렬도 직접 해봐야지.
- [1204. 최빈수 구하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3)
  - 처음에는 최빈수가 여러 개이면 어떻게 할지는 고려하지 않고 그냥 index()로 했더니 틀림.
  - 나중에는 `filter`를 이용해서, 최빈수가 여러 개일 경우 **모두** 뽑아내고, 그 중 **가장 큰 수**를 출력했다.
- [1284. 수도 요금 경쟁](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3)

