class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        #if 4, 5 taken check 6 7
            #if 6 7 free add 1 if 8 9 are free
            #else we can't add anything
        
        #if 6, 7 taken check 4, 5
            #if 4, 5 free add 1 if 2, 3 free
            #else we can't add anything
        
        #if 4 5 6 7 free add 1

        reservedSeats.sort()
        m = len(reservedSeats)
        ans = 0 
        four_five = False
        six_seven = False
        two_three = False
        eight_nine = False
        seen = set()
        for i in range(m):
            next_seat_row = reservedSeats[i + 1][0] if i + 1 < m else -1
            curr_row, curr_seat = reservedSeats[i]
            seen.add(curr_row)
            if curr_seat in (2, 3):
                two_three = True
            elif curr_seat in (4, 5):
                four_five = True
            elif curr_seat in (6, 7):
                six_seven = True
            elif curr_seat in (8, 9):
                eight_nine = True
# [[1, 4], [1, 7], [4, 3], [4, 6]]

            if curr_row != next_seat_row:
                if not four_five and not six_seven:
                    if not two_three and not eight_nine:
                        ans += 2
                    else:
                        ans += 1
                elif four_five:
                    if not six_seven and not eight_nine:
                        ans += 1
                elif six_seven:
                    if not four_five and not two_three:
                        ans += 1
                
                four_five = False
                six_seven = False
                two_three = False
                eight_nine = False
        
        return ans + ((n - len(seen)) * 2)

        seats = defaultdict(set)

        for x, y in reservedSeats:
            if y in (2, 3, 4, 5, 6, 7, 8, 9):
                seats[x].add(y)
        ans = 0
        for i in range(1, n + 1):
    
            four_five = (4 in seats[i] or 5 in seats[i])
            six_seven = (6 in seats[i] or 7 in seats[i])
            two_three = (2 in seats[i] or 3 in seats[i])
            eight_nine = (8 in seats[i] or 9 in seats[i])
            if not four_five and not six_seven:
                if not two_three and not eight_nine:
                    ans += 2
                else:
                    ans += 1
            elif four_five:
                if not six_seven and not eight_nine:
                    ans += 1
            elif six_seven:
                if not four_five and not two_three:
                    ans += 1
        
        return ans

            
                


            



        