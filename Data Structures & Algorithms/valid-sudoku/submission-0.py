class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowres = [set() for i in range(0, 9)]
        colres = [set() for i in range(0, 9)]
        boxres = [set() for i in range(0, 9)]

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == ".": continue

                #print(j, i, n)
                rr = rowres[i]
                if n in rr:
                    #print("row fail", rr) 
                    #print(rowres)
                    return False
                rr.add(n)

                cc = colres[j] 
                if n in cc: 
                    #print("col fail")
                    return False
                cc.add(n)

                gridKey = math.floor(j/3) + math.floor(i/3)*3
                bb = boxres[gridKey]
                if n in bb: 
                    #print("box fail")
                    return False
                bb.add(n)

        return True
