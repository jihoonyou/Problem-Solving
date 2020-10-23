import java.util.ArrayList;
import java.util.Deque;
import java.util.ArrayDeque;
import java.lang.Math;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList();
        Deque<Double> queue =  new ArrayDeque<Double>();
        int day = 0;
        
        for(int i = 0; i < progresses.length; i++) {
            double required = 100 - progresses[i];
            queue.add(Math.ceil(required/speeds[i]));
        }

        while(!queue.isEmpty()) {
            if (day < queue.getFirst()) {
                day += (queue.getFirst() - day);
            }
            else {
                int count = 0;
                while (!queue.isEmpty() && day >= queue.getFirst()) {
                    queue.removeFirst();
                    count += 1;
                }
                answer.add(count);                
            }   
        }
        return answer.stream().mapToInt(x -> x).toArray();
    }
}