using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GitHub.Beakjoon
{
    public class test
    {
        static void Main(string[] args){
            // 입력 문자열을 공백기준 자름 그리고 배열 저장
            string[] s = Console.ReadLine().Split();
            // 배열의 0번과 1번을 더함, int형으로 변환
            Console.WriteLine(int.Parse(s[0]) + int.Parse(s[1]));
        }
    }
}