import random 

    # ------------------------------------ ref กานต์ สุขสมกิจ ------------------------------------ 
class Bot_MsOlivia:
    def check_position_can_move(self,mark,list_board,another) :
        position_collect = []
        point_collect = []
        for r in range(8)  :
            for c in range(8) :
                point = 0
                if list_board[r][c]["image"] == mark :
                    point += self.get_point_top(list_board,another,r,c)
                    point += self.get_point_top_left(list_board,another,r,c)
                    position_collect.append((r,c))
                    point_collect.append(point)
                    
        if len(point_collect) == 0: # if there is no point
            return 0 # stop
        point = max(point_collect)
        index = point_collect.index(point)
        most_point = position_collect[index]
        row = most_point[0]
        col = most_point[1]
        return list((row,col))

    def get_point_top(self,list_board,another,row,col):
            point = 0
            for looprow in range(row-1,-1,-1) :
                if list_board[looprow][col] == another :
                    point+=1
                else :
                    return point

    # หาตำแหน่งที่มี marker
    def check_position_can_move(self,mark,list_board,another,empty,current) :
        position_collect = []
        point_collect = []
        for r in range(8)  :
            for c in range(8) :
                point = 0
                if list_board[r][c]["image"] == mark :
                    # นับคะแนนจาก marker ในแต่ละด้าน
                    point += self.get_point_top(list_board,another,r,c,empty,mark,current)
                    point += self.get_point_left(list_board,another,r,c,empty,mark,current)
                    point += self.get_point_bottom(list_board,another,r,c,empty,mark,current)
                    point += self.get_point_right(list_board,another,r,c,empty,mark,current)
                    point += self.get_point_top_left(list_board,another,r,c,empty,mark,current)
                    point += self.get_point_top_right(list_board,another,r,c,empty,mark,current)
                    point += self.get_point_bottom_left(list_board,another,r,c,empty,mark,current)
                    point += self.get_point_bottom_right(list_board,another,r,c,empty,mark,current)
                    position_collect.append((r,c))
                    point_collect.append(point)
        if len(point_collect) == 0: # if there is no point
            return 0 # stop
        # หาแต้มที่มากที่สุดและเก็บค่า row,column
        point = max(point_collect)
        index = point_collect.index(point)
        most_point = position_collect[index]
        row = most_point[0]
        col = most_point[1]
        return list((row,col))

    def get_point_top(self,list_board,another,row,col,empty,mark,current):
            point = 0
            for looprow in range(row-1,-1,-1) :
                if list_board[looprow][col]["image"] == another :
                    point+=1
                elif list_board[looprow][col]["image"]== empty or list_board[looprow][col]["image"]== mark  :
                    return 0
                elif list_board[looprow][col]["image"]== current :
                    return point
            return 0 
                
    def get_point_bottom(self,list_board,another,row,col,empty,mark,current):
            point = 0
            for looprow in range(row+1,8) :
                if list_board[looprow][col]["image"] == another :
                    point+=1
                elif list_board[looprow][col]["image"]== empty or list_board[looprow][col]["image"]== mark  :
                    return 0
                elif list_board[looprow][col]["image"]== current :
                    return point
            return 0
    def get_point_right(self,list_board,another,row,col,empty,mark,current):
            point = 0
            for loopcol in range(col+1,8) :
                if list_board[row][loopcol]["image"] == another :
                    point+=1
                elif list_board[row][loopcol]["image"]== empty or list_board[row][loopcol]["image"]== mark  :
                    return 0
                elif  list_board[row][loopcol]["image"]== current :
                    return point
            return 0
    def get_point_left(self,list_board,another,row,col,empty,mark,current):
            point = 0
            for loopcol in range(col-1,-1,-1) :
                if list_board[row][loopcol]["image"] == another :
                    point+=1
                elif list_board[row][loopcol]["image"]== empty or list_board[row][loopcol]["image"]== mark  :
                    return 0
                elif list_board[row][loopcol]["image"]== current:
                    return point
            return 0
                
    
    def get_point_top_left(self,list_board,another,row,col,empty,mark,current):
            point = 0
            a = 1
            while row-a > 0 and col-a > 0 :
                if list_board[row-a][col-a]["image"]==another: 
                    a+=1
                    point+=1
                elif list_board[row-a][col-a]["image"]== empty or list_board[row-a][col-a]["image"]== mark  :
                    return 0                      
                elif list_board[row-a][col-a]["image"]== current :
                    return point 
            return 0
    
    def get_point_bottom_right(self,list_board,another,row,col,empty,mark,current):
            point = 0
            a = 1
            while row+a < 8  and col+a < 8 :
                if list_board[row+a][col+a]["image"]==another: 
                    a+=1
                    point+=1
                elif list_board[row+a][col+a]["image"]== empty or list_board[row+a][col+a]["image"]== mark  :
                    return 0  
                elif list_board[row+a][col+a]["image"]== current :                 
                    return point
            return 0 
                 
    def get_point_bottom_left(self,list_board,another,row,col,empty,mark,current):
            point = 0
            a = 1
            while row+a < 8  and col-a > 0 :
                if list_board[row+a][col-a]["image"]==another: 
                    a+=1
                    point+=1
                elif list_board[row+a][col-a]["image"]== empty or list_board[row+a][col-a]["image"]== mark  :
                    return 0 
                elif list_board[row+a][col-a]["image"]== current :                    
                    return point
            return 0
    def get_point_top_right(self,list_board,another,row,col,empty,mark,current):
            point = 0
            a = 1
            while row-a > 0  and col+a < 8 :
                if list_board[row-a][col+a]["image"]==another: 
                    a+=1
                    point+=1
                elif list_board[row-a][col+a]["image"]== empty or list_board[row-a][col+a]["image"]== mark  :
                    return 0                      
                elif  list_board[row-a][col+a]["image"]== current :
                    return point
            return 0