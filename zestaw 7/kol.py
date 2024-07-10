def wstaw(p, n):
    flag = True
    cnt = 0
    pc = p.next 
    kc = p.next.next
    while p != pc or flag:
        if p ==pc:
            flag = False
            if n[0] == pc.val[-1]:
                flag2 = False
                while (n[-1] != kc.val[0] and kc != pc) or not flag:
                    flag2 = True
                    kc = kc.next
                    cnt += 1
                p = p.next
            else:
                return False
    return cnt 