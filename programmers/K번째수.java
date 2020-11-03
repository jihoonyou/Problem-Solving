import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        int index = 0;
        for(int[] command: commands) {
            int i = command[0]-1;
            int j = command[1];
            int k = command[2]-1;
            System.out.println(Arrays.toString(command));
            int[] subarr = Arrays.copyOfRange(array, i, j);
            Arrays.sort(subarr);
            answer[index] = subarr[k];
            index += 1;
        }
        return answer;
    }
}