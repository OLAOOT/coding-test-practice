#include <stdio.h>

/* 
100기준
101+100+101이상? 재귀
만약 실패시
100-1~100+1? 1개
200-2보다 작음? 실패
200-2~200+2? 2개
300-4보다 작음? 실패
300-4~300+4? 3개
...

t: try,양옆에 끼는 수. 0부터 시작
n: 재귀 중 양옆에 끼는 수 제거한 수
judge() 실패 시 0 리턴

*/
    int dis(int st)
    {
        int i;
        int sum = 0;
        
        for (i = 1; i <= st / 2; i++)
            sum += i;
            
        return st % 2 == 1 ? sum * 2 + i : sum * 2;
    }

    int secondJudge(int t, int n, int st) //st: secondJudgeTry (startValue: 1)
    {
        if (n >= t * st - dis(st) && n <= t * st + dis(st))
            return st;
        else
            if (n < t * (st + 1))
                return 0;
            else
                return secondJudge(t, n, st + 1);
    }
    
    
    int firstJudge(int t, int n) //t: try n: num
    {
        if (n > (t + 1) + t + (t + 1))
        {
            int tmp = firstJudge(t + 1, n - (t + 1) * 2);
            if (tmp)
                return 2 + tmp;
        }
        
        return secondJudge(t, n, 1);
    }
    
    
    
 int main()
 {   
     int T;
     int i;
     scanf("%d", &T);
     
     for (i = 0; i < T; i++)
     {
         int x, y;
         scanf("%d %d", &x, &y);
         printf("%d\n", firstJudge(0, y - x));
     }
     
    
    return 0;
}