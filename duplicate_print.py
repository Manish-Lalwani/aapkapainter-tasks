from typing import List


class DuplicateCheck:

    def first_duplicate_occurrence_print(self,l1:List[int]) -> None:
        """
        Prints only the first occurrence of a duplicate
        """
        l2:List[int] = []
        for x in l1:
            if x in l2:
                print(x)
                break
            else:
                l2.append(x)


if __name__ == "__main__":
    try:
        l1: List[int] = [int(x) for x in input("Enter numbers separated by space: ").split()]
        dc: DuplicateCheck = DuplicateCheck()
        dc.first_duplicate_occurrence_print(l1=l1)
    except Exception as e:
        print(f"Following exception has occurred:   {e}")

