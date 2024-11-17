"""Jumping Bug"""

lt=[float(input()) for _ in range(5)]
total_distance,jump_factor,end_gap,pit_start,pit_end=lt

finish=total_distance-end_gap
cnt,pos=0,0
distance_left=total_distance
while pos<finish:
    pos+=jump_factor*distance_left
    if pit_start<=pos<=pit_end:
        pos=pit_end
    cnt+=1
    distance_left=total_distance-pos

print(cnt)
