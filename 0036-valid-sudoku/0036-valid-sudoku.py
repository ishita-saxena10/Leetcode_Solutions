class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        # 3x3 Grid check
        for i in range(0,9,3):
            for j in range(0,9,3):
                chk = []
                for m in range(i, i+3):
                    for n in range(j,j+3):
                        if b[m][n] in chk: return False
                        if b[m][n]!=".":
                            chk.append(b[m][n])
        # Row Check
        for i in b:
            tmp = []
            for j in i:
                if j in tmp: return False
                if j !=".":
                    tmp.append(j)
        # Column Check
        for i in range(9):
            tmp = []
            for j in range(9):
                if b[j][i] in tmp: return False
                if b[j][i] != ".":
                    tmp.append(b[j][i])
        
        return True