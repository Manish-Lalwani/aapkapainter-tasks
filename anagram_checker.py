from typing import List


class AnagramCheck:
    def anagram_checker(self,string1:str,string2:str) -> str:
        l1:List[str] = list(string1.lower())
        l2:List[str] = list(string2.lower())
        for x in l1:
            if x in l2:
                l2.remove(x)
            else:
                return "no"
        return "yes"


if __name__ == "__main__":
    try:
        string1: str = input("Enter first string: ")
        string2: str = input("Enter second string: ")
        ac: AnagramCheck = AnagramCheck()

        print(ac.anagram_checker(string1=string1,string2=string2))
    except Exception as e:
        print(f"Following exception has occurred:   {e}")