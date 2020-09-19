/*
K번째수
https://programmers.co.kr/learn/courses/30/lessons/42748?language=javascript
*/
function solution(array, commands) {
    var answer = [];
    for(let index = 0; index < commands.length; index++) {
        let [i,j,k] = commands[index];
        answer.push(array.slice(i-1,j).sort((a,b) =>  a-b)[k-1]);
    }
    console.log(answer);
    return answer;
}

// 참고 필요 - sorting : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort