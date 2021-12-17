import math

def roots(rn):
    try:
        rs = rn.split()
        try:
            root =list(map(int,rs))
            print(root)
            if len(root) != 3:
                print("Tre tall!\n")
                return None
            else:
                a = root[0]
                b = root[1]
                c = root[2]
                if a == 0:
                    print("Ikke kvadratisk\n")
                    return None
                else:
                    dis = b * b - 4 * a * c
                    solve = math.sqrt(abs(dis))
                    if dis < 0:
                        rn = [-b / (2 * a), -b / (2 * a)]
                        cn = [solve, -solve]
                        sol = str(rn) + "+ j " + str(cn)
                    elif dis == 0:
                        sol = str([-b / (2 * a)])
                    else:
                        sol = str([(-b + solve) / (2 * a), (-b - solve) / (2 * a)])
                    print("Polynomene gitt av " + str(root) + "har røtter i: " + str(sol))
                    return 1
        except ValueError:
            print("Prøv igjen\n")
    except IOError:
        print("Prøv igjen\n")

rn=input("Gi meg de tre tallene for andregradsformelen!:\n")
poly = roots(rn)
if roots(rn) == None:
    roots(rn)